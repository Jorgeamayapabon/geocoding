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
FORMATTED_ADDRESS_LITERAL_STR: Final[str] = 'formatted_address'
PLACE_ID_LITERAL_STR: Final[str] = 'place_id'

SUCCESSFUL_RESPONSE_DICT: Final[dict] = {'address_components': [{'long_name': '1300', 'short_name': '1300', 'types': ['street_number']}, {'long_name': 'Southeast Stark Street', 'short_name': 'SE Stark St', 'types': ['route']}, {'long_name': 'Southeast Portland', 'short_name': 'Southeast Portland', 'types': ['neighborhood', 'political']}, {'long_name': 'Portland', 'short_name': 'Portland', 'types': ['locality', 'political']}, {'long_name': 'Multnomah County', 'short_name': 'Multnomah County', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'Oregon', 'short_name': 'OR', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'United States', 'short_name': 'US', 'types': ['country', 'political']}, {'long_name': '97214', 'short_name': '97214', 'types': ['postal_code']}], 'formatted_address': '1300 SE Stark St, Portland, OR 97214, USA', 'geometry': {'bounds': {'northeast': {'lat': 45.5192416, 'lng': -122.6517382}, 'southwest': {'lat': 45.51871329999999, 'lng': -122.6524753}}, 'location': {'lat': 45.5189567, 'lng': -122.652102}, 'location_type': 'ROOFTOP', 'viewport': {'northeast': {'lat': 45.52028388029149, 'lng': -122.6507577697085}, 'southwest': {'lat': 45.51758591970849, 'lng': -122.6534557302915}}}, 'place_id': 'ChIJpQGHkKOglVQRbqiHjgzzNgM', 'types': ['premise']}