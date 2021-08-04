#!/bin/python3

import argparse 
import json
import requests

#ip lookup using ip-api.com API

parser = argparse.ArgumentParser()

parser.add_argument("target", help="Specify the target using IP address or url or hostname")

args = parser.parse_args()

target = args.target

url = f"http://ip-api.com/json"
fields=["query", "reverse", "status", "message", "country", "countryCode", "region", "regionName",
        "city", "zip", "lat", "lon", "timezone", "isp", "org", "as"]
try:
    response = requests.get(f"{url}/{target}?fields={','.join(fields)}").json()

    if response["status"] == "success":
        print() 
        for item in response.keys():
            if item not in ("status", "message"):
                if response[item]:
                    print(f"{item}: {response[item]}")

    else:
        print(f"!!! {response['message']}")

except:
    print("Connection Error")

