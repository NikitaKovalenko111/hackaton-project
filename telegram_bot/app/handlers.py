from aiogram.filters import CommandStart,Command
from aiogram import Router, F, html
from aiogram.types import Message, CallbackQuery, FSInputFile
import os

import app.keyboards as kb
from app.navigator import navigator_router
from app.circle import circle_router
from app.tuc import tuc_router
from app.facts import fact_router

def img_path(path):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Поднимаемся на один уровень вверх (в папку telegram_bot)
    parent_dir = os.path.dirname(current_dir)
    # Соединяем путь с папкой 'img' и файлом path
    photo_path = os.path.join(parent_dir, 'img', path)
    return photo_path

# Создаем роутер
router = Router()

# добавляем
router.include_router(navigator_router)
router.include_router(circle_router)
router.include_router(tuc_router)
router.include_router(fact_router)

@router.message(CommandStart()) # сообщение
async def command_start_handler(message: Message) -> None:
    photo_file = FSInputFile(img_path('start.jpg'))
    await message.answer_photo(
        photo=photo_file,
        caption=f"Приветик, {html.bold(message.from_user.full_name)}! Добро пожаловать! Я — твой путеводитель по университету. Здесь ты можешь найти карту кампуса, узнать расписание, получить информацию о студенческих объединениях и профкоме, а также найти ответы на самые важные вопросы. Спрашивай, что тебя интересует, и я помогу тебе освоиться!", reply_markup=kb.main  # подпись к фото
    )

@router.message(F.text.lower() == "cтуденческие объединения".lower()) # при выборе клавиши студ объед
async def command1(message: Message):
    await message.answer("Студенческие объединения и творческие коллективы – это объединение студентов Уфимского университета, где каждый занимается интересным для него делом в команде единомышленников.", reply_markup=kb.circle)


@router.message(F.text.lower() == "Карта".lower()) # при выборе клавиши карта
async def send_map_with_photo(message: Message):
    photo_file = FSInputFile(img_path('map.png'))
    await message.answer_photo(
        photo=photo_file,
        caption="Вот наша университетская карта!"  # подпись к фото
    )

@router.message(F.text.lower() == "Рассписание пар".lower()) # при выборе клавиши карта
async def send_map_with_photo(message: Message):
    photo_file = FSInputFile(img_path('time.png'))
    await message.answer_photo(
        photo=photo_file,
        caption="Длительность пар\n\nРасписание можно посмотреть на следующих платформах:\n- https://isu.uust.ru/schedule_2024/ — самое актуальное расписание\n- https://schedule.uust.ru/\n- @schedule_uust_bot\n\nПриложение:\n https://apps.apple.com/app/id6447134234\n https://www.rustore.ru/catalog/app/ru.uust_time.schedule"  #  подпись к фото
    )

@router.message(F.text.lower() == "фактики".lower()) # при выборе клавиши студ объед
async def command1(message: Message):
    await message.answer("Можешь выбрать наиболее встречаемый вопрос и получить ответ", reply_markup=kb.facts)

