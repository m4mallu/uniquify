# 🗿 [Uniquify](https://t.me/RMProjects)
<br>
Uniquify is a simple telegram interface bot that can utilize for deleting the duplicate media files from a chat.
Presently supported media  types are documents video and audio.

## Process:
 - Bot is an interface only.
 - Session user is doing the function.
 - So, `Bot doesn't need to be in the chat`.
 - Session user need to be an admin in the chat with `Delete messages privilege`
 - Commands can only run by the Authorized users.
 - Add chat id using command -  Eg:`/chat -100123456789` (-100 not mandatory)
 - Add a delay to the process - Eg: `/delay 2` (Delay not mandatory)
 - Finally, run `/purge` to start the process.
 - Realtime duplicate count with current message id will be updated while the process.

## Deploy to Heroku:
<p align="left">
  <a href="https://heroku.com/deploy?template=https://github.com/m4mallu/uniquify">
     <img height="30px" src="https://img.shields.io/badge/Deploy%20To%20Heroku-blueviolet?style=for-the-badge&logo=heroku">
  </a>
</p>

## Variables:

* `API_HASH`    Your API Hash from my.telegram.org
* `API_ID`      Your API ID from my.telegram.org
* `BOT_TOKEN`   Your bot token from @BotFather
* `AUTH_USERS`  Create a list of User Ids to use this bot
* `TG_USER_SESSION` [Click Here](https://replit.com/@ayrahikari/pyrogram-session-maker) to generate a User Session String.

## Deploy Locally:

Create a `config.py` with the above variables (Refer sample_config.py)
```
git clone https://github.com/m4mallu/uniquify
cd uniquify
virtualenv -p python3 venv
. ./venv/bin/activate
pip3 install -r requirements.txt
python3 main.py
```

## @BotFather Commands
```
start - Check alive
chat - Add chat id (Admin Only)
delay - Add a process delay (Admin Only)
purge - Initiate the process (Admin Only)
```

#### [Join Telegram Bot Update Channel](https://t.me/RMProjects)
## Developer: [𝑅𝑒𝓃𝒿𝒾𝓉𝒽 𝑀𝒶𝓃𝑔𝒶𝓁](https://t.me/space4renjith)

<p align="center">
    <a href="https://t.me/space4renjith">
        <img alt="GPL3" src ="https://telegra.ph/file/c4f778ccfc576a954dd20.gif" width="340" height="214"/>
    </a>
</p>


