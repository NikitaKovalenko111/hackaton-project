from aiogram.filters import CommandStart,Command
from aiogram import Router, F, html
from aiogram.types import Message, CallbackQuery, FSInputFile,InputMediaPhoto
import os

import app.keyboards as kb

def img_path(path):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Поднимаемся на один уровень вверх (в папку telegram_bot)
    parent_dir = os.path.dirname(current_dir)
    # Соединяем путь с папкой 'img' и файлом path
    photo_path = os.path.join(parent_dir, 'img', path)
    return photo_path
def file_path(path):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    # Предполагаем, что PDF-файлы лежат в папке 'files' в корне проекта
    document_path = os.path.join(parent_dir, 'files', path)
    return document_path

fact_router = Router()

"""
@fact_router.callback_query(F.data == 'fact')
async def fact(message: Message):
    await callback.message.answer("")
"""
@fact_router.callback_query(F.data == 'fact1')
async def fact1(callback: CallbackQuery):
    photo_file = FSInputFile(img_path('f1.png'))
    await callback.message.answer_photo(
        photo=photo_file,
        caption="Лекция - пара, когда несколько групп собирают в одной большой душной аудитории и читают им материал. Стоит ли ходить? 50/50. Если хотите всё знать и уметь, то смело вставайте к первой паре. Если вы верите в себя и одногрупника, который ходил и всё записывал, то можете продлить свой сон. (Некоторые преподы отмечают на лекциях и могут проводить контрольные, узнайте об этом заранее)\n\nПрактика - приходим, решаем задачки, вопросы решаем, ничего интересного. Ходить стоит, но если вы сверхчеловек, который сам всё может изучить, то появляйтесь хотя бы изредка\n\nЛабы - две пары подряд вы сидите и занимаетесь чем-то, прогуливать не стоит, потому что придётся отрабатывать. Защитить лабу - это показать, что вы разбираетесь в своей работе, а не списали её у друга за 10 минут до конца."  # подпись к фото
    )
    document_file = FSInputFile(file_path('Как читать учебный план.pdf'))
    await callback.message.answer_document(
        document=document_file,
        caption="Как читать учебный план?"
    )
    document_file = FSInputFile(file_path('Учебные_планы.xlsx'))
    await callback.message.answer_document(
        document=document_file
    )
    photo_file = FSInputFile(img_path('f2.png'))
    await callback.message.answer_photo(
        photo=photo_file,
        caption="Экзамен - приходишь, решаешь задачки или отвечаешь письменно на вопросы, потом бубнишь перед преподом защиту, получаешь оценку. Также на многих предметах можно получить автомат по экзамену - скипнуть заучивание материала, решение билета и защиту. Автомат можно получить по разным причинам, но чаще всего за успехи в учебе во время семестра.\n\nЗачёт - надо просто все вовремя сдать и получить зачёт или незачёт. У некоторых преподавателей на некоторых дисциплинах надо сдать зачетную работу, чтобы получить этот самый.\n\nДиф зачет aka зачет с оценкой aka дифференцированный зачет - то же самое, что зачет, но он может поднасрать тебе в стипуху, если получишь «удовл.» (троечка).\n\nПроект aka курсач - массивная чапалаха, которую ты делаешь в последнюю неделю, чтобы закрыть предмет, хотя у тебя был целый семестр для этого.\n\nСеместр - учебное полугодие"
    )
@fact_router.callback_query(F.data == 'fact2')
async def fact1(callback: CallbackQuery):
    photo_file = FSInputFile(img_path('f3.png'))
    await callback.message.answer_photo(
        photo=photo_file,
        caption="Стипендия - любимое слово каждого студента. Получают ее 25 числа каджого месяца, а если дата приходится на выходные, то раньше. При неудачной сдаче сессии(у вас есть тройки/двойки или незачёты,задолженности) можете забыть о ней до следующего семестра, если, конечно, вы хорошо закроете сессию. Существует несколько видов стипендий,посмотрим с чем их едят, а также немного про материальную помощь"
    )
    media = [
        # Первое фото с подписью
        InputMediaPhoto(
            media=FSInputFile(img_path('f4.png')),
            caption="Академ стипендия."
        ),
        # Второе фото без подписи
        InputMediaPhoto(
            media=FSInputFile(img_path('f5.png'))
        )
    ]
    # Отправляем группу медиафайлов
    await callback.message.answer_media_group(media=media)
    media = [
        # Первое фото с подписью
        InputMediaPhoto(
            media=FSInputFile(img_path('f6.png')),
            caption="Социальная стипендия."
        ),
        # Второе фото без подписи
        InputMediaPhoto(
            media=FSInputFile(img_path('f7.png'))
        )
    ]
    # Отправляем группу медиафайлов
    await callback.message.answer_media_group(media=media)
    document_file = FSInputFile(file_path('Как оформить социалку.pdf'))
    await callback.message.answer_document(
        document=document_file
    )
    document_file = FSInputFile(file_path('Как_оформить_социалку,_не_выходя_из_комнаты.pdf'))
    await callback.message.answer_document(
        document=document_file
    )
@fact_router.callback_query(F.data == 'fact3')
async def fact1(callback: CallbackQuery):
    photo_file = FSInputFile(img_path('f8.png'))
    await callback.message.answer_photo(
        photo=photo_file,
        caption="Материальная помощь — это единовременная выплата, по различным социальным причинам.\n\nПолучать её могут и бюджетники, и платники, если они состоят в Профсоюзе. Для этого следует лишь собрать документы и принести их в профком (не забудьте профсоюзный билет) не позднее какого-то (20?28?) числа каждого месяца (может быть раньше в связи с праздниками/выходными), сама выплата приходит в следующем месяце.\n\nСписок причин и документов для оформления приведён ниже"
    )
    document_file = FSInputFile(file_path('Причины матпомощи.pdf'))
    await callback.message.answer_document(
        document=document_file
    )
@fact_router.callback_query(F.data == 'fact4')
async def fact1(callback: CallbackQuery):
    photo_file = FSInputFile(img_path('f9.png'))
    await callback.message.answer_photo(
        photo=photo_file,
        caption="Пару слов туда-сюда\n\n1. Да, тараканы есть, в разных количествах и не везде, вам придётся смириться с этим. Главное - убирайтесь и травите их.\n\n2. Никаких электронагревательных приборов. А если честно, то можно всё, главное не спалиться перед проверками. Если стучат в дверь, а вы никого не ждали, прячьте всё.\n\n3. Дружим со студсоветом. Повезёт - вам и комнату поменяют на хорошую, и мебель новую подгонят, и просто вашу жопу прикроют."
    )

@fact_router.callback_query(F.data == 'fact5')
async def fact1(callback: CallbackQuery):
    photo_file = FSInputFile(img_path('f10.png'))
    await callback.message.answer_photo(
        photo=photo_file,
        caption="ИСУ? ШТА?\n\nЗнакомьтесь, это ИСУ — типа местные госуслуги: можно заказать справочки, посмотреть свои оценки, кинуть заявку на общагу и прочие мелочи жизни.\n\nА как получить туда доступ — смотрите ниже:\nhttps://isu.uust.ru/"
    )
    document_file = FSInputFile(file_path('Как получить доступ в ИСУ.pdf'))
    await callback.message.answer_document(
        document=document_file
    )

@fact_router.callback_query(F.data == 'fact6')
async def fact6(callback: CallbackQuery):
    media = [
        # Первое фото с подписью
        InputMediaPhoto(
            media=FSInputFile(img_path('f11.jpg')),
            caption="\nИнформация о медосмотре для студентов \n\n⚠️ <b>ВАЖНО:</b> C сентября по ноябрь будет проходить обязательный медосмотр для всех студентов 1-го курса, необходимый для занятий по физической культуре. Каждый староста должен подойти в медпукт и оставить свои контактыю\n"
        ),
        # Второе фото без подписи
        InputMediaPhoto(
            media=FSInputFile(img_path('f12.jpg'))
        ),
        # Третье фото без подписи
        InputMediaPhoto(
            media=FSInputFile(img_path('f13.jpg'))
        )]
    await callback.message.answer_media_group(media=media)
    await callback.message.answer(    "1. Документы для медосмотра \nВам необходимо подготовить <b>копии</b> следующих документов. Положите их в отдельный файл или скрепите степлером.\n\n* <b>Паспорт:</b> ксерокопия страниц с фотографией и пропиской на одном листе.\n* <b>Медицинский полис ОМС:</b> ксерокопия с обеих сторон на одном листе.\n* <b>СНИЛС:</b> ксерокопия.\n* <b>ИНН:</b> ксерокопия.\n* <b>Справка 086/у</b> (если есть) или результаты флюорографии за последний год. Если их нет, флюорографию сделают во время медкомиссии.\n* <b>Сертификат о прививках:</b>\n    * Дифтерия-столбняк (АДСм, последняя прививка в 14 лет).\n    * Корь (2 записи).\n    * Паротит (2 записи).\n    * Краснуха (2 записи).\n    * Гепатит В (3 записи).\n    * *Примечание: Вся эта информация обычно содержится в справке 086/у или в сертификате профилактических прививок.*\n* <b>Справка об инвалидности</b> (если есть).\n")
    await callback.message.answer("\n2. Информация о прикреплении к поликлинике \n\nВсе студенты автоматически прикрепляются к <b>ГКБ №5 ПО-№3</b> по адресу: <b>ул. Цюрупы, 4</b>.\n\n* <b>Если вы не хотите прикрепляться к этой поликлинике</b>, вам необходимо лично сообщить об этом в учебную часть или деканат.\n* <b>Для иногородних студентов (не из Уфы и Башкортостана):</b> Вам нужно самостоятельно прийти в поликлинику ГКБ №5 ПО-№3 по адресу: ул. Цюрупы, 4, чтобы оформить полис ОМС вашего региона и прикрепиться. Это нужно сделать до начала медкомиссии.\n* <b>Для всех студентов:</b> Вы можете самостоятельно прикрепиться к поликлинике для получения медицинской помощи, не дожидаясь медосмотра.\n")

@fact_router.callback_query(F.data == 'fact7')
async def fact7(callback: CallbackQuery):
    await callback.message.answer("\nЕсли вы пропустили занятия по болезни, вам нужна <b>справка о нетрудоспособности (095/у)</b>. Её можно получить в поликлинике, к которой вы прикреплены. Учитывайте, что справка оформляется только с даты обращения к врачу или вызова скорой помощи. Если вы были на приёме у врача, попросите справку о том, что вы посещали врача, чтобы закрыть прогул.\n")


@fact_router.callback_query(F.data == 'fact8')
async def fact8(callback: CallbackQuery):
    await callback.message.answer("<b>Психологическая помощь в университете</b>\n\nЕсли психологическое состояние мешает учёбе, нужна справка. Отсутствие на парах по этой причине должно быть подтверждено, как и при болезни.\n\nВ университете есть психологическая служба, где можно получить помощь. Каждому студенту доступно <b>пять бесплатных консультаций</b> за семестр. Обратиться за помощью — это нормально и важно.\n\nТакже регулярно проводятся <b>психологические тесты</b>. Отвечайте на них честно, чтобы получить точную оценку своего состояния и нужную поддержку.\n")
