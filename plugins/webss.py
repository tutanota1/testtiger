from pyrogram import Client, filters
from pyrogram.types import Message

from plugins.http import get

@Client.on_message(filters.command("webss"))
async def take_ss(_, message: Message):
    try:
        if len(message.command) != 2:
            return await message.reply_text("Give A Url To Fetch Screenshot.")
        url = message.text.split(None, 1)[1]
        m = await message.reply_text("**Taking Screenshot**")
        await m.edit("**Uploading**")
        ss = await get(f"https://screenshotapi1.herokuapp.com/?print={url}")['url']
        try:
            await message.reply_photo(
                photo=ss,
                quote=False,
            )
        except TypeError:
            return await m.edit("No Such Website.")
        await m.delete()
    except Exception as e:
        await message.reply_text(str(e))
