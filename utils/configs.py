import os
import time


class Var(object):

    # Get a bot token from botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    # Get from my.telegram.org
    API_ID = int(os.environ.get("API_ID", 12345))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "")


    # To record start time of bot
    BOT_START_TIME = time.time()

    # You Can Get An API Key From https://api.imgbb.com.
    API = os.environ.get("API", None)

    OWNER_ID = int(os.environ.get("OWNER_ID", "853393439"))
    BOT_NAME = os.environ.get("BOT_NAME", "ImgBBRobot")

    START_PIC = "https://i.imgur.com/zYIllxt.jpg"
    HELP_PIC = "https://i.imgur.com/AmxAlix.jpg"


class Tr(object):

    START_TEXT = """
👋 Hi ! {} Welcome To @Imgbb_bot

**With This Bot You Can Hosts Your Images On imgbb.com **

You Can Send An Image As Forwarded Message From Any Chat/Channel Or Upload It As Photo Or File.
"""

    ABOUT_TEXT = """🤖 **My Name:** [ImgBB](t.me/@imgbb_bot)

📝 **Language:** [Python 3](https://www.python.org)

📚 **Framework:** [Pyrogram](https://github.com/pyrogram/pyrogram)

📡 **Hosted On:** [Railway](railway.app)

👨‍💻 **Developer:** [Being Ramesh](t.me/Rksowner)

💡 **Source Code:** [Github](https://github.com/AmineSoukara/ImgBB-Bot/fork)

👥 **Support Group:** [Rks Help](https://t.me/+9UIG-51jj442ZWM1)

📢 **Updates Channel:** [Being Ramesh](https://t.me/rksmoviez)


❤ [Donate](https://www.paypal.me/Rameshkusahu) (PayPal)
"""

    HELP_TEXT = """💡 Just Send Me Your Photo And I'll Upload it To You .  That's it

❤ [Donate](https://www.paypal.me/Rameshkusahu) (PayPal)
"""

    ERR_TEXT = "⚠️ API Not Found"

    ERRTOKEN_TEXT = "😶 The Access Token Provided Is Expired, Revoked, Malformed Or Invalid For Other Reasons. DM @AmineSoukara",

    WAIT = "💬 Please Wait !!"
