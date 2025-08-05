import requests
from data_usgs import get_from_usgs
from data_fulcrum import get_from_fulcrum

def updating_elevation():
   
    headers, data, testdata = get_from_fulcrum()
    
##Using form id
    for testrecord in testdata["records"][:1]: #test code
     record_id = testrecord["id"]
     record_url = f"https://api.fulcrumapp.com/api/v2/records/{record_id}.json"
     print(" before update :", testrecord['form_values'].get('b1f0'))
     testrecord['form_values']["b1f0"] = "37.96833942"
     update_response = requests.put(record_url, headers=headers, json={'record': testrecord})
     print("response", update_response.json())
     print(" after update :", testrecord['form_values'].get('b1f0'))
     
##Using record id     
    #record_id = "0a9122f8-6b31-4a74-bd89-63147c5c2b37"
    #record_url = f"https://api.fulcrumapp.com/api/v2/records/{record_id}.json"
    #record_response = requests.get(record_url, headers=headers)
    #record = record_response.json()['record']
    
    #print(" before update :", record["form_values"].get("usgs_elevation"))
    #print(type(record["form_values"].get("usgs_elevation")))
    #record["form_values"]["usgs_elevation"] = 10
    #update_response = requests.put(record_url, headers=headers, json={'record': record})
    #print("response", update_response)
    #print(" after update :", record["form_values"].get("usgs_elevation"))
    #print(type(record["form_values"].get("usgs_elevation")))
    
     #print(" elevation req number only before update:", testrecord["form_values"].get("elevation_required_numbers_only"))  #test code
     #testrecord["form_values"]["elevation_required_numbers_only"] = 20
     #push the update
     #print(" after update :", testrecord["form_values"].get("elevation_required_numbers_only"))


    for record in data["records"][:1]: 
     #print("Default elevation :", record["altitude"])  
  
     lat = record["latitude"]
     lon = record["longitude"]
     #print("when latitude is ", lat, "and logitude is ", lon)
     #print("Vertical Accuracy: ", record["vertical_accuracy"], ", Horizontal Accuracy: ", record["horizontal_accuracy"])
     
     if lat and lon: #(if lat and lon not none)
      elevation = get_from_usgs(lat, lon)
      
      if elevation is not None:
          print(f"USGS Elevation: {elevation} meters")
          #print("Updating elevation in Fulcrum...")
          #record["form_values"]["usgs_elevation"] = elevation #updates values in fulcrum 
          #print(record["form_values"].get("usgs_elevation"))
      else:
          print("Skipping record",record["id"], "due to elevation error.")      
     
   