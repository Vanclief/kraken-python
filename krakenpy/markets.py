from krakenpy.requester import Requester
import krakenpy.helpers as helpers

TICKER_URL = "public/Ticker"
ORDERS_URL = "public/Depth"
TRADES_URL = "public/Trades"
SYMBOLS_URL = "public/AssetPairs"
SYMBOL_DETAILS = "public/AssetPairs"


class Market(object):

    def __init__(self, api_base):
        self.r = Requester(api_base)

    def get_ticker(self, symbol):

        endpoint = TICKER_URL + helpers.symbol_to_request(symbol)
        status, response = self.r.get(endpoint)

        if status != 200:
            return status, response['error']

        return status, helpers.dict_to_float(response)


    def get_orderbook(self, symbol):

        endpoint = ORDERS_URL + helpers.symbol_to_request(symbol)
        status, response = self.r.get(endpoint)

        if status != 200:
            return status, response['error']

        for order_type in response.keys():
            for order in response[order_type]:
                for key, value in order.items():
                    order[key] = float(value)

        return status, response

    def get_trades(self, symbol):
        endpoint = TRADES_URL + helpers.symbol_to_request(symbol)
        status, response = self.r.get(endpoint)

        if status != 200:
            return status, response['error']

        parsed_response = []

        tid = response['result']['last']

        for key, values in response['result'].items():
            if key != 'last':
                for value in values:
                    print(key, value)
                    p = {}
                    p['timestamp'] = float(value[2])
                    p['tid'] = int(tid)
                    p['price'] = float(value[0])
                    p['amount'] = float(value[1])
                    p['exchange'] = 'kraken'
                    p['type'] = helpers.stringify_trade_type(value[3])

                    parsed_response.append(p)

        return status, parsed_response


    def get_symbols(self):
        endpoint = SYMBOLS_URL
        status, response = self.r.get(endpoint)

        if status != 200:
            return status, response['error']

        parsed_response = []

        for symbol in response['result']:
            parsed_response.append(symbol.lower())

        return status, parsed_response

    def get_symbol_details(self):
        endpoint = SYMBOL_DETAILS
        status, response = self.r.get(endpoint)

        if status != 200:
            return status, response['error']

        parsed_response = []

        for symbol in response['result']:
            p = {}
            p['pair'] = symbol.lower()
            p['price_precision'] = 8
            p['maximum_order_size'] = float(0)
            p['minimum_order_size'] = float(0)
            p['expiration'] = "NA"
            parsed_response.append(p)


        return status, parsed_response
