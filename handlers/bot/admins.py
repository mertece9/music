# ππππ ππππ ππππ πππππ πππππππππ @SHAILENDRA34 |
# ππππ« πππ«π¨ π©π©π₯π¬ ππ₯π’π¬π‘ ππ¨π§'π­ π«ππ¦π¨π―π π­π‘π’π¬ π₯π’π§π ππ«π¨π¦ π‘ππ«π π


from asyncio.queues import QueueEmpty
from config import que
from pyrogram import Client, filters
from pyrogram.types import Message
from cache.admins import set
from helpers.decorators import authorized_users_only, errors
from helpers.channelmusic import get_chat_id
from helpers.command import commandpro
from helpers.filters import other_filters
from callsmusic import callsmusic, queues
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream import InputStream
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, KeyboardButton,
                            ReplyKeyboardMarkup, ReplyKeyboardRemove)


PAUSED = "https://telegra.ph/file/e1baf2c6dde1534acb45f.jpg"
RESUMED = "https://telegra.ph/file/6d861ec0c75efe088d043.jpg"
SKIPPED = "https://telegra.ph/file/ec4cb3823e85bd9bb6022.jpg"
END = "https://telegra.ph/file/30525f90e119bf95d9d80.jpg"

BUTTON = [
    [
        InlineKeyboardButton(text="π Destek", url=f"https://t.me/sohbetmuhabbetw"),
        InlineKeyboardButton(text="πKanal", url=f"https://t.me/sohbetmuhabbetw"), 
    ],
]

ACTV_CALLS = []

@Client.on_message(commandpro(["/pause", "/durdur", "/pause{BOT_USERNAME}", "/durdur{BOT_USERNAME}"]) & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    await callsmusic.pytgcalls.pause_stream(message.chat.id)
    
    await message.reply_photo(
        photo=PAUSED,
        caption=f"MΓΌzik durduruldu !\n\nβ¦ /devam :- mΓΌziΔi devam ettir",
        reply_markup=InlineKeyboardMarkup(BUTTON)
    )
    await message.delete()


@Client.on_message(commandpro(["/resume", "/devam", "/resume{BOT_USERNAME}", "/devam{BOT_USERNAME}"]) & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    await callsmusic.pytgcalls.resume_stream(message.chat.id)
    
    await message.reply_photo(
        photo=RESUMED,
        caption=f"mΓΌzik devam ediyor !.\n\nβ¦ /durdur :- ΕarkΔ±yΔ± duraklat!!",
        reply_markup=InlineKeyboardMarkup(BUTTON)
    )
    await message.delete()


@Client.on_message(commandpro(["/son", "/end", "/son{BOT_USERNAME}", "/end{BOT_USERNAME}"]) & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    chat_id = message.chat.id 
    for x in callsmusic.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        await message.reply_text("β’> **Εu anda mΓΌzik Γ§almΔ±yor**")
    else:
        try:
            queues.clear(chat_id)
        except QueueEmpty:
            pass
        await callsmusic.pytgcalls.leave_group_call(chat_id)
        await _.send_message(
            message.chat.id,
            "β’> **MΓΌzik durduruldu !**"
        )

@Client.on_message(commandpro(["/skip", "/atla", "/atla{BOT_USERNAME}", "/skip{BOT_USERNAME}"]) & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    global que
    chat_id = message.chat.id
    for x in callsmusic.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        
        await message.reply_text(
            "**Atlamam iΓ§in ΕarkΔ± Γ§almam gerekiyor !**",
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )
        await message.delete()
    else:
        queues.task_done(chat_id)
        
        if queues.is_empty(chat_id):
            await callsmusic.pytgcalls.leave_group_call(chat_id)
        else:
            await callsmusic.pytgcalls.change_stream(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        callsmusic.queues.get(chat_id)["file"],
                    ),
                ),
            )
    
    await message.reply_photo(
        photo=SKIPPED,
        caption=f"SΔ±radaki ΕarkΔ±ya geΓ§ildi β",
        reply_markup=InlineKeyboardMarkup(BUTTON)
    )
    await message.delete()

