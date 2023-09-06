import json
import requests
import googlemaps
import logging

from datetime import datetime

from tools.constants import ADDRESS_COMPONENTS_LITERAL_STR, ADDRESS_STR, GEOMETRY_LITERAL_STR, GOOGLE_API_STR, LATITUDE_LITERAL_STR, LOCATION_LITERAL_STR, LONGITUDE_LITERAL_STR, LONGNAME_LITERAL_STR, NEIGHBORHOOD_STR, TYPES_LITERAL_STR

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)



def geocoding(st: int = 1300) -> dict:
    """
    return geocode_result: dict
    """

    try:
        gmaps = googlemaps.Client(key=GOOGLE_API_STR)

        #geocoding address
        geocode_result = gmaps.geocode(f"{st} {ADDRESS_STR}")[0]
        
        if not geocode_result:
            raise googlemaps.exceptions.HTTPError()
        
        return geocode_result

    except googlemaps.exceptions.HTTPError as er:
        logging.info(f'sending error.... {er}')
        

def get_location(st: int = 1300) -> list:
    """
    return geo_lon_lat: list 
    """

    geocode = geocoding(st)
    location = geocode[GEOMETRY_LITERAL_STR][LOCATION_LITERAL_STR]

    longitude = location[LONGITUDE_LITERAL_STR]
    latitude = location[LATITUDE_LITERAL_STR]

    geo_lon_lat: list(float, float) = [longitude,latitude]

    logging.info(f"Latitude is {geo_lon_lat[0]} and longitude is {geo_lon_lat[1]}")

    return geo_lon_lat

def get_neighborhood(st: int = 1300) -> str:
    """
    return neighborhood_name: str 
    """

    geocode = geocoding(st)

    address_components = geocode[ADDRESS_COMPONENTS_LITERAL_STR]
    
    for component in address_components:
        if NEIGHBORHOOD_STR in component[TYPES_LITERAL_STR]:
            neighborhood_name = component[LONGNAME_LITERAL_STR]
    
    logging.info(f"The neighborhood is {neighborhood_name}")
    return neighborhood_name
