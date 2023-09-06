from typing import Final
from decouple import config

GOOGLE_API_STR: Final[str] = config("GOOGLE_API")
ADDRESS_STR: Final[str] = 'SE Stark Street, Portland, OR 97214'
NEIGHBORHOOD_STR: Final[str] = 'neighborhood'
TYPES_LITERAL_STR: Final[str] = 'types'
LONGNAME_LITERAL_STR: Final[str] = 'long_name'
GEOMETRY_LITERAL_STR: Final[str] = 'geometry'
LOCATION_LITERAL_STR: Final[str] = 'location'
LONGITUDE_LITERAL_STR: Final[str] = 'lng'
LATITUDE_LITERAL_STR: Final[str] = 'lat'
ADDRESS_COMPONENTS_LITERAL_STR: Final[str] = 'address_components'