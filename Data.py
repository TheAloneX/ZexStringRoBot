from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}
Here For help You to Create Session
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
    ]

    # Help Message
    HELP = """
💫 **Available Commands** 💫

/shelp - This Message
/generate - Start Generating Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    # About Message
    ABOUT = """"""
