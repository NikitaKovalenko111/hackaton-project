from aiogram import Router, F
from aiogram.types import Message
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import os
import aiohttp

# Создаем роутер для навигатора
navigator_router = Router()

# Определяем состояния для FSM
class NavigatorStates(StatesGroup):
    start_point = State()
    end_point = State()
    waiting_for_next_step = State()

def img_pathnav(filename: str) -> str:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    parent2_dir = os.path.dirname(parent_dir)
    full_path = os.path.join(parent2_dir, 'photos', filename)
    if not os.path.exists(full_path):
        raise FileNotFoundError(f"Файл изображения не найден: {full_path}")
    return full_path



@navigator_router.message(F.text.lower() == "навигатор".lower())
async def navigator_command(message: Message, state: FSMContext):
    await message.answer("Введите начальную точку(Например, 6-101а - кабинет. Буквы в названии на русском языке.):")
    await state.set_state(NavigatorStates.start_point)

@navigator_router.message(NavigatorStates.start_point)
async def process_start_point(message: Message, state: FSMContext):
    await state.update_data(start_point=message.text)
    await message.answer("Введите конечную точку(Например, 6-101а - кабинет. Буквы в названии на русском языке.):")
    await state.set_state(NavigatorStates.end_point)

    @navigator_router.message(NavigatorStates.end_point)
    async def process_end_point(message: Message, state: FSMContext):
        await state.update_data(end_point=message.text)
        user_data = await state.get_data()
        start = user_data.get("start_point")
        end = user_data.get("end_point")

        # URL вашего сервера навигации
        SERVER_BASE_URL = "http://185.185.68.35:3001/navigate"
        full_url = f"{SERVER_BASE_URL}?start={start}&end={end}"

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(full_url) as response:
                    data = await response.json()

                    if response.status == 200:
                        if "error" in data:
                            await message.answer(f"Ошибка сервера: {data['error']}")
                            await state.clear()  # Очищаем состояние после ошибки
                            return
                        elif isinstance(data, list) and len(data) > 0:  # Ожидаем массив
                            # Сохраняем весь маршрут и текущий индекс в FSM
                            await state.update_data(current_route_data=data, current_route_index=0)

                            # Отправляем первую точку маршрута
                            await send_next_route_step(message, state)  # Вызываем функцию для отправки шага

                        else:
                            await message.answer("Маршрут не найден или ответ сервера некорректен. Проверьте правильность аудиторий.")
                            await state.clear()
                    else:
                        error_message = data.get("error", "Неизвестная ошибка сервера.")
                        await message.answer(f"Произошла ошибка при запросе к серверу ({response.status}): {error_message}")
                        await state.clear()

        except aiohttp.ClientConnectorError:
            await message.answer("Не удалось подключиться к серверу навигации. Попробуйте позже.")
            await state.clear()
        except aiohttp.ContentTypeError:
            await message.answer("Сервер навигации вернул некорректный ответ. Попробуйте позже.")
            await state.clear()
        except FileNotFoundError as e:  # Добавляем обработку ошибки, если img_pathnav не нашел файл
            await message.answer(f"Не удалось найти файл изображения: {e}. Пожалуйста, сообщите администратору.")
            await state.clear()
        except Exception as e:
            await message.answer(f"Произошла непредвиденная ошибка: {e}")
            await state.clear()

async def send_next_route_step(target_message: Message, state: FSMContext):
    user_data = await state.get_data()
    route_data = user_data.get("current_route_data")
    current_index = user_data.get("current_route_index")

    if route_data is None or current_index is None:
        await target_message.answer("Произошла ошибка при получении данных маршрута.")
        await state.clear()
        return

    # Проверяем, не закончился ли маршрут
    if current_index >= len(route_data):
        await target_message.answer("Вы достигли конечной точки! Маршрут завершен.")
        await state.clear() # Сбрасываем состояние после завершения маршрута
        return

    current_step = route_data[current_index]
    photo_filename = current_step.get("photo")
    nums = current_step.get("nums", [])

    caption_text = "Дойдите до этой точки."
    if nums:
        caption_text += f"\nОриентир(кабинеты, которые нвходятся рядом): {', '.join(nums)}"

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Продолжить", callback_data="navigate_next_step")]
    ])

    try:
        # Отправляем фото
        photo_file = FSInputFile(img_pathnav(photo_filename))
        await target_message.answer_photo(
            photo=photo_file,
            caption=caption_text,
            reply_markup=keyboard
        )
        # Переключаем состояние на ожидание нажатия кнопки "Продолжить"
        await state.set_state(NavigatorStates.waiting_for_next_step)
    except FileNotFoundError as e:
        await target_message.answer(f"Ошибка: Изображение '{photo_filename}' для текущего шага не найдено. {e}")
        await state.clear()
    except Exception as e:
        await target_message.answer(f"Произошла ошибка при отправке шага маршрута: {e}")
        await state.clear()


# ... (после других обработчиков в navigator.py) ...

@navigator_router.callback_query(F.data == "navigate_next_step", NavigatorStates.waiting_for_next_step)
async def handle_next_step_callback(callback: CallbackQuery, state: FSMContext):
    # Увеличиваем индекс текущего шага
    user_data = await state.get_data()
    current_index = user_data.get("current_route_index", 0)
    await state.update_data(current_route_index=current_index + 1)

    # Отправляем следующий шаг маршрута
    await send_next_route_step(callback.message, state)

    # Отвечаем на callback, чтобы кнопка не висела в состоянии "нажата"
    await callback.answer()