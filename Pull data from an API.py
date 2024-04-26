import requests
import json

#example 1
#response_API = requests.get('https://api.covid19india.org/state_district_wise.json')
#print(response_API.status_code)
#data = response_API.text
#print(data)
#parse_json = json.loads(data)
#print(parse_json)
#active_case = parse_json['Andaman and Nicobar Islands']['districtData']['South Andaman']['active']
#print("Active cases in South Andaman:", active_case)


#example 2
response_API = requests.get('https://gmail.googleapis.com/$discovery/rest?version=v1')
#print(response_API.status_code)
data = response_API.text
parse_json = json.loads(data)
info = parse_json['description']
print("Info about API:\n", info)
key = parse_json['parameters']['key']['description']
print("\nDescription about the key:\n",key)