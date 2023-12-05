import krakenex
import config

class KrakenAPI:
    def __init__(self):
        self.api = krakenex.API(key=config.KRAKEN_API_KEY, secret=config.KRAKEN_API_SECRET)

    def get_asset_info(self):
        return self.api.query_public('Assets')

    def get_ohlc_data(self, pair, interval=1, since=None):
        # Fetch OHLC data
        return self.api.query_public('OHLC', {'pair': pair, 'interval': interval, 'since': since})

# Example usage
# kraken_api = KrakenAPI()
# print(kraken_api.get_asset_info())
# print(kraken_api.get_ohlc_data('BTCUSD'))
