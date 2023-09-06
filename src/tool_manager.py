import googlemaps
import logging

from datetime import datetime

from tools.constants import ADDRESS_STR, GOOGLE_API_STR

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)



def geocoding() -> tuple:
    """
    return tuple with latitude and longitude
    """

    try:
        gmaps = googlemaps.Client(key=GOOGLE_API_STR)

        #geocoding address
        geocode_result = gmaps.geocode(ADDRESS_STR)
        
        if not geocode_result:
            raise googlemaps.exceptions.HTTPError()
        
        location = geocode_result[0]['geometry']['location']

        geo_lat_lon: tuple(float, float) = (location['lat'],location['lng'])

        logging.info(f"lat is {geo_lat_lon[0]} and lng is {geo_lat_lon[1]}")

        return geo_lat_lon

    except googlemaps.exceptions.HTTPError as er:
        logging.info(f'sending error.... {er}')
        