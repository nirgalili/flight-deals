import os
import requests
import datetime

today = datetime.date.today()
tommorow = today + datetime.timedelta(days=1)
six_month_from_now = today + datetime.timedelta(days=6*30)
today = today.strftime("%d/%m/%Y")
tommorow = tommorow.strftime("%d/%m/%Y")
six_month_from_now = six_month_from_now.strftime("%d/%m/%Y")



MY_FLY_FROM = "LON"



apikey_kiwi = os.environ["apikey_kiwi"]

search_cheap_price_endpoint = "https://tequila-api.kiwi.com/v2/search"

headers = {
    "apikey": apikey_kiwi
}

class FlightData:
    #This class is responsible for structuring the flight data.
    # pass
    def __init__(self, iataCode):
        self.query = {
            "fly_to": iataCode,
            "location_types": "city",
            "fly_from": MY_FLY_FROM,
            "date_from": tommorow,
            "date_to": six_month_from_now,
            "flight_type": "round",
            "max_stopovers": 0,
            "curr": "GBP",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "limit": 1





        }
        self.cheap_flight_price_search()

    def cheap_flight_price_search(self):
        response = requests.get(url=search_cheap_price_endpoint, params=self.query, headers=headers)
        resaults = response.json()
        print(resaults["data"][0])
        self.price_of_flight = resaults["data"][0]["price"]
        self.city_flight_from = resaults["data"][0]["cityFrom"]
        self.city_flight_to = resaults["data"][0]["cityTo"]
        self.airport_iataCode_flight_from = resaults["data"][0]["flyFrom"]
        self.airport_iataCode_flight_to = resaults["data"][0]["flyTo"]
        local_departure_to = resaults["data"][0]["route"][0]["local_departure"]
        self.local_date_flight_to = local_departure_to.split("T")[0]

        local_departure_from = resaults["data"][0]["route"][1]["local_departure"]
        self.local_date_flight_from = local_departure_from.split("T")[0]


        print(f"{self.city_flight_to}: £{self.price_of_flight}")


# my_flight_data = FlightData("PAR")
