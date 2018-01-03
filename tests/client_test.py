from krakenpy.kraken import Kraken
import httpretty

client = Kraken()

TICKER_URL = 'https://api.kraken.com/0/public/Ticker'
ORDERS_URL = 'https://api.kraken.com/0/public/Depth'
TRADES_URL = 'https://api.kraken.com/0/public/Trades'
SYMBOLS_URL = 'https://api.kraken.com/0/public/AssetPairs'
SYMBOL_DETAILS = 'https://api.kraken.com/0/public/AssetPairs'


def set_time_endpoint():

    mock_body = (
            '{"error":[],"result":{"unixtime":1514919213,"rfc1123":"Tue,' +
            '  2 Jan 18 18:53:33 +0000"}}'
            )

    mock_url = 'https://api.kraken.com/0/public/Time'
    mock_status = 200

    httpretty.register_uri(
            httpretty.GET, mock_url, body=mock_body, status=mock_status
            )


def test_should_have_correct_url():
    k = Kraken()
    assert k.api_base == 'https://api.kraken.com/0/'


def test_should_have_api_key():
    k = Kraken('974554aed089', '2976be9e189d')
    assert k.api_key == '974554aed089'


def test_should_have_secret_key():
    k = Kraken('974554aed089', '2976be9e189d')
    assert k.api_secret == '2976be9e189d'


@httpretty.activate
def test_should_return_ticker():

    set_time_endpoint()

    mock_symbol = 'btcusd'
    mock_body = (
            '{"error":[],"result":{"XXBTZUSD":{"a":["14429.00000","1",' +
            '"1.000"],"b":["14427.80000","2","2.000"],"c":["14427.80000",' +
            '"0.84801287"],"v":["2146.80696649","2726.69706158"],' +
            '"p":["13728.68641","13705.40692"],"t":[13783,18274],' +
            '"l":["13088.80000","13088.80000"],"h":["14427.80000"' +
            ',"14427.80000"],"o":"13506.10000"}}}'
            )
    mock_url = TICKER_URL + '?pair=XBTUSD'
    mock_status = 200

    httpretty.register_uri(
            httpretty.GET, mock_url, body=mock_body, status=mock_status
            )

    expected_response = {
            "mid": 14428.4,
            "bid": 14427.8,
            "ask": 14429.0,
            "last_price": 14427.8,
            "low": 13088.8,
            "high": 14427.8,
            "volume": 2726.69706158,
            "timestamp": 1514919213
            }

    response = client.ticker(mock_symbol)
    assert expected_response == response[1]


@httpretty.activate
def test_should_return_orderbook():

    mock_symbol = 'btcusd'
    mock_body = (
            '{"error":[],"result":{"XXBTZUSD":{"asks":[["14432.00000",' +
            '"3.900",1514918034]],' +
            '"bids":[["14430.00000","0.997",1514918017]]}}}'
            )
    mock_url = ORDERS_URL + '?pair=XBTUSD'
    mock_status = 200

    httpretty.register_uri(
            httpretty.GET, mock_url, body=mock_body, status=mock_status
            )

    expected_response = {
            "asks": [
                {
                    "price": 14432.0,
                    "amount": 3.900,
                    "timestamp": 1514918034.0
                    }
                ],
            "bids": [
                {
                    "price": 14430.0,
                    "amount": 0.997,
                    "timestamp": 1514918017.0
                    }
                ]
            }

    response = client.orderbook(mock_symbol)
    assert expected_response == response[1]


@httpretty.activate
def test_should_return_trades():

    mock_symbol = 'btcusd'
    mock_body = (
            '{"error":[],"result":{"XXBTZUSD":[["13903.40000","0.02161302",' +
            '1514914305.0079,"s","l",""]], "last":"1514918068359220939"}}'
            )
    mock_url = TRADES_URL + '?pair=XBTUSD'
    mock_status = 200

    httpretty.register_uri(
            httpretty.GET, mock_url, body=mock_body, status=mock_status
            )

    expected_response = [
            {   "timestamp": 1514914305.0079, "tid": 1514918068359220939,
                "price": 13903.4, "amount": 0.02161302,
                "exchange": "kraken", "type": "sell"}
            ]

    response = client.trades(mock_symbol)
    assert expected_response == response[1]



@httpretty.activate
def test_should_return_symbols():

    mock_body = (
            '{"error":[],"result":{"BCHEUR":{"altname":"BCHEUR",' +
            '"aclass_base":"currency","base":"BCH",' +
            '"aclass_quote":"currency","quote":"ZEUR","lot":"unit",' +
            '"pair_decimals":1,"lot_decimals":8,"lot_multiplier":1,' +
            '"leverage_buy":[],"leverage_sell":[],"fees":[[0,0.26],' +
            '[50000,0.24],[100000,0.22],[250000,0.2],[500000,0.18],' +
            '[1000000,0.16],[2500000,0.14],[5000000,0.12],[10000000,0.1]]' +
            ',"fees_maker":[[0,0.16],[50000,0.14],[100000,0.12]' +
            ',[250000,0.1],[500000,0.08],[1000000,0.06],[2500000,0.04]' +
            ',[5000000,0.02],[10000000,0]],"fee_volume_currency":"ZUSD"' +
            ',"margin_call":80,"margin_stop":40},' +
            '"BCHUSD":{"altname":"BCHUSD","aclass_base":"currency",' +
            '"base":"BCH","aclass_quote":"currency","quote":"ZUSD"' +
            ',"lot":"unit","pair_decimals":1,"lot_decimals":8' +
            ',"lot_multiplier":1,"leverage_buy":[],"leverage_sell":[]' +
            ',"fees":[[0,0.26],[50000,0.24],[100000,0.22],[250000,0.2]' +
            ',[500000,0.18],[1000000,0.16],[2500000,0.14],[5000000,0.12]' +
            ',[10000000,0.1]],"fees_maker":[[0,0.16],[50000,0.14]' +
            ',[100000,0.12],[250000,0.1],[500000,0.08],[1000000,0.06]' +
            ',[2500000,0.04],[5000000,0.02],[10000000,0]]' +
            ',"fee_volume_currency":"ZUSD","margin_call":80' +
            ',"margin_stop":40}}}'
            )

    mock_url = SYMBOLS_URL
    mock_status = 200

    httpretty.register_uri(
            httpretty.GET, mock_url, body=mock_body, status=mock_status
            )

    expected_response = ["bcheur", "bchusd"]

    response = client.symbols()
    assert expected_response == response[1]


@httpretty.activate
def test_should_return_symbol_details():

    mock_body = (
        '{"error":[],"result":{"BCHEUR":{"altname":"BCHEUR",' +
        '"aclass_base":"currency","base":"BCH",' +
        '"aclass_quote":"currency","quote":"ZEUR","lot":"unit",' +
        '"pair_decimals":1,"lot_decimals":8,"lot_multiplier":1,' +
        '"leverage_buy":[],"leverage_sell":[],"fees":[[0,0.26],' +
        '[50000,0.24],[100000,0.22],[250000,0.2],[500000,0.18],' +
        '[1000000,0.16],[2500000,0.14],[5000000,0.12],[10000000,0.1]]' +
        ',"fees_maker":[[0,0.16],[50000,0.14],[100000,0.12]' +
        ',[250000,0.1],[500000,0.08],[1000000,0.06],[2500000,0.04]' +
        ',[5000000,0.02],[10000000,0]],"fee_volume_currency":"ZUSD"' +
        ',"margin_call":80,"margin_stop":40},' +
        '"BCHUSD":{"altname":"BCHUSD","aclass_base":"currency",' +
        '"base":"BCH","aclass_quote":"currency","quote":"ZUSD"' +
        ',"lot":"unit","pair_decimals":1,"lot_decimals":8' +
        ',"lot_multiplier":1,"leverage_buy":[],"leverage_sell":[]' +
        ',"fees":[[0,0.26],[50000,0.24],[100000,0.22],[250000,0.2]' +
        ',[500000,0.18],[1000000,0.16],[2500000,0.14],[5000000,0.12]' +
        ',[10000000,0.1]],"fees_maker":[[0,0.16],[50000,0.14]' +
        ',[100000,0.12],[250000,0.1],[500000,0.08],[1000000,0.06]' +
        ',[2500000,0.04],[5000000,0.02],[10000000,0]]' +
        ',"fee_volume_currency":"ZUSD","margin_call":80' +
        ',"margin_stop":40}}}'
            )

    mock_url = SYMBOL_DETAILS
    mock_status = 200

    httpretty.register_uri(
            httpretty.GET, mock_url, body=mock_body, status=mock_status
            )

    expected_response = [
            {
                "pair": "bcheur", "price_precision": 8,
                "maximum_order_size": 0.0, "minimum_order_size": 0.0,
                "expiration": "NA"
                },
            {
                "pair": "bchusd", "price_precision": 8,
                "maximum_order_size": 0.0, "minimum_order_size": 0.0,
                "expiration": "NA"
                }
            ]
    response = client.symbol_details()
    assert expected_response == response[1]
