#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from flight_search import FlightSearch

wish_deals_endpoint = "https://api.sheety.co/530a49192b31d09ac9d82f6490293373/myFlightDeals/prices"

response = requests.get(url=wish_deals_endpoint)
response_data = response.json()
print("____________________________________________________")
print(response.text)
print("____________________________________________________")
sheet_data = response_data["prices"]
print(sheet_data)


for i in sheet_data:
    iataCode = i["iataCode"]
    if iataCode =="":
        my_flight_search = FlightSearch(iataCode)
        my_flight_search.get_update_iataCode()
        update_iataCode = my_flight_search.code
        # print(update_iataCode)
        i["iataCode"] = update_iataCode

print("____________________________________________________")
print(sheet_data)
