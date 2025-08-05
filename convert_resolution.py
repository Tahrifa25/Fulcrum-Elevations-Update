import math

def arcseconds_to_meters(resolution_arcsec: float, latitude_deg: float) -> dict:
    """
    Converts a resolution in arc-seconds to horizontal and vertical accuracy in meters.
    
    Parameters:
    - resolution_arcsec: Resolution in arc-seconds (e.g., 1 for 1" resolution)
    - latitude_deg: Latitude in decimal degrees (e.g., 36.5 for Tennessee)
    
    Returns:
    - Dictionary with 'horizontal_accuracy_m' and 'vertical_accuracy_m'
    """
    # Constants
    meters_per_degree_lat = 111_320  # Approximate length of a degree of latitude in meters
    meters_per_degree_lon = 111_320 * math.cos(math.radians(latitude_deg))  # Varies with latitude

    # Convert arc-seconds to degrees
    resolution_deg = resolution_arcsec / 3600.0

    # Accuracy
    vertical_accuracy_m = resolution_deg * meters_per_degree_lat
    horizontal_accuracy_m = resolution_deg * meters_per_degree_lon

    return {
        "horizontal_accuracy_m": round(horizontal_accuracy_m, 2),
        "vertical_accuracy_m": round(vertical_accuracy_m, 2)
    }