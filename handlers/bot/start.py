# ππππ ππππ ππππ πππππ πππππππππ @SHAILENDRA34 | 
# ππππ« πππ«π¨ π©π©π₯π¬ ππ₯π’π¬π‘ ππ¨π§'π­ π«ππ¦π¨π―π π­π‘π’π¬ π₯π’π§π ππ«π¨π¦ π‘ππ«π π


from helpers.filters import command
from pyrogram import Client as bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import (BOT_NAME, SUPPORT_GROUP, OWNER_USERNAME, BOT_USERNAME)


@bot.on_message(filters.command("start"))
def start_(bot, message):
    
    START_TEXT = """**β­ Merhaba {}\n\nβ«οΈBen {} \n\nβ«οΈBasit bir mΓΌzik botuyum .\n\nβ«οΈBeni Grubunuza ekleyip yΓΆnetici yapΔ±n ve mΓΌziΔin keyfini Γ§Δ±karΔ±n !**"""

    START_BUTTON = [
                [
                    InlineKeyboardButton(text="π Beni Gruba Ekleyin π", url=f"http://t.me/{BOT_USERNAME}?startgroup=true"),
                ],
                [
                    InlineKeyboardButton(text="π Destek ", url=f"https://t.me/tMertTt"),
                    InlineKeyboardButton(text="πΉπ· Kanal ", url="https://t.me/sohbetmuhabbetw"),
                ],                
                [                    
                    InlineKeyboardButton(text="π TΓΌm Komutlar ", url="https://t.me/ProTubeSupport/2"),
                ],
                
            ]
    message.reply_text(
        START_TEXT.format(message.from_user.mention, BOT_NAME, SUPPORT_GROUP),
        reply_markup=InlineKeyboardMarkup(START_BUTTON)
    )
    message.delete()

@bot.on_message(filters.command("hsusueue"))
def help_(bot, message):
    HELP_TXT = """Merhaba {}\niΕte yardΔ±m menΓΌsΓΌ \nGrubuna ekleyerek mΓΌzik keyfine baΕlayabilirsiniz @{} sorununuz nedir? π«"""
    
    HELP_BUTTON = [
        [
            InlineKeyboardButton(text="πΉοΈ Temel komutlar", callback_data="basic_"),
            InlineKeyboardButton(text="πΉοΈ Admin komutlar", callback_data="admin_cmd"),
        ],
        [
            InlineKeyboardButton(text="π Kapat", callback_data="close_"),
            InlineKeyboardButton(text="β¬οΈ Geri", callback_data="HOME"),
        ],
    ]
    message.reply_text(
        HELP_TXT.format(message.from_user.first_name, SUPPORT_GROUP),
        reply_markup=InlineKeyboardMarkup(HELP_BUTTON)
    )
    message.delete()

@bot.on_callback_query()
def callback_query(Client, callback: CallbackQuery):
    if callback.data == "help_":
    
        HELP_TXT = f"""Merhaba iΕte yardΔ±m menΓΌsΓΌ istediΔiniz seΓ§eneΔinizi seΓ§in ve keΕfedin \nHer tΓΌrlΓΌ yardΔ±m veya sorun iΓ§in katΔ±lΔ±n @{SUPPORT_GROUP} Sorununuz nedir π«?"""
    
        HELP_BUTTON = [
            [
                InlineKeyboardButton(text="πΉοΈ Temel komutlar", callback_data="bcd"),
                InlineKeyboardButton(text="πΉοΈ Admin komutlar", callback_data="admin"),
            ],
            [
                InlineKeyboardButton(text="π Kapat", callback_data="close_"),
                InlineKeyboardButton(text="β¬οΈ Geri", callback_data="HOME"),
            ],
        ]
        callback.edit_message_text(
            HELP_TXT,
            reply_markup=InlineKeyboardMarkup(HELP_BUTTON)
        )
    elif callback.data == "HOME":
 
        START_TEXT = f"""Merhaba, ben {BOT_NAME} \nBasit ve gecikmesiz bir bottur\nHerhangi bir sorun olduΔunda katΔ±lΔ±n π @{SUPPORT_GROUP}\nya da help butonuna basΔ±nΔ±z  /help """
        START_BUTTON = [
                [
                    InlineKeyboardButton(text="Kanal π«", url=f"https://t.me/sohbetmuhabbetw"),
                    InlineKeyboardButton(text="Beni gruba ekle β", url=f"http://t.me/{BOT_USERNAME}?startgroup=true"),
                ],
                [
                    InlineKeyboardButton(text="Sahibim β­", url=f"https://t.me/{OWNER_USERNAME}"),
                    InlineKeyboardButton(text="Sohbet Grubu β¨", url="https://t.me/sohbetmuhabbetw"),
                ],                
                [                    
                    InlineKeyboardButton(text="Komutlar πΉοΈ", callback_data="help_"),
                ],
                
            ]
        
        callback.edit_message_text(
            START_TEXT,
            reply_markup=InlineKeyboardMarkup(START_BUTTON)
        )
    elif callback.data == "bcd":
        B_HELP = """
`Κα΄sΙͺα΄ α΄α΄α΄α΄α΄Ι΄α΄s :- `

/oynat (Sorgu, yt linki, ses dosyasΔ± ) - bu komutu kullanΔ±n ve mΓΌziΔin keyfine bakΔ±n 
/ytp (sorgu) - Daha geliΕmiΕ muzik aramak iΓ§in kullanΔ±n 
/bul (Sorgu) - Bu komutla sevdiginiz ΕarkΔ±larΔ± indirebilirsiniz 
/ara (sorgu) - YouTube de arama yapar 
"""
        BUTTON = [
            [
                InlineKeyboardButton(text="π Kapat", callback_data="close_"),
                InlineKeyboardButton(text="β¬οΈ Geri", callback_data="help_"),
            ],
        ]
        callback.edit_message_text(
            B_HELP,
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )
    elif callback.data == "admin":
        A_HELP = """
`Admin komutlar :-`

/durdur - Γalan mΓΌziΔi durdurur
/devam - duran mΓΌziΔi devam ettirir
/atla - sΔ±radaki ΕarkΔ±ya geΓ§er 
/son - ΕarkΔ±yΔ± sonlandΔ±rΔ±r
/katil - asistanΔ± gruba ekler


`Sudo komutlar :-`

/rmf - DosyayΔ± veri tabanΔ±ndan temizler 
/rmw - Veri tabanΔ±nΔ±ndan ham dosyalarΔ± temizler
/clean - DosyalarΔ± sunucudan temizler
/gcast - kΓΌresel mesaj yayΔ±nlamak iΓ§in 
"""
        BUTTON = [
            [
                InlineKeyboardButton(text="π kapat", callback_data="close_"),
                InlineKeyboardButton(text="β¬οΈ Geri", callback_data="help_"),
            ],
        ]
        callback.edit_message_text(
            A_HELP,
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )
    elif callback.data == "close_":
        callback.message.delete()
