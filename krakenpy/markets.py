from krakenpy.requester import Requester
import krakenpy.helpers as helpers

TICKER_URL = "public/Ticker/"
ORDERS_URL = "public/Depth/"
TRADES_URL = "public/Trades/"
SYMBOLS_URL = "public/AssetPairs"
SYMBOL_DETAILS = "public/AssetPairs"


class Market(object):

    def __init__(self, api_base):
        self.r = Requester(api_base)

    def get_ticker(self, symbol):

        endpoint = TICKER_URL + symbol
        status, response = self.r.get(endpoint)

        if status != 200:
            return status, response

        return status, helpers.dict_to_float(response)


    def get_orderbook(self, symbol):

        endpoint = ORDERS_URL + symbol
        status, response = self.r.get(endpoint)

        if status != 200:
            return status, response

        for order_type in response.keys():
            for order in response[order_type]:
                for key, value in order.items():
                    order[key] = float(value)

        return status, response

    def get_trades(self, symbol):
        endpoint = TRADES_URL + symbol
        status, response = self.r.get(endpoint)

        if status != 200:
            return status, response

        return status, helpers.list_dict_to_float(response)


    def get_symbols(self):
        endpoint = SYMBOLS_URL
        return self.r.get(endpoint)

    def get_symbol_details(self):
        endpoint = SYMBOL_DETAILS
        status, response = self.r.get(endpoint)

        if status != 200:
            return status, response

        return status, helpers.list_dict_to_float(response)
