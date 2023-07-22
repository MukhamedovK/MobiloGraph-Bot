import logging

from aiogram import Dispatcher, Bot, executor
from aiogram.types import *
from keyboard import start_btn, start_btn1, reply_btn, video_lessons, idea, android, master_class, interview, videomontaj, vacanse, trend_musics, fikr_bildirish


logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "6251779786:AAG3lZJXf7u2-r7rBOW29ZhSiCbEL7ZF3zw"

bot = Bot(token=BOT_TOKEN, parse_mode='html')
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: Message): 
    btn = await start_btn()
    btn1 = await start_btn1()
    await message.answer(f"Assalomu alaykum {message.from_user.first_name}\n\n"
                        "**Sizni botimizda ko'rganimizdan xursandmiz😊\n\n"
                        "**📲 Botdan Mobilografiyaga oid barcha ma'lumotlarni olishingiz mumkin", reply_markup=btn)
    await message.answer("Botdan foydalanish uchun\n\n"
                        "👉 @shk_uz\n"
                        "👉 @dasturlash_hayoti\n\n"
                        "kanallariga obuna bo'ling va tekshirish tugmasini bosing.", reply_markup=btn1)
    

@dp.callback_query_handler(text='check')
async def check_btn(call: CallbackQuery):
    btn = await reply_btn()
    btn1 = await start_btn()
    
    await call.message.answer(f"Assalomu alaykum {call.from_user.first_name}\n\n"
                        "**Sizni botimizda ko'rganimizdan xursandmiz😊\n\n"
                        "**📲 Botdan Mobilografiyaga oid barcha ma'lumotlarni olishingiz mumkin", reply_markup=btn1)
    
    await call.message.answer("<b>Marhamat, kerakli bo'limni tanlang: ⤵️</b>", reply_markup=btn)


@dp.message_handler()
async def text_handler(message: Message):
    text = message.text
    if text == "Foydali loyihalar ✅":
        await message.answer("@Dasturlash_hayoti — Dasturlashga oid qiziqarli ma'lumotlar, memlar\n\n"
                            "@Kompyuterdasturlari_uz — Kompyuteringiz uchun kerakli dasturlarni yuklab olishingiz mumkin\n\n"

                            "@it_ishkal — Kompyuter va OS'da vujudga kelgan muammolarni yechishingiz mumkin.\n\n"
                            "@newlink_uz — Eng foydali va noyob linklar kanali\n\n"

                            "@Universal_IT — IT ga oid darslar, kerakli ma'lumotlar va oxirgi yangiliklarni kuzatib borishingiz mumkin\n\n"
                            "@Mantiqiy_Savol_Boshqotirmalar_uz — Eng katta va Eng aktiv Boshqotirmalar kanali\n\n"

                            "@FoydaliUniversal_bot – IT ga oid bepul videodarslar va foydali ma'lumotlarni ulashuvchi universal bot\n\n"
                            "@itsoftwareuz — Kompyuteringiz uchun kerakli eng so'ngi dasturlar, IT memlar, va IT ga doir qiziqarli testlar berib boriladigan loyiha\n\n"

                            "@shk_uz — Kompyuter olamining siz bilgan va bilmagan sirlari jamlangan Telegramdagi eng top kanal\n\n"
                            "@ilovazor — Bu kanalda ish, oʻqish va shaxsiy hayotingizni birmuncha yengillashtirish va zavqlanish imkonini beruvchi ilova, bot va linklar berib boriladi!\n\n"

                            "@KiberxavfsizlikBot — Internet bilan ishlashda o'zimiz va shaxsiy ma'lumotlarimizni asrashni o'rganamiz!\n\n"
                            "@MobilographBot — Botdan Mobilografiyaga oid barcha ma'lumotlarni topishingiz mumkin\n\n"

                            "👆Bu ro'yxatdagilar hali boshlanishi. Oldimizda siz obunachilarga foydasi tegadigan ko'p loyihalar qilish rejada bor.\n\n" 
                            "<b>Bizdan uzoqlashmang!</b>")
        
    elif text == "Boshlang'ich tushuncha":
        album = MediaGroup()
        video = InputFile("1.mp4")
        album.attach_video(video=video, caption=("<b>📹 MOBILOGRAPHY NIMA?</b> \n\n"
                                                "- Video davomida Mobilografiya haqida boshlang'ich tushuncha ega bo'lasiz.\n\n"
                                                "<i>Ko'rib bo'lgach keyingi bo'limga o'ting ⤵️</i>\n\n"
                                                "👉 @MobilographBot"))

        await message.answer_media_group(media=album)
        await message.answer("©Video muallifi: Ustoz Kamol digital")

    elif text == "Video darslar":
        btn = await video_lessons()
        await message.answer("<b>🎥 Video darslar 2 ta bo'limni o'z ichiga oladi:</b>\n\n"
                            "1. Nazariy \n"
                            "2. Amaliy \n\n" 
                            "Birinchi bo'limda telefonda to'gri videoga olishni o'rganasiz. 2- bo'limda esa, o'rganganlaringiz asosida tajribaviy videolarni tomosha qilasiz. \n\n"
                            "<b>Marhamat, kerakli bo'limni tanlang ⤵️</b>", reply_markup=btn)

    elif text == "💡 G'oya/idea":
        btn = await idea()
        await message.answer("<b>Ushbu bo'limda turli rukndagi videolar uchun tayyor g'oyalar bilan tanishasiz. </b>\n\n"
                            "Hozirda mavjud: \n"
                            "- Avtomobilni tasvirga olish uchun g'oyalar; \n"
                            "- Manzarani tasvirga olish uchun video g'oyalar. \n\n"
                            "<b>O'zingizga kerakli bo'limni tanlang ⤵️</b>", reply_markup=btn)
        
    elif text == "Android uchun montaj dastur":
        btn = await android()
        await message.answer("Android uchun montaj dastur", reply_markup=btn)

    elif text == "Master class":
        btn = await master_class()
        await message.answer("<b>Mobilograf Drexlee tomonidan suratga olingan professional kadrlar! </b>\n\n"
                            "Marhamat, kerakli bo'limni tanlang ⤵️", reply_markup=btn)
        
    elif text == "Intervyu":
        btn = await interview()
        await message.answer("Ushbu bo'limda video sohasiga oid bo'lgan qiziq suhbatlarni o'zbek tilida tomosha qilasiz. \n\n"
                            "<b>Marhamat, intervyu raqami ustiga bosing ⤵️</b>", reply_markup=btn)
        
    elif text == "Videomontaj uchun musiqa":
        btn = await videomontaj()
        await message.answer("Ushbu bo'limda, videomontaj jarayonida foydalanishingiz mumkin bo'lgan musiqalar mavjud \n\n"
                            "<b>Tasodifiy musiqa tugmasini bosing ⤵️</b>", reply_markup=btn)
        
    elif text == "After effect darsi":
        album1 = MediaGroup()
        video1 = InputFile("2.mp4")
        album2 = MediaGroup()
        video2 = InputFile("3.mp4")

        album1.attach_video(video=video1, caption=("<b>After effect dasturida animatsiya tayyorlash bo'yicha bepul kurs. </b>\n\n"
                                                    "⏳ Davomiyligi: 3:36:02 \n"
                                                    "⚖️ Hajmi: 347.3 MB \n\n"
                                                    "Noldan professionalgacha bilishingiz kerak bo'lgan ma'lumotlarni o'rganib olasiz. \n\n"
                                                    "* Video ingliz tilida! \n\n"
                                                    "© 👤 Envato Tuts+ \n\n"
                                                    "👉 @Mobilographbot"))
        await message.answer_media_group(media=album1)

        album2.attach_video(video=video2, caption=("<b>📹 Motion graphics. 32- dars. Amaliyot darsi (1-qism) </b>\n\n"
                                                    "©Milliy_talim_resurslari → (http://www.youtube.com/@milliy_talim_resurslar) \n\n"
                                                    "👉 @MobilographBot"))
        await message.answer_media_group(media=album2)

        await message.answer("After effect dasturida qanday qilib montaj qilish mumkinligi haqida bilib olasiz. Noldan professionalgacha. \n\n"
                            "* Video ingliz tilida bo'ladi.")
        

    elif text == "Vakansiyalar":
        btn = await vacanse()
        await message.answer("<b>⚡️Bu boʼlimda siz mobilografiyani oʼrganib, ish qidirib ishlashingiz mumkin. </b>\n\n"
                            "<b>Marhamat, kerakli bo'limni tanlang: ⤵️</b>", reply_markup=btn)
        
    elif text == "Trenddagi musiqalar":
        btn = await trend_musics()
        await message.answer("<b>⬇️Bu bo'lim orqali siz instagram, tik tok, you tube dagi trendga chiqqan musiqalarni yuklab olishingiz mumkin. </b>\n\n"
                            "<b>Marhamat, kerakli bo'limni tanlang: ⤵️</b>", reply_markup=btn)
        
    elif text == "🗯️ Fikr bildirish":
        btn = await fikr_bildirish()
        await message.answer("Taklif va murojaatlaringizni qoldirishingiz mumkin!", reply_markup=btn)

    elif text == "🔙 Orqaga":
        btn = await reply_btn()
        await message.answer("<b>Marhamat, kerakli bo'limni tanlang: ⤵️</b>", reply_markup=btn)

    elif text == "🔝 Asosiy Menyu":
        btn = await reply_btn()
        await message.answer("<b>Marhamat, kerakli bo'limni tanlang: ⤵️</b>", reply_markup=btn)

    elif text == "🚫 Bekor qilish":
        btn = await reply_btn()
        await message.answer("<b>Marhamat, kerakli bo'limni tanlang: ⤵️</b>", reply_markup=btn)


    
        
        





if __name__ == "__main__":
    executor.start_polling(dp)