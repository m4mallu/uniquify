from bot import Bot
from presets import Presets
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
from plugins.commands import purge_status
from support.buttons import reply_markup_back, reply_markup_start


@Client.on_callback_query(filters.regex(r'^help_btn$'))
async def help_button(b: Bot, cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit_text(Presets.HELP_MESSAGE,
                               reply_markup=reply_markup_back
                               )

@Client.on_callback_query(filters.regex(r'^back_btn$'))
async def back_button(b: Bot, cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit_text(Presets.WELCOME_MSG.format(cb.from_user.mention),
                               reply_markup=reply_markup_start
                               )

@Client.on_callback_query(filters.regex(r'^close_btn$'))
async def close_button(b: Bot, cb: CallbackQuery):
    await cb.message.delete()


@Client.on_callback_query(filters.regex(r'^cancel_btn$'))
async def cancel_button(b: Bot, cb: CallbackQuery):
    id = int(cb.from_user.id)
    try:
        purge_status.pop(id)
    except Exception:
        pass
