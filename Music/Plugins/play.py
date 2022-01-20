import os
import time
from os import path
import random
import asyncio
import shutil
from pytube import YouTube
from yt_dlp import YoutubeDL
from Music import converter
import yt_dlp
import shutil
import psutil
from pyrogram import Client
from pyrogram.types import Message, Voice
from pytgcalls import StreamType
from pytgcalls.types.input_stream import InputAudioStream, InputStream
from sys import version as pyver
from Music import (
    dbb,
    app,
    BOT_USERNAME,
    BOT_ID,
    BOT_NAME,
    ASSID,
    ASSNAME,
    ASSUSERNAME,
    ASSMENTION,
)
from Music.MusicUtilities.tgcallsrun import (
    music,
    convert,
    download,
    clear,
    get,
    is_empty,
    put,
    task_done,
    ASS_ACC,
)
from Music.MusicUtilities.database.queue import (
    get_active_chats,
    is_active_chat,
    add_active_chat,
    remove_active_chat,
    music_on,
    is_music_playing,
    music_off,
)
from Music.MusicUtilities.database.onoff import (
    is_on_off,
    add_on,
    add_off,
)
from Music.MusicUtilities.database.chats import (
    get_served_chats,
    is_served_chat,
    add_served_chat,
    get_served_chats,
)
from Music.MusicUtilities.helpers.inline import (
    play_keyboard,
    search_markup,
    play_markup,
    playlist_markup,
    audio_markup,
    play_list_keyboard,
)
from Music.MusicUtilities.database.blacklistchat import (
    blacklisted_chats,
    blacklist_chat,
    whitelist_chat,
)
from Music.MusicUtilities.database.gbanned import (
    get_gbans_count,
    is_gbanned_user,
    add_gban_user,
    add_gban_user,
)
from Music.MusicUtilities.database.theme import (
    _get_theme,
    get_theme,
    save_theme,
)
from Music.MusicUtilities.database.assistant import (
    _get_assistant,
    get_assistant,
    save_assistant,
)
from Music.config import DURATION_LIMIT
from Music.MusicUtilities.helpers.decorators import errors
from Music.MusicUtilities.helpers.filters import command
from Music.MusicUtilities.helpers.gets import (
    get_url,
    themes,
    random_assistant,
    ass_det,
)
from Music.MusicUtilities.helpers.logger import LOG_CHAT
from Music.MusicUtilities.helpers.thumbnails import gen_thumb
from Music.MusicUtilities.helpers.chattitle import CHAT_TITLE
from Music.MusicUtilities.helpers.ytdl import ytdl_opts 
from Music.MusicUtilities.helpers.inline import (
    play_keyboard,
    search_markup2,
    search_markup,
)
from pyrogram import filters
from typing import Union
import subprocess
from asyncio import QueueEmpty
import shutil
import os
from youtubesearchpython import VideosSearch
from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant
from pyrogram.types import Message, Audio, Voice
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    Message,
)

flex = {}
chat_watcher_group = 3

def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(":")))
    )

@Client.on_message(command(["play", f"play@{BOT_USERNAME}", "p"]))
async def play(_, message: Message):
    chat_id = message.chat.id  
    if message.sender_chat:
        return await message.reply_text("❌ You're an Anonymous Admin\n✅ Kembalikan ke Akun Pengguna Dari Hak Admin.")  
    user_id = message.from_user.id
    chat_title = message.chat.title
    username = message.from_user.first_name
    checking = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    if await is_on_off(1):
        LOG_ID = "-1001184239224"
        if int(chat_id) != int(LOG_ID):
            return await message.reply_text(f">> ❌ 𝐁𝐨𝐭 𝐬𝐞𝐝𝐚𝐧𝐠 𝐝𝐚𝐥𝐚𝐦 𝐌𝐚𝐢𝐧𝐭𝐞𝐧𝐚𝐧𝐜𝐞, 𝐌𝐨𝐡𝐨𝐧 𝐦𝐚𝐚𝐟 𝐚𝐭𝐚𝐬 𝐤𝐞𝐭𝐢𝐝𝐚𝐤𝐧𝐲𝐚𝐦𝐚𝐧𝐚𝐧𝐧𝐲𝐚")
        return await message.reply_text(f">> ❌ 𝐁𝐨𝐭 𝐬𝐞𝐝𝐚𝐧𝐠 𝐝𝐚𝐥𝐚𝐦 𝐌𝐚𝐢𝐧𝐭𝐞𝐧𝐚𝐧𝐜𝐞, 𝐌𝐨𝐡𝐨𝐧 𝐦𝐚𝐚𝐟 𝐚𝐭𝐚𝐬 𝐤𝐞𝐭𝐢𝐝𝐚𝐤𝐧𝐲𝐚𝐦𝐚𝐧𝐚𝐧𝐧𝐲𝐚")
    a = await app.get_chat_member(message.chat.id , BOT_ID)
    if a.status != "administrator":
        await message.reply_text(f"𝐒𝐚𝐲𝐚 𝐩𝐞𝐫𝐥𝐮 𝐦𝐞𝐧𝐣𝐚𝐝𝐢 𝐚𝐝𝐦𝐢𝐧 𝐝𝐞𝐧𝐠𝐚𝐧 𝐛𝐞𝐛𝐞𝐫𝐚𝐩𝐚 𝐢𝐳𝐢𝐧:\n\n>> **can_manage_voice_chats:** 𝐔𝐧𝐭𝐮𝐤 𝐦𝐞𝐧𝐠𝐞𝐥𝐨𝐥𝐚 𝐨𝐛𝐫𝐨𝐥𝐚𝐧 𝐬𝐮𝐚𝐫𝐚\n>> **can_delete_messages:** 𝐔𝐧𝐭𝐮𝐤 𝐦𝐞𝐧𝐠𝐡𝐚𝐩𝐮𝐬 𝐒𝐚𝐦𝐩𝐚𝐡 𝐲𝐚𝐧𝐠 𝐃𝐢𝐜𝐚𝐫𝐢 𝐌𝐮𝐬𝐢𝐤\n>> **can_invite_users**: 𝐔𝐧𝐭𝐮𝐤 𝐦𝐞𝐧𝐠𝐮𝐧𝐝𝐚𝐧𝐠 𝐚𝐬𝐢𝐬𝐭𝐞𝐧 𝐮𝐧𝐭𝐮𝐤 𝐦𝐞𝐧𝐠𝐨𝐛𝐫𝐨𝐥\n>> **can_restrict_members**: 𝐔𝐧𝐭𝐮𝐤 𝐌𝐞𝐥𝐢𝐧𝐝𝐮𝐧𝐠𝐢 𝐌𝐮𝐬𝐢𝐤 𝐝𝐚𝐫𝐢 𝐒𝐩𝐚𝐦𝐦𝐞𝐫.")
        return
    if not a.can_manage_voice_chats:
        await message.reply_text(
        "❌ 𝐒𝐚𝐲𝐚 𝐭𝐢𝐝𝐚𝐤 𝐦𝐞𝐦𝐢𝐥𝐢𝐤𝐢 𝐢𝐳𝐢𝐧 𝐲𝐚𝐧𝐠 𝐝𝐢𝐩𝐞𝐫𝐥𝐮𝐤𝐚𝐧 𝐮𝐧𝐭𝐮𝐤 𝐦𝐞𝐥𝐚𝐤𝐮𝐤𝐚𝐧 𝐭𝐢𝐧𝐝𝐚𝐤𝐚𝐧 𝐢𝐧𝐢."
        + "\n**Izin:** **𝐊𝐄𝐋𝐎𝐋𝐀 𝐂𝐇𝐀𝐓 𝐒𝐔𝐀𝐑𝐀**")
        return
    if not a.can_delete_messages:
        await message.reply_text(
        "❌ 𝐒𝐚𝐲𝐚 𝐭𝐢𝐝𝐚𝐤 𝐦𝐞𝐦𝐢𝐥𝐢𝐤𝐢 𝐢𝐳𝐢𝐧 𝐲𝐚𝐧𝐠 𝐝𝐢𝐩𝐞𝐫𝐥𝐮𝐤𝐚𝐧 𝐮𝐧𝐭𝐮𝐤 𝐦𝐞𝐥𝐚𝐤𝐮𝐤𝐚𝐧 𝐭𝐢𝐧𝐝𝐚𝐤𝐚𝐧 𝐢𝐧𝐢."
        + "\n**Izin:** **𝐇𝐀𝐏𝐔𝐒 𝐏𝐄𝐒𝐀𝐍**")
        return
    if not a.can_invite_users:
        await message.reply_text(
        "❌ 𝐒𝐚𝐲𝐚 𝐭𝐢𝐝𝐚𝐤 𝐦𝐞𝐦𝐢𝐥𝐢𝐤𝐢 𝐢𝐳𝐢𝐧 𝐲𝐚𝐧𝐠 𝐝𝐢𝐩𝐞𝐫𝐥𝐮𝐤𝐚𝐧 𝐮𝐧𝐭𝐮𝐤 𝐦𝐞𝐥𝐚𝐤𝐮𝐤𝐚𝐧 𝐭𝐢𝐧𝐝𝐚𝐤𝐚𝐧 𝐢𝐧𝐢."
        + "\n**Izin:** **𝐈𝐍𝐕𝐈𝐓𝐄 𝐏𝐄𝐍𝐆𝐆𝐔𝐍𝐀 𝐌𝐄𝐋𝐀𝐋𝐔𝐈 𝐋𝐈𝐍𝐊**")
        return
    if not a.can_restrict_members:
        await message.reply_text(
        "❌ 𝐒𝐚𝐲𝐚 𝐭𝐢𝐝𝐚𝐤 𝐦𝐞𝐦𝐢𝐥𝐢𝐤𝐢 𝐢𝐳𝐢𝐧 𝐲𝐚𝐧𝐠 𝐝𝐢𝐩𝐞𝐫𝐥𝐮𝐤𝐚𝐧 𝐮𝐧𝐭𝐮𝐤 𝐦𝐞𝐥𝐚𝐤𝐮𝐤𝐚𝐧 𝐭𝐢𝐧𝐝𝐚𝐤𝐚𝐧 𝐢𝐧𝐢."
        + "\n**Izin:** **𝐁𝐀𝐍 𝐏𝐄𝐍𝐆𝐆𝐔𝐍𝐀**")
        return
    try:
        b = await app.get_chat_member(message.chat.id , ASSID) 
        if b.status == "kicked":
            await message.reply_text(f"❌ {ASSNAME}(@{ASSUSERNAME}) 𝐃𝐢𝐛𝐚𝐧𝐧𝐞𝐝 𝐝𝐢 𝐨𝐛𝐫𝐨𝐥𝐚𝐧 𝐆𝐫𝐨𝐮𝐩 𝐀𝐧𝐝𝐚 **{chat_title}**\n\n𝐔𝐧𝐛𝐚𝐧 𝐩𝐞𝐦𝐛𝐥𝐨𝐤𝐢𝐫𝐚𝐧𝐧𝐲𝐚 𝐭𝐞𝐫𝐥𝐞𝐛𝐢𝐡 𝐝𝐚𝐡𝐮𝐥𝐮 𝐮𝐧𝐭𝐮𝐤 𝐦𝐞𝐧𝐠𝐠𝐮𝐧𝐚𝐤𝐚𝐧 𝐌𝐮𝐬𝐢𝐤")
            return
    except UserNotParticipant:
        if message.chat.username:
            try: 
                await ASS_ACC.join_chat(f"{message.chat.username}")
                await message.reply(f"✅ {ASSNAME} 𝐁𝐞𝐫𝐡𝐚𝐬𝐢𝐥 𝐁𝐞𝐫𝐠𝐚𝐛𝐮𝐧𝐠",) 
                await remove_active_chat(chat_id)
            except Exception as e:
                await message.reply_text(f"❌ **𝐀𝐬𝐢𝐬𝐭𝐞𝐧 𝐆𝐚𝐠𝐚𝐥 𝐁𝐞𝐫𝐠𝐚𝐛𝐮𝐧𝐠**\n\n**Reason**:{e}")
                return
        else:
            try:
                xxy = await app.export_chat_invite_link(message.chat.id)
                yxy = await app.revoke_chat_invite_link(message.chat.id, xxy)
                await ASS_ACC.join_chat(yxy.invite_link)
                await message.reply(f"✅ {ASSNAME} 𝐁𝐞𝐫𝐡𝐚𝐬𝐢𝐥 𝐁𝐞𝐫𝐠𝐚𝐛𝐮𝐧𝐠",) 
                await remove_active_chat(chat_id)
            except UserAlreadyParticipant:
                pass
            except Exception as e:
                return await message.reply_text(f"❌ **𝐀𝐬𝐢𝐬𝐭𝐞𝐧 𝐆𝐚𝐠𝐚𝐥 𝐁𝐞𝐫𝐠𝐚𝐛𝐮𝐧𝐠**\n\n**Alasan**:{e}")       
    audio = (message.reply_to_message.audio or message.reply_to_message.voice) if message.reply_to_message else None
    url = get_url(message)
    await message.delete()
    fucksemx = 0
    if audio:
        fucksemx = 1
        what = "Audio Searched"
        await LOG_CHAT(message, what)
        mystic = await message.reply_text(f"**🔄 𝐌𝐞𝐦𝐩𝐫𝐨𝐬𝐞𝐬 𝐀𝐮𝐝𝐢𝐨 𝐲𝐚𝐧𝐠 𝐃𝐢𝐛𝐞𝐫𝐢𝐤𝐚𝐧 𝐎𝐥𝐞𝐡 {username}**")
        if audio.file_size > 157286400:
            await mystic.edit_text("❌ **𝐔𝐤𝐮𝐫𝐚𝐧 𝐅𝐢𝐥𝐞 𝐀𝐮𝐝𝐢𝐨 𝐇𝐚𝐫𝐮𝐬 𝐊𝐮𝐫𝐚𝐧𝐠 𝐃𝐚𝐫𝐢 150 𝐦𝐛**") 
            return
        duration = round(audio.duration / 60)
        if duration > DURATION_LIMIT:
            return await mystic.edit_text(f"❌ **𝐊𝐞𝐬𝐚𝐥𝐚𝐡𝐚𝐧 𝐃𝐮𝐫𝐚𝐬𝐢**\n\n**𝐃𝐮𝐫𝐚𝐬𝐢 𝐲𝐚𝐧𝐠 𝐃𝐢𝐢𝐳𝐢𝐧𝐤𝐚𝐧: **{DURATION_LIMIT} 𝐦𝐢𝐧𝐮𝐭𝐞(s)\n**𝐃𝐮𝐫𝐚𝐬𝐢 𝐲𝐚𝐧𝐠 𝐃𝐢𝐭𝐞𝐫𝐢𝐦𝐚:** {duration} minute(s)")
        file_name = audio.file_unique_id + '.' + (
            (
                audio.file_name.split('.')[-1]
            ) if (
                not isinstance(audio, Voice)
            ) else 'ogg'
        )
        file_name = path.join(path.realpath('downloads'), file_name)
        file = await convert(
            (
                await message.reply_to_message.download(file_name)
            )
            if (
                not path.isfile(file_name)
            )
            else file_name,
        )
        title = "Selected Audio from Telegram"
        link = "https://t.me/TurboMusicChnl"
        thumb = "cache/audioplay.jpg"
        videoid = "smex1"
    elif url:
        what = "URL Searched"
        await LOG_CHAT(message, what)
        query = message.text.split(None, 1)[1]
        mystic = await message.reply_text("Processing Url")
        ydl_opts = {"format": "bestaudio/best"}
        try:
            results = VideosSearch(query, limit=1)
            for result in results.result()["result"]:
                title = (result["title"])
                duration = (result["duration"])
                views = (result["viewCount"]["short"])  
                thumbnail = (result["thumbnails"][0]["url"])
                link = (result["link"])
                idxz = (result["id"])
                videoid = (result["id"])
        except Exception as e:
            return await mystic.edit_text(f"❌ **𝐋𝐚𝐠𝐮 𝐓𝐢𝐝𝐚𝐤 𝐃𝐢𝐭𝐞𝐦𝐮𝐤𝐚𝐧**\n**Possible Reason:**{e}")    
        smex = int(time_to_seconds(duration))
        if smex > DURATION_LIMIT:
            return await mystic.edit_text(f"❌ **𝐊𝐞𝐬𝐚𝐥𝐚𝐡𝐚𝐧 𝐃𝐮𝐫𝐚𝐬𝐢**\n\n**𝐃𝐮𝐫𝐚𝐬𝐢 𝐲𝐚𝐧𝐠 𝐃𝐢𝐢𝐳𝐢𝐧𝐤𝐚𝐧: **90 𝐦𝐢𝐧𝐮𝐭𝐞(s)\n**𝐃𝐮𝐫𝐚𝐬𝐢 𝐲𝐚𝐧𝐠 𝐃𝐢𝐭𝐞𝐫𝐢𝐦𝐚:** {duration} 𝐦𝐢𝐧𝐮𝐭𝐞(s)")
        if duration == "None":
            return await mystic.edit_text("❌ **𝐌𝐚𝐚𝐟! 𝐕𝐢𝐝𝐞𝐨 𝐥𝐚𝐧𝐠𝐬𝐮𝐧𝐠 𝐭𝐢𝐝𝐚𝐤 𝐃𝐢𝐝𝐮𝐤𝐮𝐧𝐠**")
        if views == "None":
            return await mystic.edit_text("❌ **𝐌𝐚𝐚𝐟! 𝐕𝐢𝐝𝐞𝐨 𝐥𝐚𝐧𝐠𝐬𝐮𝐧𝐠 𝐭𝐢𝐝𝐚𝐤 𝐃𝐢𝐝𝐮𝐤𝐮𝐧𝐠**")
        semxbabes = (f"Downloading {title[:50]}")
        await mystic.edit(semxbabes)
        theme = random.choice(themes)
        ctitle = message.chat.title
        ctitle = await CHAT_TITLE(ctitle)
        userid = message.from_user.id
        thumb = await gen_thumb(thumbnail, title, userid, theme, ctitle)
        def my_hook(d): 
            if d['status'] == 'downloading':
                percentage = d['_percent_str']
                per = (str(percentage)).replace(".","", 1).replace("%","", 1)
                per = int(per)
                eta = d['eta']
                speed = d['_speed_str']
                size = d['_total_bytes_str']
                bytesx = d['total_bytes']
                if str(bytesx) in flex:
                    pass
                else:
                    flex[str(bytesx)] = 1
                if flex[str(bytesx)] == 1:
                    flex[str(bytesx)] += 1
                    try:
                        if eta > 2:
                            mystic.edit(f"Downloading {title[:80]}\n\n**Ukuran file:** {size}\n**Downloaded:** {percentage}\n**Speed:** {speed}\n**ETA:** {eta} sec")
                    except Exception as e:
                        pass
                if per > 250:    
                    if flex[str(bytesx)] == 2:
                        flex[str(bytesx)] += 1
                        if eta > 2:     
                            mystic.edit(f"Downloading {title[:80]}..\n\n**Ukuran file:** {size}\n**Downloaded:** {percentage}\n**Speed:** {speed}\n**ETA:** {eta} sec")
                        print(f"[{videoid}] Downloaded {percentage} dengan kecepatan {speed} | ETA: {eta} seconds")
                if per > 500:    
                    if flex[str(bytesx)] == 3:
                        flex[str(bytesx)] += 1
                        if eta > 2:     
                            mystic.edit(f"Downloading {title[:80]}...\n\n**Ukuran file:** {size}\n**Downloaded:** {percentage}\n**Speed:** {speed}\n**ETA:** {eta} sec")
                        print(f"[{videoid}] Downloaded {percentage} dengan kecepatan {speed} | ETA: {eta} seconds")
                if per > 800:    
                    if flex[str(bytesx)] == 4:
                        flex[str(bytesx)] += 1
                        if eta > 2:    
                            mystic.edit(f"Downloading {title[:80]}....\n\n**Ukuran file:** {size}\n**Downloaded:** {percentage}\n**Speed:** {speed}\n**ETA:** {eta} sec")
                        print(f"[{videoid}] Downloaded {percentage} dengan kecepatan {speed} | ETA: {eta} seconds")
            if d['status'] == 'finished': 
                try:
                    taken = d['_elapsed_str']
                except Exception as e:
                    taken = "00:00"
                size = d['_total_bytes_str']
                mystic.edit(f"**Downloaded {title[:80]}.....**\n\n**Ukuran file:** {size}\n**Time Taken:** {taken} sec\n\n**Converting File** [__FFmpeg processing__]")
                print(f"[{videoid}] Downloaded| Elapsed: {taken} seconds")  
        loop = asyncio.get_event_loop()
        x = await loop.run_in_executor(None, download, link, my_hook)
        file = await convert(x)
    else:
        if len(message.command) < 2:
            what = "Command"
            await LOG_CHAT(message, what)
            user_name = message.from_user.first_name
            thumb ="cache/IMG_20211201_214925_953.jpg"
            buttons = playlist_markup(user_name, user_id)
            hmo = await message.reply_photo(
            photo=thumb, 
            caption=("**Contoh Penggunaan:** /play [Nama Musik atau Tautan Youtube atau Balas Audio]\n\nJika Anda ingin memainkan Daftar Putar! Pilih salah satu dari Bawah."),    
            reply_markup=InlineKeyboardMarkup(buttons),
            ) 
            return
        what = "Query Given"
        await LOG_CHAT(message, what)
        query = message.text.split(None, 1)[1]
        mystic = await message.reply_text("**🔄 𝐒𝐞𝐚𝐫𝐜𝐡𝐢𝐧𝐠**")
        try:
            a = VideosSearch(query, limit=5)
            result = (a.result()).get("result")
            title1 = (result[0]["title"])
            duration1 = (result[0]["duration"])
            title2 = (result[1]["title"])
            duration2 = (result[1]["duration"])      
            title3 = (result[2]["title"])
            duration3 = (result[2]["duration"])
            title4 = (result[3]["title"])
            duration4 = (result[3]["duration"])
            title5 = (result[4]["title"])
            duration5 = (result[4]["duration"])
            ID1 = (result[0]["id"])
            ID2 = (result[1]["id"])
            ID3 = (result[2]["id"])
            ID4 = (result[3]["id"])
            ID5 = (result[4]["id"])
        except Exception as e:
            return await mystic.edit_text(f"❌ 𝐋𝐚𝐠𝐮 𝐓𝐢𝐝𝐚𝐤 𝐃𝐢𝐭𝐞𝐦𝐮𝐤𝐚𝐧.\n**𝐌𝐮𝐧𝐠𝐤𝐢𝐧 𝐊𝐚𝐫𝐞𝐧𝐚 𝐀𝐥𝐞𝐬𝐚𝐧:**{e}")
        thumb ="cache/IMG_20211201_214925_953.jpg"
        await mystic.delete()   
        buttons = search_markup(ID1, ID2, ID3, ID4, ID5, duration1, duration2, duration3, duration4, duration5, user_id, query)
        hmo = await message.reply_photo(
            photo=thumb, 
            caption=(
            f"""
**🎼 𝐒𝐢𝐥𝐚𝐡𝐤𝐚𝐧 𝐏𝐢𝐥𝐢𝐡 𝐋𝐚𝐠𝐮 𝐘𝐚𝐧𝐠 𝐈𝐧𝐠𝐢𝐧 𝐋𝐮 𝐏𝐮𝐭𝐚𝐫 𝐊𝐧𝐭𝐥 🎼**

¹ <b>{title1[:75]}</b>
  ┣ [ᴋᴇᴘᴏ ʟᴜ ᴋᴏɴᴛᴏʟ](https://t.me/{BOT_USERNAME}?start=info_{ID1})
  ┣ **ᴅᴇᴠᴇʟᴏᴘᴇʀ** : [{BOT_NAME}](t.me/{BOT_USERNAME})
  ┗ **ᴘᴇᴍɪᴍᴘɪɴ** : [» ʜɪʀᴏsʜɪ «](https://t.me/Bisubiarenak)

² <b>{title2[:75]}</b>
  ┣ [ᴋᴇᴘᴏ ʟᴜ ᴋᴏɴᴛᴏʟ](https://t.me/{BOT_USERNAME}?start=info_{ID2})
  ┣ **ᴅᴇᴠᴇʟᴏᴘᴇʀ** : [{BOT_NAME}](t.me/{BOT_USERNAME})
  ┗ **ᴘᴇᴍɪᴍᴘɪɴ** : [» ʜɪʀᴏsʜɪ «](https://t.me/Bisubiarenak)

³ <b>{title3[:75]}</b>
  ┣ [ᴋᴇᴘᴏ ʟᴜ ᴋᴏɴᴛᴏʟ](https://t.me/{BOT_USERNAME}?start=info_{ID3})
  ┣ **ᴅᴇᴠᴇʟᴏᴘᴇʀ** : [{BOT_NAME}](t.me/{BOT_USERNAME})
  ┗ **ᴘᴇᴍɪᴍᴘɪɴ** : [» ʜɪʀᴏsʜɪ «](https://t.me/Bisubiarenak)

⁴ <b>{title4[:75]}</b>
  ┣ [ᴋᴇᴘᴏ ʟᴜ ᴋᴏɴᴛᴏʟ](https://t.me/{BOT_USERNAME}?start=info_{ID3})
  ┣ **ᴅᴇᴠᴇʟᴏᴘᴇʀ** : [{BOT_NAME}](t.me/{BOT_USERNAME})
  ┗ **ᴘᴇᴍɪᴍᴘɪɴ** : [» ʜɪʀᴏsʜɪ «](https://t.me/Bisubiarenak)

⁵ <b>{title5[:75]}</b>
  ┣ [ᴋᴇᴘᴏ ʟᴜ ᴋᴏɴᴛᴏʟ](https://t.me/{BOT_USERNAME}?start=info_{ID3})
  ┣ **ᴅᴇᴠᴇʟᴏᴘᴇʀ** : [{BOT_NAME}](t.me/{BOT_USERNAME})
  ┗ **ᴘᴇᴍɪᴍᴘɪɴ** : [» ʜɪʀᴏsʜɪ «](https://t.me/Bisubiarenak)
"""),    
            reply_markup=InlineKeyboardMarkup(buttons),
        )  
        disable_web_page_preview=True
        return   
    if await is_active_chat(chat_id):
        position = await put(chat_id, file=file)
        _chat_ = ((str(file)).replace("_","", 1).replace("/","", 1).replace(".","", 1))
        cpl=(f"downloads/{_chat_}final.png")     
        shutil.copyfile(thumb, cpl) 
        f20 = open(f'search/{_chat_}title.txt', 'w')
        f20.write(f"{title}") 
        f20.close()
        f111 = open(f'search/{_chat_}duration.txt', 'w')
        f111.write(f"{duration}") 
        f111.close()
        f27 = open(f'search/{_chat_}username.txt', 'w')
        f27.write(f"{checking}") 
        f27.close()
        if fucksemx != 1:
            f28 = open(f'search/{_chat_}videoid.txt', 'w')
            f28.write(f"{videoid}") 
            f28.close()
            buttons = play_markup(videoid, user_id)
        else:
            f28 = open(f'search/{_chat_}videoid.txt', 'w')
            f28.write(f"{videoid}") 
            f28.close()
            buttons = audio_markup(videoid, user_id)
        checking = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
        await message.reply_photo(
            photo=thumb,
            caption=(f"""
<b>**🎼 𝐌𝐞𝐧𝐚𝐦𝐛𝐚𝐡𝐤𝐚𝐧 𝐊𝐞 𝐃𝐚𝐟𝐭𝐚𝐫 𝐀𝐧𝐭𝐫𝐢𝐚𝐧 𝐋𝐚𝐠𝐮 🎼**</b>

<b>🏷️ **𝐍𝐚𝐦𝐚** :</b> [{title[:80]}]({link})
<b>⏱️ **𝐃𝐮𝐫𝐚𝐬𝐢** :</b> {duration} 𝐌𝐞𝐧𝐢𝐭
<b>🎧 **𝐀𝐭𝐚𝐬 𝐏𝐞𝐫𝐦𝐢𝐧𝐭𝐚𝐚𝐧** : </b>{checking}
<b>🔢 **𝐏𝐨𝐬𝐢𝐬𝐢 𝐀𝐧𝐭𝐫𝐢𝐚𝐧 𝐊𝐞** » </b>{position}
"""),
            reply_markup=InlineKeyboardMarkup(buttons)
        )
        return await mystic.delete()     
    else: 
        await music_on(chat_id)
        await add_active_chat(chat_id)
        await music.pytgcalls.join_group_call(
            chat_id, 
            InputStream(
                InputAudioStream(
                    file,
                ),
            ),
            stream_type=StreamType().local_stream,
        )
        _chat_ = ((str(file)).replace("_","", 1).replace("/","", 1).replace(".","", 1))                                                                                           
        checking = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
        if fucksemx != 1:
            f28 = open(f'search/{_chat_}videoid.txt', 'w')
            f28.write(f"{videoid}") 
            f28.close()
            buttons = play_markup(videoid, user_id)
        else:
            f28 = open(f'search/{_chat_}videoid.txt', 'w')
            f28.write(f"{videoid}") 
            f28.close()
            buttons = audio_markup(videoid, user_id)
        await message.reply_photo(
        photo=thumb,
        reply_markup=InlineKeyboardMarkup(buttons),    
        caption=(f"""
<b>🏷 **𝐍𝐚𝐦𝐚** :</b> [{title[:80]}]({link})
<b>⏱️ **𝐃𝐮𝐫𝐚𝐬𝐢** :</b> {duration} 𝐌𝐞𝐧𝐢𝐭
<b>🎧 **𝐀𝐭𝐚𝐬 𝐩𝐞𝐫𝐦𝐢𝐧𝐭𝐚𝐚𝐧** :</b> {checking}
<b>⚡ **𝐏𝐞𝐦𝐢𝐦𝐩𝐢𝐧** : [𝐇𝐢𝐫𝐨𝐬𝐡𝐢](https://t.me/Bisubiarenak)
""")
        )   
        return await mystic.delete()
         
    
    
    
@Client.on_callback_query(filters.regex(pattern=r"Music"))
async def startyuplay(_,CallbackQuery): 
    callback_data = CallbackQuery.data.strip()
    chat_id = CallbackQuery.message.chat.id
    chat_title = CallbackQuery.message.chat.title
    callback_request = callback_data.split(None, 1)[1]
    userid = CallbackQuery.from_user.id 
    try:
        id,duration,user_id = callback_request.split("|") 
    except Exception as e:
        return await CallbackQuery.message.edit(f"❌ 𝐓𝐞𝐫𝐣𝐚𝐝𝐢 𝐤𝐞𝐬𝐚𝐥𝐚𝐡𝐚𝐧\n**𝐊𝐞𝐦𝐮𝐧𝐠𝐤𝐢𝐧𝐚𝐧 𝐚𝐥𝐚𝐬𝐚𝐧𝐧𝐲𝐚 bisa**:{e}")
    if duration == "None":
        return await CallbackQuery.message.reply_text(f"❌ **𝐌𝐚𝐚𝐟, 𝐕𝐢𝐝𝐞𝐨 𝐋𝐚𝐧𝐠𝐬𝐮𝐧𝐠 𝐭𝐢𝐝𝐚𝐤 𝐝𝐢𝐝𝐮𝐤𝐮𝐧𝐠**")      
    if CallbackQuery.from_user.id != int(user_id):
        return await CallbackQuery.answer("❌ **𝐈𝐧𝐢 𝐛𝐮𝐤𝐚𝐧 𝐮𝐧𝐭𝐮𝐤𝐦𝐮 𝐂𝐚𝐫𝐢 𝐋𝐚𝐠𝐮 𝐌𝐢𝐥𝐢𝐤 𝐀𝐧𝐝𝐚**", show_alert=True)
    await CallbackQuery.message.delete()
    checking = f"[{CallbackQuery.from_user.first_name}](tg://user?id={userid})"
    url = (f"https://www.youtube.com/watch?v={id}")
    videoid = id
    idx = id
    smex = int(time_to_seconds(duration))
    if smex > DURATION_LIMIT:
        await CallbackQuery.message.reply_text(f"❌ **𝐊𝐞𝐬𝐚𝐥𝐚𝐡𝐚𝐧 𝐃𝐮𝐫𝐚𝐬𝐢**\n\n✅ **𝐃𝐮𝐫𝐚𝐬𝐢 𝐲𝐚𝐧𝐠 𝐃𝐢𝐢𝐳𝐢𝐧𝐤𝐚𝐧: **90 𝐦𝐢𝐧𝐮𝐭𝐞(s)\n📲 **𝐃𝐮𝐫𝐚𝐬𝐢 𝐲𝐚𝐧𝐠 𝐃𝐢𝐭𝐞𝐫𝐢𝐦𝐚:** {duration} 𝐦𝐢𝐧𝐮𝐭𝐞(s)")
        return 
    try:
        with yt_dlp.YoutubeDL(ytdl_opts) as ytdl:
            x = ytdl.extract_info(url, download=False)
    except Exception as e:
        return await CallbackQuery.message.reply_text(f"❌ 𝐆𝐚𝐠𝐚𝐥 𝐦𝐞𝐧𝐠𝐮𝐧𝐝𝐮𝐡 𝐯𝐢𝐝𝐞𝐨 𝐢𝐧𝐢.\n\n**Reason**:{e}") 
    title = (x["title"])
    await CallbackQuery.answer(f"Selected {title[:20]}.... \nProcessing...", show_alert=True)
    mystic = await CallbackQuery.message.reply_text(f"Downloading {title[:50]}")
    thumbnail = (x["thumbnail"])
    idx = (x["id"])
    videoid = (x["id"])
    def my_hook(d): 
        if d['status'] == 'downloading':
            percentage = d['_percent_str']
            per = (str(percentage)).replace(".","", 1).replace("%","", 1)
            per = int(per)
            eta = d['eta']
            speed = d['_speed_str']
            size = d['_total_bytes_str']
            bytesx = d['total_bytes']
            if str(bytesx) in flex:
                pass
            else:
                flex[str(bytesx)] = 1
            if flex[str(bytesx)] == 1:
                flex[str(bytesx)] += 1
                try:
                    if eta > 2:
                        mystic.edit(f"Downloading {title[:80]}\n\n**Ukuran file:** {size}\n**Downloaded:** {percentage}\n**Speed:** {speed}\n**ETA:** {eta} sec")
                except Exception as e:
                    pass
            if per > 250:    
                if flex[str(bytesx)] == 2:
                    flex[str(bytesx)] += 1
                    if eta > 2:     
                        mystic.edit(f"Downloading {title[:80]}..\n\n**Ukuran file:** {size}\n**Downloaded:** {percentage}\n**Speed:** {speed}\n**ETA:** {eta} sec")
                    print(f"[{videoid}] Downloaded {percentage} dengan kecepatan {speed} | ETA: {eta} seconds")
            if per > 500:    
                if flex[str(bytesx)] == 3:
                    flex[str(bytesx)] += 1
                    if eta > 2:     
                        mystic.edit(f"Downloading {title[:80]}...\n\n**Ukuran file:** {size}\n**Downloaded:** {percentage}\n**Speed:** {speed}\n**ETA:** {eta} sec")
                    print(f"[{videoid}] Downloaded {percentage} dengan kecepatan {speed} | ETA: {eta} seconds")
            if per > 800:    
                if flex[str(bytesx)] == 4:
                    flex[str(bytesx)] += 1
                    if eta > 2:    
                        mystic.edit(f"Downloading {title[:80]}....\n\n**Ukuran file:** {size}\n**Downloaded:** {percentage}\n**Speed:** {speed}\n**ETA:** {eta} sec")
                    print(f"[{videoid}] Downloaded {percentage} dengan kecepatan {speed} | ETA: {eta} seconds")
        if d['status'] == 'finished': 
            try:
                taken = d['_elapsed_str']
            except Exception as e:
                taken = "00:00"
            size = d['_total_bytes_str']
            mystic.edit(f"**Downloaded {title[:50]}.....**\n\n**Ukuran file:** {size}\n**Time Taken:** {taken} sec\n\n**Converting File** [__FFmpeg processing__]")
            print(f"[{videoid}] Downloaded| Elapsed: {taken} seconds")    
    loop = asyncio.get_event_loop()
    x = await loop.run_in_executor(None, download, url, my_hook)
    file = await convert(x)
    theme = random.choice(themes)
    ctitle = CallbackQuery.message.chat.title
    ctitle = await CHAT_TITLE(ctitle)
    thumb = await gen_thumb(thumbnail, title, userid, theme, ctitle)
    await mystic.delete()
    if await is_active_chat(chat_id):
        position = await put(chat_id, file=file)
        buttons = play_markup(videoid, user_id)
        _chat_ = ((str(file)).replace("_","", 1).replace("/","", 1).replace(".","", 1))
        cpl=(f"downloads/{_chat_}final.png")     
        shutil.copyfile(thumb, cpl) 
        f20 = open(f'search/{_chat_}title.txt', 'w')
        f20.write(f"{title}") 
        f20.close()
        f111 = open(f'search/{_chat_}duration.txt', 'w')
        f111.write(f"{duration}") 
        f111.close()
        f27 = open(f'search/{_chat_}username.txt', 'w')
        f27.write(f"{checking}") 
        f27.close()
        f28 = open(f'search/{_chat_}videoid.txt', 'w')
        f28.write(f"{videoid}") 
        f28.close()
        await mystic.delete()
        m = await CallbackQuery.message.reply_photo(
        photo=thumb,
        caption=(f"""
<b>🎼 𝐌𝐞𝐧𝐚𝐦𝐛𝐚𝐡𝐤𝐚𝐧 𝐊𝐞 𝐃𝐚𝐟𝐭𝐚𝐫 𝐀𝐧𝐭𝐫𝐢𝐚𝐧 𝐋𝐚𝐠𝐮 🎼</b> 

<b>🏷 **𝐍𝐚𝐦𝐚** :</b> [{title[:80]}]({url})
<b>⏱️ **𝐃𝐮𝐫𝐚𝐬𝐢** :</b> {duration} 𝐌𝐞𝐧𝐢𝐭
<b>💡 **𝐒𝐭𝐚𝐭𝐮𝐬** : `Dalam antrian`
<b>🎧 **𝐀𝐭𝐚𝐬 𝐏𝐞𝐫𝐦𝐢𝐧𝐭𝐚𝐚𝐧** :</b> {checking}
<b>🔢 **𝐏𝐨𝐬𝐢𝐬𝐢 𝐀𝐧𝐭𝐫𝐢𝐚𝐧 𝐊𝐞** »</b> `{position}`
"""),
        reply_markup=InlineKeyboardMarkup(buttons)
        )
        os.remove(thumb)
        await CallbackQuery.message.delete()       
    else:
        await music_on(chat_id)
        await add_active_chat(chat_id)
        await music.pytgcalls.join_group_call(
            chat_id, 
            InputStream(
                InputAudioStream(
                    file,
                ),
            ),
            stream_type=StreamType().local_stream,
        )
        buttons = play_markup(videoid, user_id)
        await mystic.delete()
        m = await CallbackQuery.message.reply_photo(
        photo=thumb,
        reply_markup=InlineKeyboardMarkup(buttons),    
        caption=(f"""
<b>🏷 **𝐍𝐚𝐦𝐚** :</b> [{title[:80]}]({url})
<b>⏱️ **𝐃𝐮𝐫𝐚𝐬𝐢** :</b> {duration} 𝐌𝐞𝐧𝐢𝐭
<b>💡 **𝐒𝐭𝐚𝐭𝐮𝐬** : `Sedang memutar`
<b>🎧 **𝐀𝐭𝐚𝐬 𝐏𝐞𝐫𝐦𝐢𝐧𝐭𝐚𝐚𝐧** :</b> {checking}
<b>⚡ **𝐏𝐞𝐦𝐢𝐦𝐩𝐢𝐧** :</b> [𝐇𝐢𝐫𝐨𝐬𝐡𝐢](https://t.me/Bisubiarenak)
""")
        )   
        os.remove(thumb)
        await CallbackQuery.message.delete()

        
        
        
@Client.on_callback_query(filters.regex(pattern=r"popat"))
async def popat(_,CallbackQuery): 
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    print(callback_request)
    userid = CallbackQuery.from_user.id 
    try:
        id , query, user_id = callback_request.split("|") 
    except Exception as e:
        return await CallbackQuery.message.edit(f"❌ 𝐓𝐞𝐫𝐣𝐚𝐝𝐢 𝐤𝐞𝐬𝐚𝐥𝐚𝐡𝐚𝐧\n**𝐊𝐞𝐦𝐮𝐧𝐠𝐤𝐢𝐧𝐚𝐧 𝐚𝐥𝐚𝐬𝐚𝐧𝐧𝐲𝐚 𝐛𝐢𝐬𝐚**:{e}")       
    if CallbackQuery.from_user.id != int(user_id):
        return await CallbackQuery.answer("❌ **𝐈𝐧𝐢 𝐛𝐮𝐤𝐚𝐧 𝐮𝐧𝐭𝐮𝐤𝐦𝐮 𝐂𝐚𝐫𝐢 𝐋𝐚𝐠𝐮 𝐌𝐢𝐥𝐢𝐤 𝐀𝐧𝐝𝐚**", show_alert=True)
    i=int(id)
    query = str(query)
    try:
        a = VideosSearch(query, limit=10)
        result = (a.result()).get("result")
        title1 = (result[0]["title"])
        duration1 = (result[0]["duration"])
        title2 = (result[1]["title"])
        duration2 = (result[1]["duration"])      
        title3 = (result[2]["title"])
        duration3 = (result[2]["duration"])
        title4 = (result[3]["title"])
        duration4 = (result[3]["duration"])
        title5 = (result[4]["title"])
        duration5 = (result[4]["duration"])
        title6 = (result[5]["title"])
        duration6 = (result[5]["duration"])
        title7= (result[6]["title"])
        duration7 = (result[6]["duration"])      
        title8 = (result[7]["title"])
        duration8 = (result[7]["duration"])
        title9 = (result[8]["title"])
        duration9 = (result[8]["duration"])
        title10 = (result[9]["title"])
        duration10 = (result[9]["duration"])
        ID1 = (result[0]["id"])
        ID2 = (result[1]["id"])
        ID3 = (result[2]["id"])
        ID4 = (result[3]["id"])
        ID5 = (result[4]["id"])
        ID6 = (result[5]["id"])
        ID7 = (result[6]["id"])
        ID8 = (result[7]["id"])
        ID9 = (result[8]["id"])
        ID10 = (result[9]["id"])                    
    except Exception as e:
        return await mystic.edit_text(f"❌ 𝐋𝐚𝐠𝐮 𝐓𝐢𝐝𝐚𝐤 𝐃𝐢𝐭𝐞𝐦𝐮𝐤𝐚𝐧.\n**𝐊𝐞𝐦𝐮𝐧𝐠𝐤𝐢𝐧𝐚𝐧 𝐀𝐥𝐚𝐬𝐚𝐧:**{e}")
    if i == 1:
        buttons = search_markup2(ID6, ID7, ID8, ID9, ID10, duration6, duration7, duration8, duration9, duration10 ,user_id, query)
        await CallbackQuery.edit_message_text(
            f"""
<b>**🎼 𝐒𝐢𝐥𝐚𝐡𝐤𝐚𝐧 𝐏𝐢𝐥𝐢𝐡 𝐋𝐚𝐠𝐮 𝐘𝐚𝐧𝐠 𝐈𝐧𝐠𝐢𝐧 𝐋𝐮 𝐏𝐮𝐭𝐚𝐫 𝐊𝐧𝐭𝐥 🎼**</b>

⁶ <b>{title6[:75]}</b>
  ┣ [ᴋᴇᴘᴏ ʟᴜ ᴋᴏɴᴛᴏʟ](https://t.me/{BOT_USERNAME}?start=info_{ID3})
  ┣ **ᴅᴇᴠᴇʟᴏᴘᴇʀ** : [{BOT_NAME}](t.me/{BOT_USERNAME})
  ┗ **ᴘᴇᴍɪᴍᴘɪɴ** : [» ʜɪʀᴏsʜɪ «](https://t.me/Bisubiarenak)

⁷ <b>{title7[:75]}</b>
  ┣ [ᴋᴇᴘᴏ ʟᴜ ᴋᴏɴᴛᴏʟ](https://t.me/{BOT_USERNAME}?start=info_{ID3})
  ┣ **ᴅᴇᴠᴇʟᴏᴘᴇʀ** : [{BOT_NAME}](t.me/{BOT_USERNAME})
  ┗ **ᴘᴇᴍɪᴍᴘɪɴ** : [» ʜɪʀᴏsʜɪ «](https://t.me/Bisubiarenak)

⁸ <b>{title8[:75]}</b>
  ┣ [ᴋᴇᴘᴏ ʟᴜ ᴋᴏɴᴛᴏʟ](https://t.me/{BOT_USERNAME}?start=info_{ID3})
  ┣ **ᴅᴇᴠᴇʟᴏᴘᴇʀ** : [{BOT_NAME}](t.me/{BOT_USERNAME})
  ┗ **ᴘᴇᴍɪᴍᴘɪɴ** : [» ʜɪʀᴏsʜɪ «](https://t.me/Bisubiarenak)

⁹ <b>{title9[:75]}</b>
  ┣ [ᴋᴇᴘᴏ ʟᴜ ᴋᴏɴᴛᴏʟ](https://t.me/{BOT_USERNAME}?start=info_{ID3})
  ┣ **ᴅᴇᴠᴇʟᴏᴘᴇʀ** : [{BOT_NAME}](t.me/{BOT_USERNAME})
  ┗ **ᴘᴇᴍɪᴍᴘɪɴ** : [» ʜɪʀᴏsʜɪ «](https://t.me/Bisubiarenak)

¹⁰ <b>{title10[:75]}</b>
  ┣ [ᴋᴇᴘᴏ ʟᴜ ᴋᴏɴᴛᴏʟ](https://t.me/{BOT_USERNAME}?start=info_{ID3})
  ┣ **ᴅᴇᴠᴇʟᴏᴘᴇʀ** : [{BOT_NAME}](t.me/{BOT_USERNAME})
  ┗ **ᴘᴇᴍɪᴍᴘɪɴ** : [» ʜɪʀᴏsʜɪ «](https://t.me/Bisubiarenak)
""", 
            reply_markup=InlineKeyboardMarkup(buttons),
        )  
        disable_web_page_preview=True
        return    
    if i == 2:
        buttons = search_markup(ID1, ID2, ID3, ID4, ID5, duration1, duration2, duration3, duration4, duration5, user_id, query)
        await CallbackQuery.edit_message_text(
            f"""
<b>**🎼 𝐒𝐢𝐥𝐚𝐡𝐤𝐚𝐧 𝐏𝐢𝐥𝐢𝐡 𝐋𝐚𝐠𝐮 𝐘𝐚𝐧𝐠 𝐈𝐧𝐠𝐢𝐧 𝐋𝐮 𝐏𝐮𝐭𝐚𝐫 𝐊𝐧𝐭𝐥 🎼**</b>

¹ <b>{title1[:75]}</b>
  ┣ [ᴋᴇᴘᴏ ʟᴜ ᴋᴏɴᴛᴏʟ](https://t.me/{BOT_USERNAME}?start=info_{ID3})
  ┣ **ᴅᴇᴠᴇʟᴏᴘᴇʀ** : [{BOT_NAME}](t.me/{BOT_USERNAME})
  ┗ **ᴘᴇᴍɪᴍᴘɪɴ** : [» ʜɪʀᴏsʜɪ «](https://t.me/Bisubiarenak)

² <b>{title2[:75]}</b>
  ┣ [ᴋᴇᴘᴏ ʟᴜ ᴋᴏɴᴛᴏʟ](https://t.me/{BOT_USERNAME}?start=info_{ID3})
  ┣ **ᴅᴇᴠᴇʟᴏᴘᴇʀ** : [{BOT_NAME}](t.me/{BOT_USERNAME})
  ┗ **ᴘᴇᴍɪᴍᴘɪɴ** : [» ʜɪʀᴏsʜɪ «](https://t.me/Bisubiarenak)

³ <b>{title3[:75]}</b>
  ┣ [ᴋᴇᴘᴏ ʟᴜ ᴋᴏɴᴛᴏʟ](https://t.me/{BOT_USERNAME}?start=info_{ID3})
  ┣ **ᴅᴇᴠᴇʟᴏᴘᴇʀ** : [{BOT_NAME}](t.me/{BOT_USERNAME})
  ┗ **ᴘᴇᴍɪᴍᴘɪɴ** : [» ʜɪʀᴏsʜɪ «](https://t.me/Bisubiarenak)

⁴ <b>{title4[:75]}</b>
  ┣ [ᴋᴇᴘᴏ ʟᴜ ᴋᴏɴᴛᴏʟ](https://t.me/{BOT_USERNAME}?start=info_{ID3})
  ┣ **ᴅᴇᴠᴇʟᴏᴘᴇʀ** : [{BOT_NAME}](t.me/{BOT_USERNAME})
  ┗ **ᴘᴇᴍɪᴍᴘɪɴ** : [» ʜɪʀᴏsʜɪ «](https://t.me/Bisubiarenak)

⁵ <b>{title5[:75]}</b>
  ┣ [ᴋᴇᴘᴏ ʟᴜ ᴋᴏɴᴛᴏʟ](https://t.me/{BOT_USERNAME}?start=info_{ID3})
  ┣ **ᴅᴇᴠᴇʟᴏᴘᴇʀ** : [{BOT_NAME}](t.me/{BOT_USERNAME})
  ┗ **ᴘᴇᴍɪᴍᴘɪɴ** : [» ʜɪʀᴏsʜɪ «](https://t.me/Bisubiarenak)
""",    
            reply_markup=InlineKeyboardMarkup(buttons),
        )  
        disable_web_page_preview=True
        return    
        
@app.on_message(filters.command("playplaylist"))
async def play_playlist_cmd(_, message):
    thumb ="cache/IMG_20211201_214925_953.jpg"
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    buttons = playlist_markup(user_name, user_id)
    await message.reply_photo(
    photo=thumb, 
    caption=("**𝐌𝐮𝐬𝐢𝐜'𝐬 𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 𝐅𝐞𝐚𝐭𝐮𝐫𝐞**\n\n𝐏𝐢𝐥𝐢𝐡 𝐃𝐚𝐟𝐭𝐚𝐫 𝐏𝐮𝐭𝐚𝐫 𝐲𝐚𝐧𝐠 𝐢𝐧𝐠𝐢𝐧 𝐀𝐧𝐝𝐚 𝐦𝐚𝐢𝐧𝐤𝐚𝐧."),    
    reply_markup=InlineKeyboardMarkup(buttons),
    )
    return
