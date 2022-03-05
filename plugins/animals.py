from pyrogram import Client, filters
from plugins.http import get, resp_get


@Clent.on_message(filters.command("catfacts"))
async def catfacts(client, message):
    """
    Get cat facts
    """
    message = await message.reply_text("`Getting cat facts...`")
    resp = await get("https://cat-fact.herokuapp.com/facts/random")
    return await message.edit(resp["text"])


@Client.on_message(filters.command("animalfacts"))
async def animalfacts(client, message):
    somerandomvariable = await get("https://axoltlapi.herokuapp.com/")
    return await message.reply_photo(somerandomvariable["url"], caption=somerandomvariable["facts"])


@Client.on_message(filters.command("dogfacts"))
async def dogfacts(client, message):
    somerandomvariable = await get("https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number=1")
    return await message.reply_text(somerandomvariable[0]["fact"])
