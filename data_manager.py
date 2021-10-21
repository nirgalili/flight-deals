import requests

update_iataCode_in_sheet_endpoint = "https://api.sheety.co/530a49192b31d09ac9d82f6490293373/myFlightDeals/prices/"


class DataManager:

    # This class is responsible for talking to the Google Sheet.

    def __init__(self, row):
        self.code = row["iataCode"]
        self.id = row["id"]
        self.json_row = {
            "price": row
        }

        self.update_iatacode_in_sheety()

    def update_iatacode_in_sheety(self):
        requests.put(url=f"{update_iataCode_in_sheet_endpoint}{self.id}", json=self.json_row)
