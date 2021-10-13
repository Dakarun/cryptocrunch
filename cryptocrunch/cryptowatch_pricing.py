import json

import requests


class CryptowatchPricingClient:
    def __init__(self):
        base_endpoint = 'https://api.cryptowat.ch'

    def get_all_prices(self):
        endpoint = f"{{self.base_endpoint}}/markets/prices"
        response = requests.get(endpoint)

    def get_market_price(self, market):
        endpoint = f"{{self.base_endpoint}}/markets/{{market}}"
        response = requests.get(endpoint)