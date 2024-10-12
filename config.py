from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "0b520ca0bacb2a29469faf063b6c38b1")
      API_ID = int(getenv("API_ID", "9196094"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "7492219896:AAHOcP2Pgl-jOYiRvwRliImVi8xhAaZgns0")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002156218433:-1002223245236").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
