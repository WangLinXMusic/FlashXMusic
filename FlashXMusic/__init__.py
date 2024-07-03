from FlashXMusic.core.bot import Hotty
from FlashXMusic.core.dir import dirr
from FlashXMusic.core.git import git
from FlashXMusic.core.userbot import Userbot
from FlashXMusic.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Hotty()
userbot = Userbot()
api = SafoneAPI()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

APP = "sasukevipmusicbot"  # connect music api key "Dont change it"
