import os
import requests
from dotenv import load_dotenv

def get_from_fulcrum():
    print("Getting elevations from Fulcrum...")
    
    load_dotenv()
    API_KEY = os.getenv("FULCRUM_API_KEY")
    FORM_ID = os.getenv("FORM_ID")
    TEST_FORM_ID = os.getenv("TEST_FORM_ID") #test code
    
    fulcrumURL = f"https://api.fulcrumapp.com/api/v2/records?form_id={FORM_ID}"
    testURL = f"https://api.fulcrumapp.com/api/v2/records?form_id={TEST_FORM_ID}" #test code
    
    headers = {
    "X-ApiToken": API_KEY,
    "Accept": "application/json"
    }
    response = requests.get(fulcrumURL, headers=headers)
    response.raise_for_status()    
    data = response.json()
    
    test_response = requests.get(testURL, headers=headers) #test code
    test_response.raise_for_status()  #test code
    testdata = test_response.json() #test code
    
    return headers, data, testdata
