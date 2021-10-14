from flask import current_app

from cryptocrunch.scheduler import scheduler
from cryptocrunch.cryptowatch_pricing import CryptowatchPricingClient
from cryptocrunch.pricingstore import PricingStore

cryptowatch_client = CryptowatchPricingClient()
pricing_store = PricingStore()


@scheduler.task('interval', id='get_all_prices', seconds=60)
def get_all_prices():
    """Get all prices and store them into the db every minute"""
    records = cryptowatch_client.get_all_prices()
    pricing_store.insert(records)
