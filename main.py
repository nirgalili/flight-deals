#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from flight_search import FlightSearch
from data_manager import DataManager

wish_deals_endpoint = "https://api.sheety.co/530a49192b31d09ac9d82f6490293373/myFlightDeals/prices"

response = requests.get(url=wish_deals_endpoint)
response_data = response.json()
# print("____________________________________________________")
# print(response.text)
# print("____________________________________________________")
sheet_data = response_data["prices"]
# print(sheet_data)


for row_in_sheety_table in sheet_data:
    iataCode = row_in_sheety_table["iataCode"]
    if iataCode =="":
        my_flight_search = FlightSearch(iataCode)
        my_flight_search.get_update_iataCode()
        update_iataCode = my_flight_search.code
        # print(update_iataCode)
        row_in_sheety_table["iataCode"] = update_iataCode
        my_data_manager = DataManager(row_in_sheety_table)


# print("____________________________________________________")
# print(sheet_data)
