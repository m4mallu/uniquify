import os
import asyncio
from bot import Bot
from presets import Presets
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from support.buttons import reply_markup_start, reply_markup_cancel, reply_markup_close

purge_status = {}
chat = {}
main_delay = {}

if bool(os.environ.get("ENV", False)):
    from sample_config import Config
else:
    from config import Config

# ------------------------------ Start Function -------------------------- #
@Bot.on_message(filters.private & filters.command(['start', 'help']))
async def start_bot(c: Bot, m: Message):
    await m.reply_text(Presets.WELCOME_MSG.format(m.from_user.mention),
                       parse_mode='html',
                       disable_web_page_preview=True,
                       reply_markup=reply_markup_start
                       )


# --------------------------- Configure chat Function --------------------- #
@Bot.on_message(filters.private & filters.command('chat'))
async def config_chat(c: Bot, m: Message):
    id = int(m.from_user.id)
    msg = await m.reply_text(Presets.WAIT_MSG, m.message_id)
    if id not in Config.AUTH_USERS:
        await msg.edit_text(Presets.NOT_AUTH_TXT, reply_markup=reply_markup_close)
        return
    chat_id = str()
    status = []
    await asyncio.sleep(1)
    if (" " in m.text) and (m.text.split(" ")[1][2:].isdigit()):
        chat_str = m.text.split(" ")[1]
        if str(chat_str).startswith('-100'):
            chat_id = chat_str
        else:
            chat_id = '-100' + chat_str
        me = await c.USER.get_me()
        try:
            status = await c.USER.get_chat_member(int(chat_id), me.id)
        except Exception:
            await msg.edit(Presets.NOT_IN_CHAT, reply_markup=reply_markup_close)
            return
        if status.can_delete_messages:
            chat[id] = int(chat_id)
            await msg.edit(Presets.CHAT_ID_CNF.format(chat_id))
        else:
            await msg.edit(Presets.INCORRECT_PERMISSION, reply_markup=reply_markup_close)
    else:
        await m.delete()
        await msg.edit(Presets.INVALID_CHAT, reply_markup=reply_markup_close)


# ----------------------- Configure delay Function ----------------------- #
@Bot.on_message(filters.private & filters.command('delay'))
async def purge_delay(c: Bot, m: Message):
    id = int(m.from_user.id)
    msg = await m.reply_text(Presets.WAIT_MSG, m.message_id)
    if id not in Config.AUTH_USERS:
        await msg.edit_text(Presets.NOT_AUTH_TXT, reply_markup=reply_markup_close)
        return
    if (" " in m.text) and (m.text.split(" ")[1].isdigit()):
        value = int(m.text.split(" ")[1])
        main_delay[id] = value
        await msg.edit_text(Presets.DELAY_CNF.format(value), reply_markup=reply_markup_close)
    else:
        await m.delete()
        await msg.edit(Presets.INVALID_DELAY, reply_markup=reply_markup_close)


# ------------------------------- Delete duplicate function --------------------- #
@Bot.on_message(filters.private & filters.command('purge'))
async def delete_duplicates(c: Bot, m: Message):
    id_index = []
    duplicates = delay = count = int()
    id = int(m.from_user.id)
    purge_status[id] = id
    msg1 = await m.reply_text(Presets.PROCESSING_MSG)
    await asyncio.sleep(1)
    msg2 = await m.reply_text(Presets.CHECKING_MSG, reply_markup=reply_markup_cancel)
    if id in main_delay:
        delay = main_delay[id]
    if id in chat:
        await msg2.edit_text(Presets.CANCEL_TEXT, reply_markup=reply_markup_cancel)
        async for user_message in c.USER.iter_history(chat[id]):
            if id not in purge_status:
                try:
                    chat.pop(id)
                    main_delay.pop(id)
                except Exception:
                    pass
                if not duplicates:
                    await msg1.delete()
                await msg2.edit_text(Presets.CANCELLED_MSG, reply_markup=reply_markup_close)
                return
            if user_message and (not user_message.empty) and (id in purge_status):
                messages = await c.USER.get_messages(chat[id], user_message.message_id, replies=0)
                for file_type in tuple(Presets.FILE_TYPES):
                    media = getattr(messages, file_type, None)
                    if media is not None:
                        uid = str(media.file_unique_id)
                        if uid in id_index:
                            try:
                                await c.USER.delete_messages(chat[id], messages.message_id)
                            except FloodWait as e:
                                await asyncio.sleep(e.x)
                            except Exception:
                                pass
                            duplicates += 1
                            try:
                                await msg1.edit_text(Presets.DELETING_MSGS.format(duplicates, messages.message_id))
                            except FloodWait as e:
                                await asyncio.sleep(e.x)
                            except Exception:
                                pass
                            await asyncio.sleep(delay)
                        else:
                            id_index.append(uid)
                    count += 1
                    if count >= 99:
                        count = int()
                        await asyncio.sleep(3)
            else:
                pass
        if not duplicates:
            await msg1.delete()
            await msg2.edit_text(Presets.NO_DUPLICATES, reply_markup=reply_markup_close)
        else:
            await msg2.edit_text(Presets.PROCESS_FINISHED_TEXT, reply_markup=reply_markup_close)
        try:
            chat.pop(id)
            purge_status.pop(id)
            main_delay.pop(id)
        except Exception:
            pass
    else:
        await m.delete()
        await msg2.delete()
        await msg1.edit(Presets.PURGE_ERROR, reply_markup=reply_markup_close)
