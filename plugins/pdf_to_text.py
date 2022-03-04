import os 
from os import error, system, name
import logging
import pyrogram
import PyPDF2
import time
from decouple import config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply
from pyrogram.types import User, Message, Document 

DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/PyDF/")
# TXT_LOCATION =  os.environ.get("TXT_LOCATION", "./DOWNLOADS/txt/")
path = './DOWNLOADS/txt/bughunter0.txt'

@Client.on_message(filters.command(["pdf2txt"])) # PdfToText 
async def pdf_to_text(bot, message):
      try :
           if message.reply_to_message:
                pdf_path = DOWNLOAD_LOCATION + f"{message.chat.id}.pdf" #pdfFileObject
                txt = await message.reply("Downloading.....")
                await message.reply_to_message.download(pdf_path)  
                await txt.edit("Downloaded File")
                pdf = open(pdf_path,'rb')
                pdf_reader = PyPDF2.PdfFileReader(pdf) #pdfReaderObject
                await txt.edit("Getting Number of Pages....")
                num_of_pages = pdf_reader.getNumPages() # Number of Pages
                await txt.edit(f"Found {num_of_pages} Page")
                page_no = pdf_reader.getPage(0) # pageObject
                await txt.edit("Extracting Text from PDF...")
                page_content = """ """ # EmptyString   
                with open(f'{message.chat.id}.txt', 'a+') as text_path:   
                  for page in range (0,num_of_pages):
                      file_write = open(f'{message.chat.id}.txt','a+') 
                      page_no = pdf_reader.getPage(page) # Iteration of page number
                      page_content = page_no.extractText()
                      file_write.write(f"\n page number - {page} \n") # writing Page Number as Title
                      file_write.write(f" {page_content} ")   # writing page content
                      file_write.write(f"\n © BugHunterBots \n ") # Adding Page footer
                   #  await message.reply_text(f"**Page Number  :  {page}  **\n\n  ` {page_content} `\n     @BugHunterBots\n\n") # Use this Line of code to get Pdf Text as Messages
                        
                with open(f'{message.chat.id}.txt', 'a+') as text_path:  
                      await message.reply_document(f"{message.chat.id}.txt",caption="@Ultimate_library")      
         
                os.remove(pdf_path)
                os.remove(f"{message.chat.id}.txt")  
           else :
                await message.reply("Please Reply to PDF file")
      except Exception as error :
           await txt.delete()
           await message.reply_text(f"{error}")
           os.remove(pdf_path)
           os.remove(f"{message.chat.id}.txt") 
