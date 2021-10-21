import os
import requests
import datetime

today = datetime.date.today()
tommorow = today + datetime.timedelta(days=1).strftime("%d/%m/%Y")
six_month_from_now = today + datetime.timedelta(days=6*30).strftime("%d/%m/%Y")
today = today.strftime("%d/%m/%Y")

MY_FLY_FROM = "LON"



apikey_kiwi = os.environ["apikey_kiwi"]

search_cheap_price_endpoint = "https://tequila-api.kiwi.com/v2/search"

headers = {
    "apikey": apikey_kiwi
}

class FlightData:
    #This class is responsible for structuring the flight data.
    # pass
    def __init__(self, city_name):
        self.query = {
            "fly_to": city_name,
            "location_types": "city",
            "fly_from": MY_FLY_FROM,
            "date_from": tommorow,
            "date_to": six_month_from_now,
            "flight_type": "round",
            "max_stopovers": 0





        }
        self.cheap_flight_price_search()

    def cheap_flight_price_search(self):
        response = requests.get(url=search_cheap_price_endpoint, params=self.query, headers=headers)


