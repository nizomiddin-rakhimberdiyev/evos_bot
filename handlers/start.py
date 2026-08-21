from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from keyboards.reply import menu_button,region_button
from state.product import ProductState

from database.crud import add_product, get_all_products
from aiogram.fsm.context import FSMContext

router = Router()

@router.message(CommandStart())
async def start_command(message: Message):
    user = message.from_user
    await message.answer(f"Salom {user.full_name} !",reply_markup=menu_button)


@router.message(F.text == "🏢 Kompaniya haqida")
async def about_company(message:Message):
    text = """EVOS ® tez xizmat ko'rsatish restoranlari tarmog'i bir joyda turmaydi, siz uchun va siz bilan doimo o'sib boradi va rivojlanadi! Biz geografiyamizni kengaytiramiz va deyarli har oyda yangi filiallarni ochamiz.
    Endi bizning tarmog'imizning O'zbekiston bo'ylab 50 dan ortiq filiali mavjud. Biz doimo jamoamizning bir qismi bo'lishni xohlaydigan va EVOS ® da o'z faoliyatini boshlashga tayyor bo'lgan dinamik va faol odamlarni qidiramiz.
    EVOS ® –  bu ishonchli brenddir. EVOS ® da ishlash – barqaror daromad va martaba istiqbollari kafolati.
    EVOS ® da o'z karyerangizni boshlang!"""
    
    image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTFNq1mK44g9pOpXzTAn3dEyiydMCfmPHIrU8jUdu8fDg&s=10"

    await message.answer_photo(photo=image_url,caption=text)


@router.message(F.text == "📞 Kontaktlar/Manzil")
async def contact_company(message:Message):
    text = """Manzil: Furqat ko'chasi 175, kirish 1, 
2-qavat.
Mo'ljal: MAKRO THE TOWER

Kontakt: +998 71 203 12 12"""
    
    image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTFNq1mK44g9pOpXzTAn3dEyiydMCfmPHIrU8jUdu8fDg&s=10"


    await message.answer_photo(photo=image_url,caption=text)
    await message.answer_location(latitude=41.302196,longitude=69.248867)



@router.message(F.text == "🗣 Yangiliklar")
async def news_company(message:Message):
    text = """🍔 EVOS Tarmog'idagi Eng So'nggi Yangiliklar

    20 yillik yubiley va 'Yulduzli kombolar':
    EVOS o'zining 20 yilligiga bag'ishlab xonanda Tohir Sodiqov va bloger Khusnorik bilan hamkorlikda maxsus bayramona kombo taomlarini sotuvga chiqardi.

    20% chegirma aksiyasi:
    Restoranlardagi maxsus bayramona foto zonalarda kreativ rasmga tushib, uni EVOS Uzbekistan Instagram sahifasini belgilagan holda Stories'ga joylagan mijozlarga 20% li unikal promokod berilmoqda.

    Yangi 'Macho Lavash':
    Menyuda yangi va o'zgacha ta'mga ega bo'lgan Macho Lavash hamda yangilangan Lunch Box mahsulotlari sotuvga chiqdi.

    Filiallar kengayishi:
    Tarmqning O'zbekiston bo'ylab restoranlari soni 80 taga yetdi va yangi filiallar ochilishi davom etmoqda."""

    image_url = "https://www.afisha.uz/uploads/media/2025/06/6c165a72b92448f3f2a2cd559408402d_l.webp"

    video_url = "https://youtu.be/e5yudn51UMY?si=W7KQk4_hmYm11hnF"
    await message.answer_photo(photo=image_url,caption=text)

    await message.answer(text=f"{video_url}")




@router.message(F.text=="💼 Bo'sh ish o'rinlari")
async def vacancy_company(message:Message):
    await message.answer(text="EVOS jamoasiga qo'shiling!")
    await message.answer(text="📍 Shaharni tanlang.",reply_markup=region_button)

@router.message(F.text.in_(["Toshkent", "Qoqon", "Namangan","Toshkent viloyati","Nukus","Samarqand","Shahrisabz","Navoiy"]) )
async def send_vacancy_company(message:Message):
    text = (
        "💚 Biz izlayotgan nomzod:\n\n"
        "O‘zbekcha va ruscha erkin gaplasha oladi — mehmonlar bilan ikki tilda muloqot muammo emas;\n\n"
        "🕔 Ish vaqtiga moslashuvchan yondashuv — qayerda kerak bo‘lsangiz, o‘sha yerda bo‘lasiz;\n\n"
        "O‘z ustida ishlashni va jamoa bilan birga yuksalishni xohlaydi — ambitsiya zo‘r bo‘lsa, yo‘l ham topiladi!\n\n"
        "💚 Biz taklif qilamiz:\n\n"
        "Ishonchli ish joyi va barqaror daromad: soatiga 18 434,99 so‘m (12% soliq ushlanadi);\n\n"
        "Rivojlanish uchun imkoniyatlar: o‘qish, tajriba va lavozim ko‘tarilishi;\n\n"
        "Do‘stona jamoa va har tomonlama qo‘llab-quvvatlash.\n\n"
        "Keling, kuchlarni birlashtiramiz — kelajagingiz bu yerdan boshlanishi mumkin! 💚🚀\n\n"
        f"Manzil:{message.text}"
    )
    image_url = "https://data.daryo.uz/media/2023/17.022023/23.02/photo_2023-03-01_15-31-56.jpg"

    await message.answer_photo(photo=image_url,caption=text)





@router.message(F.text=="Mahsulot Qoshish")
async def start_add_product(message:Message,state:FSMContext):
    await state.set_state(ProductState.name)
    await message.answer("Mahsulot nomini kiriting:")


@router.message(ProductState.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(ProductState.description)
    await message.answer("Mahsulot tavsifini kiriting:")


@router.message(ProductState.description)
async def get_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await state.set_state(ProductState.price)
    await message.answer("Mahsulot narxini kiriting:")



@router.message(ProductState.price)
async def get_price(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    await state.set_state(ProductState.address)
    await message.answer("Mahsulot manzilini kiriting:")



@router.message(ProductState.address)
async def get_address(message: Message, state: FSMContext):
    await state.update_data(address=message.text)
    await state.set_state(ProductState.image)
    await message.answer("Mahsulot rasmini yuboring:")



@router.message(ProductState.image, F.photo)
async def get_image(message: Message, state: FSMContext):
    data = await state.get_data()
    image_id = message.photo[-1].file_id

    add_product(
        name=data["name"],
        description=data["description"],
        price=data["price"],
        address=data["address"],
        image_id=image_id,
    )

    await state.clear()
    await message.answer(
        "Mahsulot muvaffaqiyatli saqlandi!", reply_markup=menu_button
    )


@router.message(F.text == "Menu")
async def show_menu(message: Message):
    products = get_all_products()

    if not products:
        await message.answer("Hozircha mahsulotlar yo'q.")
        return

    for product in products:
        name, description, price, address, image_id = product
        text = f"Nomi: {name}\nTavsifi: {description}\nNarxi: {price}\nManzil: {address}"
        await message.answer_photo(photo=image_id, caption=text)
    
   

    









