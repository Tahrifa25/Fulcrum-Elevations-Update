import requests

def get_from_usgs(lat, lon):
    usgsURL=f"https://epqs.nationalmap.gov/v1/json?x={lon}&y={lat}&wkid=4326&units=Feet&includeDate=false"
    #print("Getting elevations from USGS...") 
    
    try:
        response = requests.get(usgsURL, timeout=5)
        response.raise_for_status()
        elevation = response.json()["value"]
        return elevation
    
    except Exception as e:
        print(f"Failed to fetch elevation from USGS: {e}")
        return None