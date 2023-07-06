import requests
import pandas as pd
import json

from pandas import json_normalize


base_url = 'https://npiregistry.cms.hhs.gov/api/'

def fetch_npi_data(npi):
    # Construct the URL for the API request
    #url = base_url + 'version=2.1'
    params = {
        'number': npi,
        'version': '2.1'
    }
    
    url = 'https://npiregistry.cms.hhs.gov/api/?version=2.1'
    try:
        # Send the API request
        response = requests.get(url, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            # Process the data as per your requirements
            return data
        else:
            # Request was not successful, handle the error
            print('Error:', response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        # Request encountered an exception, handle the error
        print('Error:', str(e))
        return None