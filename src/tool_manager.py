import googlemaps
import logging

from tools.constants import ADDRESS_COMPONENTS_LITERAL_STR, ADDRESS_STR, GEOMETRY_LITERAL_STR, GOOGLE_API_STR, LATITUDE_LITERAL_STR, LOCATION_LITERAL_STR, LONGITUDE_LITERAL_STR, LONGNAME_LITERAL_STR, NEIGHBORHOOD_STR, TYPES_LITERAL_STR

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)

def geocoding(st: int = 1300, address: str = ADDRESS_STR) -> dict:
    """
    Geocode an address using the Google Maps API.

    Parameters:
        st (int): The street number to geocode (default is 1300).

    Returns:
        dict: A dictionary containing geocoding information for the specified address.

    Raises:
        googlemaps.exceptions.HTTPError: If there is an error while making the API request.

    Example:
        geocode_result = geocoding(1600)
        print(geocode_result)
    """

    try:
        gmaps = googlemaps.Client(key=GOOGLE_API_STR)

        #geocoding address
        geocode_result = gmaps.geocode(f"{st} {address}")
        
        if not geocode_result:
            raise googlemaps.exceptions.HTTPError(400)
        
        return geocode_result[0]

    except googlemaps.exceptions.HTTPError as er:
        logging.info(f'sending error.... {er}')
        

def get_location(st: int = 1300, address: str = ADDRESS_STR) -> list:
    """
    Retrieve the latitude and longitude coordinates for a given street address.

    Parameters:
        st (int): The street number to geocode (default is 1300).

    Returns:
        list: A list containing two floats, representing latitude and longitude coordinates.

    Example:
        geo_coordinates = get_location(1600)
        print(f"Latitude: {geo_coordinates[0]}, Longitude: {geo_coordinates[1]}")

    Note:
        This function internally uses the `geocoding` function to obtain the coordinates.
    """

    geocode = geocoding(st=st, address=address)
    location = geocode[GEOMETRY_LITERAL_STR][LOCATION_LITERAL_STR]

    longitude = location[LONGITUDE_LITERAL_STR]
    latitude = location[LATITUDE_LITERAL_STR]

    geo_lon_lat: list(float, float) = [longitude,latitude]

    logging.info(f"Latitude is {geo_lon_lat[0]} and longitude is {geo_lon_lat[1]}")

    return geo_lon_lat

def get_neighborhood(st: int = 1300, address: str = ADDRESS_STR) -> str:
    """
    Retrieve the neighborhood name for a given street address.

    Parameters:
        st (int): The street number to geocode (default is 1300).

    Returns:
        str: The name of the neighborhood.

    Example:
        neighborhood = get_neighborhood(1600)
        print(f"The neighborhood is {neighborhood}")
    """

    geocode = geocoding(st=st, address=address)

    address_components = geocode[ADDRESS_COMPONENTS_LITERAL_STR]
    
    for component in address_components:
        if NEIGHBORHOOD_STR in component[TYPES_LITERAL_STR]:
            neighborhood_name = component[LONGNAME_LITERAL_STR]
    
    logging.info(f"The neighborhood is {neighborhood_name}")

    return neighborhood_name

def recursive_get_neighborhood(prev_neighborhood_name: str = None, st: int = 1300, address: str = ADDRESS_STR) -> str:
    """
    Recursively retrieve and monitor changes in the neighborhood name for a given street address.

    Parameters:
        prev_neighborhood_name (str, optional): The previous neighborhood name (default is None).
        st (int): The street number to geocode (default is 1300).

    Returns:
        str: The new neighborhood name when it changes; otherwise, the final neighborhood name.

    Example:
        final_neighborhood = recursive_get_neighborhood(st=1600)
        print(f"The final neighborhood is {final_neighborhood}")

    Note:
        This function relies on the `get_neighborhood` function to obtain neighborhood names.
        It recursively increments the street number and monitors changes in the neighborhood name.
    """

    new_neighborhood_name = get_neighborhood(st=st, address=address)
    if not prev_neighborhood_name:
        logging.info(f"The previous neighborhood is {new_neighborhood_name}")    
        return recursive_get_neighborhood(prev_neighborhood_name=new_neighborhood_name)
    if prev_neighborhood_name != new_neighborhood_name:
        logging.info(f"The new neighborhood is {new_neighborhood_name}")
        logging.info(f"The Street is: {st}")
        return new_neighborhood_name
    return recursive_get_neighborhood(st=st+100, prev_neighborhood_name=new_neighborhood_name, address=address)