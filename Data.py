from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}
Bot For help You to Create Session.
[➼](https://telegra.ph/file/9989afd6ad6ab59e1d43b.jpg) So What U Waiting For Generate String Session.
You can use me to generate pyrogram and telethon string session. Use below buttons to learn more !

Powered By [Zex](https://t.me/ZexNetwork)
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("♨️ Start Generating String", callback_data="generate")],
    ]

    generate_button = [
        [InlineKeyboardButton("♨️ Start Generating String", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("♨️ Start Generating String", callback_data="generate")],
        [InlineKeyboardButton("🗯️ Help", callback_data="help"),],
         [InlineKeyboardButton("💻 About", callback_data="about",],
    ]

    # Help Message
    HELP = """
💫 **Available Commands** 💫

/about - About The Bot
/help - This Message
/start - Start the Bot
/generate - Start Generating Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    # About Message
    ABOUT = """
**About This Bot** 

A telegram bot to Manage group and generate pyrogram and telethon string session by @TeamDeeCode

Source Code : [Click Here](https://github.com/AMANTYA1/String_gen)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @TeamDeeCode
    """
