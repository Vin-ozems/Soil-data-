import requests
import pandas as pd
import csv

api_endpoint = "http://api.agromonitoring.com/agro/1.0/polygons"
API_KEY = "c1237d299ac28906f12626e915c02a3a"

params = {
    "appid": API_KEY,
}

response = requests.get(url=api_endpoint,params=params)
response.raise_for_status()
data = response.json()

def fetch_poly_id(id):
    soil_api_endpoint = "http://api.agromonitoring.com/agro/1.0/soil"  
    soil_params = {
        "appid": API_KEY,
        "polyid": id
    }                       

    response1 = requests.get(url=soil_api_endpoint, params=soil_params)
    response1.raise_for_status()
    data1 = response1.json()
    return data1
    #print(data1)

# Ask how many records to process
no = int(input("How many polygons to fetch? "))
first_record = True


# Create/open the CSV file
with open("polygon_data.csv", mode="w", newline="", encoding="utf-8") as file:
    for i in range(no):
        poly_id = data[i]["id"]
        result = fetch_poly_id(poly_id)
        if first_record:
            headers = result.keys()
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            first_record = False
        print(result)  # Optional: show in console
        writer.writerow(result)  # write to CSV
