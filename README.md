<h1 align="left">
    <a href="https://github.com/m4mallu">Uniquify</a>
    <img src="https://i.gifer.com/7Ie5.gif" height="45">
</h1>

#### Uniquify is a Telegram interface bot that can delete the duplicate media files from a chat.

<details>
    <summary><b>Process</b></summary>
    <p align="left"></p>
    <ul>
        <li>Bot is an interface only.</li>
        <li>Session user is doing the job.</li>
        <li>So, <strike>Bot doesn't need to be in the chat</strike>.</li>
        <li>Session user <strike>need to be an admin</strike> in the chat with <code>Delete messages privilege</code></li>
        <li>Commands can only run by the <code>Authorized users.</code></li>
        <li>Add chat id using command -  Eg: <code>/chat -100123456789</code> (-100 not mandatory)</li>
        <li>Add a delay to the process - Eg: <code>/delay 2</code> (Delay not mandatory)</li>
        <li>Finally, run <code>/purge</code> to start the process.</li>
        <li><strong>Presently supported media  types are <code>documents, video and audio</code>.</strong></li>
    </ul>
</details>
<details>
    <summary><b>Deploy</b></summary>
    <p align="left"></p>
    <b>1. <u>Deploy to Heroku</u></b><br>
        <a href="https://heroku.com/deploy?template=https://github.com/m4mallu/uniquify">
            <img height="30px" src="https://img.shields.io/badge/Deploy%20To%20Heroku-blueviolet?style=for-the-badge&logo=heroku">
    </a><br><br>
    <b>2. <u>Deploy to VPS</u></b><br>
    <ul>
        <li>Open a Linux Terminal and run the following commands.</li>
        <li><code>git clone https://github.com/m4mallu/uniquify</code></li>
        <li><code>cd uniquify</code></li>
        <li>Create a <code>config.py</code> file with the mandatory variables.(Refer <code>sample_config.py</code>)</li>
        <li>Run the following commands in the same terminal opened.</li>
        <li><code>virtualenv -p python3 venv</code></li>
        <li><code>. ./venv/bin/activate</code></li>
        <li><code>pip3 install -r requirements.txt</code></li>
        <li><code>python3 main.py</code></li>
    </ul>
</details>
<details>
    <summary><b>Mandatory Variables</b></summary>
    <p align="left">
        
    API_HASH            -   Your API Hash from my.telegram.org
    API_ID              -   Your API ID from my.telegram.org
    BOT_TOKEN           -   Your Bot Token from @BotFather
    AUTH_USERS          -   Create a list of User Ids to use this bot
    TG_USER_SESSION     -   Your Telegram User Session String
</details>
<details>
    <summary><b>Generate User Session</b></summary>
    <p align="left"></p>
    <a href="https://replit.com/@ayrahikari/pyrogram-session-maker">
        <img src="https://img.shields.io/badge/Generate-String%20Session-orange" height="30" />
</a>
    <ul>
        <li>Open the above link and start the application.</li>
        <li>Give your APP_ID, API_HASH - Get it from <a href="https://my.telegram.org/auth"><b>HERE</b></a> </li>
        <li>On the next step, select <code>1 = User Bot</code> option .</li>
        <li>Give your phone number in <a href="https://www.cm.com/blog/how-to-format-international-telephone-numbers/">international format</a> .</li>
        <li>Give the OTP and Auth Phrase if any</li>
        <li>This will get your long user session string</li>
        <li><a href="https://docs.pyrogram.org/topics/storage-engines?highlight=string%20sessions#session-strings"><b>Keep the String safe, anyone can access your account using it.</b></a></li>
    </ul>
</details>
<details>
    <summary><b>@BotFather Commands</b></summary>
    <p align="left"></p>
    
    start   -   Check alive
    chat    -   Add chat id (Admin Only)
    delay   -   Add a process delay (Admin Only)
    purge   -   Initiate the process (Admin Only)
</details>
<details>
  <summary><b>Developer</b></summary>
    <p align="left">
        <img alt="GPL3" src ="https://c.tenor.com/10Zdx_RXqgcAAAAC/programming-crazy.gif" width="260px" style="max-width:100%;"/><br>
            <a href="https://t.me/space4renjith"><img src="https://img.shields.io/badge/Renjith-Mangal-orange" height="24">
        </a>&nbsp;
            <a href="https://t.me/rmprojects"><img src="https://img.shields.io/badge/Updates-Channel-orange" height="24">
        </a>
</p>
</details>
<details>
    <summary><b>Donate</b></summary>
    <p align="left"><br>
    <b>Buy me a coffee for the work !</b><br>
    <img src="https://telegra.ph/file/b926b7e8ea84826d81d8a.png" width="260px" style="max-width:100%;"/><br><br>
      <a href="https://www.paypal.me/space4renjith" target="_blank">
        <img src="https://img.shields.io/badge/Donate-Me-blueviolet?style=for-the-badge&logo=paypal">
    </a>
</p>
</details>
<details>
  <summary><b>Credits</b></summary>
    <p align="left">
      <a href="https://github.com/pyrogram/pyrogram">
        <img src="https://img.shields.io/badge/Pyrogram-MTProto%20API-orange?style=for-the-badge&logo=pyrogram" height="32.8">
    </a>
</p>
</details>
<details>
  <summary><b>License</b></summary>
    <p align="left">
    <a href="https://choosealicense.com/licenses/gpl-3.0/">
        <img src="https://img.shields.io/badge/License-GPLv3-blueviolet?style=for-the-badge&logo=gplv3">
    </a>
</p>
</details>
<p align="center">
    <a href="https://t.me/space4renjith">
        <img alt="GPL3" src ="https://telegra.ph/file/c4f778ccfc576a954dd20.gif" width="340" height="214"/>
    </a>
</p>


