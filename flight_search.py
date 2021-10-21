import os
import requests
apikey_kiwi = os.environ["apikey_kiwi"]
get_iataCode_from_kiwi_endpoint = "https://tequila-api.kiwi.com/locations/query"
# print(apikey_kiwi)

headers = {
    "apikey": apikey_kiwi
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    # pass
    def __init__(self, city_name):
        self.query = {
            "term": city_name,
            "location_types": "city",

        }
        self.get_update_iataCode()


    def get_update_iataCode(self):
        # self.code = "TESTING"
        response = requests.get(url=get_iataCode_from_kiwi_endpoint, params=self.query, headers=headers)
        resaults = response.json()["locations"]
        self.code = resaults[0]["code"]
        # return code

# my_flight_search = FlightSearch("Paris")
# print(my_flight_search.code)