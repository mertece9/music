# ππππ ππππ ππππ πππππ πππππππππ @SHAILENDRA34 | 
# ππππ« πππ«π¨ π©π©π₯π¬ ππ₯π’π¬π‘ ππ¨π§'π­ π«ππ¦π¨π―π π­π‘π’π¬ π₯π’π§π ππ«π¨π¦ π‘ππ«π π


import os
from pyrogram import Client, filters
from pyrogram.types import Message
from helpers.filters import command, other_filters
from helpers.decorators import sudo_users_only, errors
from helpers.command import commandpro

downloads = os.path.realpath("downloads")
raw_files = os.path.realpath("raw_files")

@Client.on_message(command("rmf") & ~filters.edited)
@errors
@sudo_users_only
async def clear_downloads(_, message: Message):
    ls_dir = os.listdir(downloads)
    if ls_dir:
        for file in os.listdir(downloads):
            os.remove(os.path.join(downloads, file))
        await message.reply_text("`ποΈΔ°ndirilen tΓΌm dosyalar kaldΔ±rΔ±ldΔ± `")
    else:
        await message.reply_text("`Temizlenecek dosya bulundu`")

        
@Client.on_message(command("rmw") & ~filters.edited)
@errors
@sudo_users_only
async def clear_raw(_, message: Message):
    ls_dir = os.listdir(raw_files)
    if ls_dir:
        for file in os.listdir(raw_files):
            os.remove(os.path.join(raw_files, file))
        await message.reply_text("`temizlik ayarlanΔ±yor ποΈ`")
    else:
        await message.reply_text("`Dosyalar hazΔ±r`")


@Client.on_message(commandpro(["/clean"]) & ~filters.edited)
@errors
@sudo_users_only
async def cleanup(_, message: Message):
    pth = os.path.realpath(".")
    ls_dir = os.listdir(pth)
    if ls_dir:
        for dta in os.listdir(pth):
            os.system("rm -rf *.webm *.jpg")
        await message.reply_text("`β α΄Κα΄α΄Ι΄α΄α΄`")
    else:
        await message.reply_text("`β Temizlik baΕarΔ±lΔ±`")
