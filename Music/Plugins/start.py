import yt_dlp
from Music import (
    ASSID,
    BOT_ID,
    BOT_NAME,
    BOT_USERNAME,
    OWNER,
    SUDOERS,
    app,
)
from Music.MusicUtilities.database.chats import is_served_chat
from Music.MusicUtilities.database.queue import remove_active_chat
from Music.MusicUtilities.database.sudo import get_sudoers
from Music.MusicUtilities.helpers.inline import personal_markup
from Music.MusicUtilities.helpers.thumbnails import down_thumb
from Music.MusicUtilities.helpers.ytdl import ytdl_opts
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)


def start_pannel():
    buttons = [
        [
            InlineKeyboardButton("Support", url="https://t.me/demonslayersupport"),
            InlineKeyboardButton("Updates", url=f"https://t.me/demonits"),
        ],
    ]
    return (
        "🎛 **{BOT_NAME} Merupakan salah satu dari bot telegram yang bisa memutar musik di grup**",
        buttons,
    )


pstart_markup = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "➕ ᴛᴀᴍʙᴀʜᴋᴀɴ sᴀʏᴀ ᴋᴇ ɢʀᴏᴜᴘ ᴀɴᴅᴀ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
        ],
        [
            InlineKeyboardButton("ɢʀᴜᴘ sᴜᴘᴘʀᴏᴛ", url="https://t.me/demonslayersupport"),
            InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ ɪɴғᴏ", url=f"https://t.me/demonits"),
        ],
        [
            InlineKeyboardButton(
                "ᴏᴡɴᴇʀ", url=f"https://t.me/Biarenakliatnyaaaa"),
            InlineKeyboardButton("ᴄᴏᴍᴍᴀɴᴅ", url="https://telegra.ph/Hiroshi-12-28-2"),
        ],
    ]
)
     
welcome_captcha_group = 2


@app.on_message(filters.new_chat_members, group=welcome_captcha_group)
async def welcome(_, message: Message):
    chat_id = message.chat.id
    for member in message.new_chat_members:
        try:
            if member.id in OWNER:
                return await message.reply_text(
                    f"💡 ᴘᴇᴍɪʟɪᴋ ʙᴏᴛ [{member.mention}] ʙᴀʀᴜ sᴀᴊᴀ ʙᴇʀɢᴀʙᴜɴɢ ᴅɪ ɢʀᴜᴘ ɪɴɪ"
                )
            if member.id in SUDOERS:
                return await message.reply_text(
                    f"💡 ᴀᴅᴍɪɴ ʙᴏᴛ [{member.mention}] ʙᴀʀᴜ sᴀᴊᴀ ʙᴇʀɢᴀʙᴜɴɢ ᴅɪ ɢʀᴜᴘ ɪɴɪ"
                )
            if member.id == ASSID:
                await remove_active_chat(chat_id)
            if member.id == BOT_ID:
                out = start_pannel()
                await message.reply_text(
                    f"""
👋 ** ʜᴀʟᴏ sᴇɴᴀɴɢ ʀᴀsᴀɴʏᴀ ʙɪsᴀ ʙᴇʀɢᴀʙᴜɴɢ ᴅɪ ɢʀᴜᴘ ɪɴɪ**

💡 **ᴊᴀɴɢᴀɴ ʟᴜᴘᴀ ᴜɴᴛᴜᴋ ᴍᴇɴᴊᴀᴅɪᴋᴀɴ sᴀʏᴀ sᴇʙᴀɢᴀɪ ᴀᴅᴍɪɴ ᴅɪ ɢʀᴜᴘ ɪɴɪ**
""",
                    reply_markup=InlineKeyboardMarkup(out[1]),
                    disable_web_page_preview=True
                )
                return
        except BaseException:
            return


@Client.on_message(
    filters.group
    & filters.command(
        ["start", "help", f"start@{BOT_USERNAME}", f"help@{BOT_USERNAME}"]
    )
)
async def start(_, message: Message):
    chat_id = message.chat.id
    out = start_pannel()
    await message.reply_text(
        f"""
ᴛᴇʀɪᴍᴀ ᴋᴀsɪʜ ᴛᴇʟᴀʜ ᴍᴇᴍᴀsᴜᴋᴋᴀɴ sᴀʏᴀ ᴅɪ {message.chat.title}.
ᴍᴜsɪᴋ ɪᴛᴜ ʜɪᴅᴜᴘ.

ᴜɴᴛᴜᴋ ʙᴀɴᴛᴜᴀɴ sɪʟᴀʜᴋᴀɴ ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ᴅɪʙᴀᴡᴀʜ.
""",
        reply_markup=InlineKeyboardMarkup(out[1]),
        disable_web_page_preview=True
    )
    return


@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def play(_, message: Message):
    if len(message.command) == 1:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
        rpk = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"
        await app.send_message(
            message.chat.id,
            text=f"""
**✨ sᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ {rpk}!

💬 [{BOT_NAME}](t.me/{BOT_USERNAME}) ᴍᴇᴍᴜɴɢᴋɪɴᴋᴀɴ ᴀɴᴅᴀ ᴜɴᴛᴜᴋ ᴍᴇᴍᴜᴛᴀʀ ᴍᴜsɪᴋ ᴘᴀᴅᴀ ɢʀᴜᴘ ᴍᴇʟᴀʟᴜɪ ᴏʙʀᴏʟᴀɴ sᴜᴀʀᴀ ʏᴀɴɢ ʙᴀʀᴜ ᴅɪ ᴛᴇʟᴇɢʀᴀᴍ**

""",
            parse_mode="markdown",
            reply_markup=pstart_markup,
            reply_to_message_id=message.message_id,
        )
    elif len(message.command) == 2:
        query = message.text.split(None, 1)[1]
        f1 = query[0]
        f2 = query[1]
        f3 = query[2]
        finxx = f"{f1}{f2}{f3}"
        if str(finxx) == "inf":
            query = (str(query)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            with yt_dlp.YoutubeDL(ytdl_opts) as ytdl:
                x = ytdl.extract_info(query, download=False)
            thumbnail = x["thumbnail"]
            searched_text = f"""
🔍 **Video Track Information**

❇️**Judul:** {x["title"]}

⏳ **Durasi:** {round(x["duration"] / 60)} Mins
👀 **Ditonton:** `{x["view_count"]}`
👍 **Suka:** `{x["like_count"]}`
👎 **Tidak suka:** `{x["dislike_count"]}`
⭐️ **Peringkat Rata-rata:** {x["average_rating"]}
🎥 **Nama channel:** {x["uploader"]}
📎 **Channel Link:** [Kunjungi Dari Sini]({x["channel_url"]})
🔗 **Link:** [Link]({x["webpage_url"]})
"""
            link = x["webpage_url"]
            buttons = personal_markup(link)
            userid = message.from_user.id
            thumb = await down_thumb(thumbnail, userid)
            await app.send_photo(
                message.chat.id,
                photo=thumb,
                caption=searched_text,
                parse_mode="markdown",
                reply_markup=InlineKeyboardMarkup(buttons),
            )
        if str(finxx) == "sud":
            sudoers = await get_sudoers()
            text = "**📝 DAFTAR PENGGUNA SUDO**\n\n"
            for count, user_id in enumerate(sudoers, 1):
                try:
                    user = await app.get_users(user_id)
                    user = user.first_name if not user.mention else user.mention
                except Exception:
                    continue
                text += f"- {user}\n"
            if not text:
                await message.reply_text("Tidak Ada Pengguna Sudo")
            else:
                await message.reply_text(text)
