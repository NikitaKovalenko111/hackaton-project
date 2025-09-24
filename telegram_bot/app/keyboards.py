from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Профком"),KeyboardButton(text="Cтуденческие объединения")],
                                     [KeyboardButton(text="Карта"),KeyboardButton(text="Навигатор")],
                                    [KeyboardButton(text="Рассписание пар"),KeyboardButton(text="Фактики")]
                                     ],
                           resize_keyboard=True,
                           input_field_placeholder="Выберите интересующий вопрос?")

circle = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Хореографический коллектив", callback_data="hor")],
                                               [InlineKeyboardButton(text="Вокально-инструментальный коллектив", callback_data="vocal")],
                                                [InlineKeyboardButton(text="Клуб по интересам", callback_data="cl_interes")],
                                               [InlineKeyboardButton(text="Театральный коллектив", callback_data="teatr")],
                                               [InlineKeyboardButton(text="Спорт, экология, туризм",callback_data="sport")],
                                               ])
hoes = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Ансамбль народного танца «Йешлек»", callback_data="hor1")],
                                               [InlineKeyboardButton(text="Ансамбль спортивного бального танца «Аллегро»", callback_data="hor2")],
                                                [InlineKeyboardButton(text="Заслуженный коллектив народного творчества РБ Народный ансамбль танца «Ирандек»", callback_data="hor3")],
                                               [InlineKeyboardButton(text="Народный ансамбль народного танца «Айтуган»", callback_data="hor4")],
                                               [InlineKeyboardButton(text="Народный танцевальный проект «Атмосфера»",callback_data="hor5")],
                                               [InlineKeyboardButton(text="Первая сборная УУНиТ по черлидингу",callback_data="hor6")],
                                               [InlineKeyboardButton(text="Студия танца «Dance vibe»",callback_data="hor7")],
                                               [InlineKeyboardButton(text="Танцевальный коллектив «Watermelons CREW»",callback_data="hor8")]])
vocals = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Вокальная студия «Септима»", callback_data="vocal1")],
                                               [InlineKeyboardButton(text="Кавер-группа «Моментов море»", callback_data="vocal2")],
                                                [InlineKeyboardButton(text="Народный ансамбль кураистов «Актамыр»", callback_data="vocal3")],
                                               [InlineKeyboardButton(text="Народный русский фольклорный ансамбль «Таусень»", callback_data="vocal4")],
                                               [InlineKeyboardButton(text="Этно-фолк группа «Янгузель»",callback_data="vocal5")],
])
teatrs = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Башкирский народный студенческий театр «Оскон» («Искра»)", callback_data="teatr1")],
                                               [InlineKeyboardButton(text="Русский студенческий театр «Гротеск»", callback_data="teatr2")],
                                                [InlineKeyboardButton(text="Татарский музыкально-поэтический театр «Сэлэт» («Талант»)", callback_data="teatr3")],
])
sports = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Зеленый проект", callback_data="sport1")],
                                               [InlineKeyboardButton(text="Туристический клуб \"Восхождение\"", callback_data="sport2")],
                                                [InlineKeyboardButton(text="Туристический клуб «Икар»", callback_data="sport3")],
                                               [InlineKeyboardButton(text="Экологический клуб «EcoBirds»", callback_data="sport4")],
])

cl_interes = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Аниме клуб «Аматэрасу»", callback_data="cl_interes1")],
                                               [InlineKeyboardButton(text="Интеллектуальный клуб УУНиТ", callback_data="cl_interes2")],
                                                [InlineKeyboardButton(text="Клуб дебатов «Достоевский»", callback_data="cl_interes3")],
                                               [InlineKeyboardButton(text="Клуб изобразительного искусства УУНиТ", callback_data="cl_interes4")],
                                               [InlineKeyboardButton(text="Клуб любителей быстрых игр на реакцию и ритм",callback_data="cl_interes5")],
                                               [InlineKeyboardButton(text="Клуб разработчиков игр Brain Bricks",callback_data="cl_interes6")],
                                               [InlineKeyboardButton(text="Комитет инициативных студентов",callback_data="cl_interes7")],
                                               [InlineKeyboardButton(text="Лига КВН УУНиТ",callback_data="cl_interes8")],
                                                [InlineKeyboardButton(text="Математический клуб УУНиТ", callback_data="cl_interes9")],
                                               [InlineKeyboardButton(text="Настольный клуб «Final Round»", callback_data="cl_interes10")],
                                                [InlineKeyboardButton(text="Поисковый отряд \"Ватан\" УУНиТ", callback_data="cl_interes11")],
                                               [InlineKeyboardButton(text="Промо-группа \"ЛАЙВ\"", callback_data="cl_interes12")],
                                               [InlineKeyboardButton(text="Студенческий бизнес-клуб УУНиТ «STUDBISS»",callback_data="cl_interes13")],
                                               [InlineKeyboardButton(text="Студенческий патриотический клуб «Авангард»",callback_data="cl_interes14")],
                                               [InlineKeyboardButton(text="Школа-студия «Титул»",callback_data="cl_interes15")],
                                               ])
tuc = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Комиссии профкома студентов", callback_data="kom")],
                                               [InlineKeyboardButton(text="Образовательные проекты", callback_data="obr")],
                                                [InlineKeyboardButton(text="Возможности профсоюза", callback_data="vosm")],
                                               ])
kom = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Социально-правовая", callback_data="kom1")],
                                               [InlineKeyboardButton(text="Научно-учебная", callback_data="kom2")],
                                                [InlineKeyboardButton(text="Культурно-массовая", callback_data="kom3")],
                                               [InlineKeyboardButton(text="Спортивная", callback_data="kom4")],
                                               [InlineKeyboardButton(text="По работе с иностранными студентами",callback_data="kom5")],
                                               [InlineKeyboardButton(text="Информационная",callback_data="kom6")],
                                               [InlineKeyboardButton(text="Жилищно-бытовая",callback_data="kom7")],
                                               ])
obr = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Проект «Активация»", callback_data="obr1")],
                                               [InlineKeyboardButton(text="ПавLOVEка", callback_data="obr2")],
                                           ])
vosm = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Тьюторское движение", callback_data="vosm1")],
                                               [InlineKeyboardButton(text="СКС РФ", callback_data="vosm2")],
                                           ])

facts = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Учёба", callback_data="fact1")],
                                               [InlineKeyboardButton(text="Стипендия", callback_data="fact2")],
                                                [InlineKeyboardButton(text="Материальная помощь", callback_data="fact3")],
                                               [InlineKeyboardButton(text="Жизнь в Общаге", callback_data="fact4")],
                                               [InlineKeyboardButton(text="ИСУ",callback_data="fact5")],
                                               [InlineKeyboardButton(text="Медкомссия для физ-ры",callback_data="fact6")],
                                               [InlineKeyboardButton(text="Я болен, что делать?",callback_data="fact7")],
                                               [InlineKeyboardButton(text="Я в депрессии, что делать?",callback_data="fact8")],
                                                [InlineKeyboardButton(text="", callback_data="fact9")],
                                               [InlineKeyboardButton(text="", callback_data="fact10")],
                                                [InlineKeyboardButton(text="", callback_data="fact11")],
                                               [InlineKeyboardButton(text="", callback_data="fact12")],
                                               [InlineKeyboardButton(text="",callback_data="fact13")],
                                               [InlineKeyboardButton(text="",callback_data="fact14")],
                                               [InlineKeyboardButton(text="",callback_data="fact15")],
                                               ])
