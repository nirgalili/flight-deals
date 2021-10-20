class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    # pass
    def __init__(self, iataCode):
        self.code = iataCode

    def get_update_iataCode(self):
        self.code = "TESTING"