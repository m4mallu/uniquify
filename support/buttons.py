from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

cancel_button = [
    [
        InlineKeyboardButton('Cancel', callback_data='cancel_btn')
    ]
]

start_button = [
    [
        InlineKeyboardButton('Support Chat', url='t.me/RMProjects'),
        InlineKeyboardButton('Help', callback_data='help_btn')
    ]
]

back_button = [
    [
        InlineKeyboardButton('⬅️ Back', callback_data='back_btn')
    ]
]

close_button = [
    [
        InlineKeyboardButton('Support Chat', url='t.me/RMProjects'),
        InlineKeyboardButton('Close', callback_data='close_btn')
    ]
]

reply_markup_close = InlineKeyboardMarkup(close_button)
reply_markup_back = InlineKeyboardMarkup(back_button)
reply_markup_cancel = InlineKeyboardMarkup(cancel_button)
reply_markup_start = InlineKeyboardMarkup(start_button)
