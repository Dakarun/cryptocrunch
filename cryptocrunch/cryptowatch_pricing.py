import json

from datetime import datetime
from math import floor

import requests


class CryptowatchPricingClient:
    # TODO: Implement more methods to pull data. e.g. from specifc exchanges
    """
    Client which hits the Cryptowatch API and parses the results into a list of lists
    """
    def __init__(self):
        self.base_endpoint = 'https://api.cryptowat.ch'

    def get_all_prices(self):
        # TODO: handle error codes
        # TODO: track budget and stop making requests for a period if there is no budget
        endpoint = f"{self.base_endpoint}/markets/prices"
        response = requests.get(endpoint)
        request_timestamp = floor(datetime.now().timestamp())
        prepared_response = self.process_prices(response.text, request_timestamp)

        return prepared_response

    def process_prices(self, payload, timestamp):
        response = json.loads(payload)
        if response['allowance']:
            print(f"Remaining budget: {str(response['allowance']['remaining'])}")
        prices = []
        for identifier, price in response['result'].items():
            market, exchange, pair = identifier.split(':')
            # TODO: Setup a more comprehensive way to add quotes to strings
            prices.append([f"'{exchange}'", f"'{pair}'", price, timestamp, f"'{self.base_endpoint}'"])
        return prices

    def mock_insert(self):
        """
        Method used for debugging parsing, should be converted into a test
        """
        with open('sample.json', 'r') as f:
            jayson = f.read()
        request_timestamp = floor(datetime.now().timestamp())
        prepared_response = self.process_prices(jayson, request_timestamp)
        return prepared_response
