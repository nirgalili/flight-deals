import requests
import os
from twilio.rest import Client
from flight_data import FlightData

twilio_sid = os.environ["twilio_sid"]
twilio_token = os.environ["twilio_token"]
# print(twilio_sid)


class NotificationManager():
    #This class is responsible for sending notifications with the deal flight details.

    def __init__(self, flight_data: FlightData):
        self.flight_data = flight_data
        self.send_sms()

    def send_sms(self):
        client = Client(twilio_sid, twilio_token)
        message = client.messages \
            .create(
            body=f"Low price alert! Only £{self.flight_data.price_of_flight}"
                 f"to fly from {self.flight_data.city_flight_from}-{self.flight_data.airport_iataCode_flight_from}"
                 f"to {self.flight_data.city_flight_to}-{self.flight_data.airport_iataCode_flight_to},"
                 f"from {self.flight_data.local_date_flight_from} to {self.flight_data.local_date_flight_to}.",
            from_="+19039450694",
            to="+972545898999"
        )
        print(message.status)










