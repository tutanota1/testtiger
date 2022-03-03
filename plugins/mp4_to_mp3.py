import os
from pyrogram import Client, filters

@Client.on_message(filters.command(["mp4tomp3"])) 
async def mp3(bot, message):
 try:
           if message.reply_to_message:
               file_path = DOWNLOAD_LOCATION + f"{message.from_user.id}.mp3"
               txt = await message.reply_text("Downloading to My server.....")
               await message.download(file_path)
               await txt.edit_text("Downloaded Successfully")
    
               # convert to audio
               await txt.edit_text("Converting to audio")
               await message.reply_audio(audio=file_path, caption="@BugHunterBots", quote=True)
    
               # remove file
               try:
                   os.remove(file_path)
               except:
                   pass
