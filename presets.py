class Presets(object):
    FILE_TYPES = ['document', 'video', 'audio']
    WELCOME_MSG = "Hello... <b>{}</b>\n<code>I can remove duplicate media files from your chat. " \
                  "For more, see ma help.</code>"
    HELP_MESSAGE = """
<i>Using this bot you can delete duplicate medias from the chat configured.

Bot is only an interface to do the process, while string session user is doing the deleting job. Bot doesn't need to be in the chat.

String session user must be an admin to the chat id configured, with 'Delete Messages' privilege.

Supported medias are: Document, video and Audio file.

Duplicate Media counter and current message id will displays in the UI with process cancel button.</i>

<b>Admin only commands are:</b>
/chat -100xxxxxxxxxx
/delay 10 (10 second delay)
/purge - <i>Delete duplicate medias</i>
    """
    WAIT_MSG = "<b>Please wait...</b>"
    NOT_AUTH_TXT = "<b>You are not Authorized !</b>"
    CHECKING_MSG = "<i>Looking for Duplicates..</i>"
    CANCELLED_MSG = "<b>Purging Cancelled by user</b>"
    NO_DUPLICATES = "<b>Congrats</b> 🤗\n<i>There are no duplicates found in the chat id given</i>"
    DELAY_CNF = "<b>Success</b> ✅\n<i>Delay of </i> {} <i>Seconds will be applied\nin the process.</i>"
    INVALID_DELAY = "<b>Error</b> ❎\n<i>Input must be in the format</i>\n>>  <code>/delay 10</code>"
    CHAT_ID_CNF = "<b>Success</b> ✅\n<i>Chat id</i> <code>{}</code><i> saved !\n\nYou can now execute:</i> /purge"
    NOT_IN_CHAT = "<b>Error</b> ❎\n<i>Session User is not a member in this chat. Join this chat as an admin, and" \
                  " try again later..</i> ☹️"
    INCORRECT_PERMISSION = "<b>Error</b> ❎\n<i>Session user is not an admin / doesn't have the privilege to</i><b> " \
                           "Delete Messages</b>" \
                           "<i> in this chat</i> ☹️"
    INVALID_CHAT = "<b>Invalid Input</b> ❎\n<i>Input must be in the format</i>\n<code>/chat -10025486542156</code>"
    DELETING_MSGS = """
<b>Messages deleted   : {}</b>
\xad                                                                 \xad
<b>Message id covered: {}</b>
    """
    CANCEL_TEXT = "\xad          <b>🇮🇳 | Click to cancel        \xad</b>"
    PROCESS_FINISHED_TEXT = "<b>Success</b> ✅\n<i>Deleted all the duplicate messages.</i>"
    PROCESSING_MSG = "<b>Please wait...</b>\n<i>This will take some time to figure out\nthe duplicates. Have" \
                     " a cup of coffee..\nBy the time i'll finish it off !</i>"
    PURGE_ERROR = "<b>Error</b> ❎\n<i>Configure the chat id first</i>  ☹️"
