from aiogram.types  import ReplyKeyboardMarkup,KeyboardButton


menu_button = ReplyKeyboardMarkup(
    
    keyboard=[
        [
            KeyboardButton(text="🏢 Kompaniya haqida")
        ],
        [
            KeyboardButton(text="💼 Bo'sh ish o'rinlari")
        ],
        [
            KeyboardButton(text="Mahsulot Qoshish"),
            KeyboardButton(text="Menu")
        ],
        [
            KeyboardButton(text="🗣 Yangiliklar"),
            KeyboardButton(text="📞 Kontaktlar/Manzil"),
            KeyboardButton(text="🇺🇿/🇷🇺 Til")
        ]

    ],
    resize_keyboard=True
    
    
)

region_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Toshkent"),
            KeyboardButton(text="Qoqon")
        ],
        [
            KeyboardButton(text="Namangan"),
            KeyboardButton(text="Toshkent viloyati")
        ],
        [
            KeyboardButton(text="Nukus"),
            KeyboardButton(text="Samarqand"),
        ],
        [
            KeyboardButton(text="Shahrisabz"),
            KeyboardButton(text="Navoiy")
        ]

    ],
    resize_keyboard=True

)


