import json

import requests


class PricingClient:
    def __init__(self):
        pass

    def get_price(self):
        endpoint = "https://api.cryptowat.ch/markets/prices"
        response = requests.get(endpoint)