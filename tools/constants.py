from typing import Final
from decouple import config

GOOGLE_API_STR: Final[str] = config("GOOGLE_API")
ADDRESS_STR: Final[str] = '1300 SE Stark Street, Portland, OR 97214'