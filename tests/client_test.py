from krakenpy.kraken import Kraken
import httpretty

client = Kraken()

TICKER_URL = 'https://api.kraken.com/0/public/Ticker'
ORDERS_URL = 'https://api.kraken.com/0/public/Depth'
TRADES_URL = 'https://api.kraken.com/0/public/Trades'
SYMBOLS_URL = 'https://api.kraken.com/0/public/AssetPairs'
SYMBOL_DETAILS = 'https://api.kraken.com/0/public/AssetPairs'


def test_should_have_correct_url():
    k = Kraken()
    assert k.api_base == 'https://api.kraken.com/'


def test_should_have_api_key():
    k = Kraken('974554aed089', '2976be9e189d')
    assert k.api_key == '974554aed089'


def test_should_have_secret_key():
    k = Kraken('974554aed089', '2976be9e189d')
    assert k.api_secret == '2976be9e189d'


@httpretty.activate
def test_should_return_ticker():

    mock_symbol = 'btcusd'
    mock_body = (
            '{"mid":"244.755","bid":"244.75","ask":"244.76",' +
            '"last_price":"244.82","low":"244.2", "high":"248.19",' +
            '"volume": "7842.11542563", "timestamp":"1395552658.339936691"}')
    mock_url = TICKER_URL + mock_symbol
    mock_status = 200

    httpretty.register_uri(
            httpretty.GET, mock_url, body=mock_body, status=mock_status
            )

    expected_response = {
            "mid": 244.755,
            "bid": 244.75,
            "ask": 244.76,
            "last_price": 244.82,
            "low": 244.2,
            "high": 248.19,
            "volume": 7842.11542563,
            "timestamp": 1395552658.339936691
            }

    response = client.ticker(mock_symbol)
    assert expected_response == response[1]


@httpretty.activate
def test_should_return_orderbook():

    mock_symbol = 'btcusd'
    mock_body = (
            '{"bids":[{"price":"562.2601", "amount":"0.985", ' +
            '"timestamp":"1395567556.0"}],"asks":[{"price":"563.001", ' +
            '"amount":"0.3","timestamp":"1395532200.0"}]}')
    mock_url = ORDERS_URL + mock_symbol
    mock_status = 200

    httpretty.register_uri(
            httpretty.GET, mock_url, body=mock_body, status=mock_status
            )

    expected_response = {
            "bids": [
                {
                    "price": 562.2601,
                    "amount": 0.985,
                    "timestamp": 1395567556.0
                    }
                ],
            "asks": [
                {
                    "price": 563.001,
                    "amount": 0.3,
                    "timestamp": 1395532200.0
                    }
                ]
            }

    response = client.orderbook(mock_symbol)
    assert expected_response == response[1]


@httpretty.activate
def test_should_return_trades():

    mock_symbol = 'btcusd'
    mock_body = (
            '[{ "timestamp":1444266681, "tid":11988919, "price":"244.8", ' +
            '"amount":"0.03297384", "exchange":"bitfinex", "type":"sell"}]')
    mock_url = TRADES_URL + mock_symbol
    mock_status = 200

    httpretty.register_uri(
            httpretty.GET, mock_url, body=mock_body, status=mock_status
            )

    expected_response = [
            {"timestamp": 1444266681, "tid": 11988919, "price": 244.8,
                "amount": 0.03297384, "exchange": "bitfinex", "type": "sell"}
            ]

    response = client.trades(mock_symbol)
    assert expected_response == response[1]



@httpretty.activate
def test_should_return_symbols():

    mock_body = '["btcusd", "ltcusd", "ltcbtc"]'
    mock_url = SYMBOLS_URL
    mock_status = 200

    httpretty.register_uri(
            httpretty.GET, mock_url, body=mock_body, status=mock_status
            )

    expected_response = ["btcusd", "ltcusd", "ltcbtc"]

    response = client.symbols()
    assert expected_response == response[1]


@httpretty.activate
def test_should_return_symbol_details():

    mock_body = (
            '[{ "pair":"btcusd", "price_precision":5,' +
            '"initial_margin":"30.0", "minimum_margin":"15.0",' +
            '"maximum_order_size":"2000.0", "minimum_order_size":"0.01",' +
            '"expiration":"NA" },{ "pair":"ltcusd", "price_precision":5,' +
            '"initial_margin":"30.0", "minimum_margin":"15.0",' +
            '"maximum_order_size":"5000.0", "minimum_order_size":"0.1", ' +
            '"expiration":"NA" },{ "pair":"ltcbtc", "price_precision":5,' +
            '"initial_margin":"30.0", "minimum_margin":"15.0",' +
            '"maximum_order_size":"5000.0", "minimum_order_size":"0.1",' +
            '"expiration":"NA"}]')
    mock_url = SYMBOL_DETAILS
    mock_status = 200

    httpretty.register_uri(
            httpretty.GET, mock_url, body=mock_body, status=mock_status
            )

    expected_response = [
            {
                "pair": "btcusd", "price_precision": 5,
                "initial_margin": 30.0, "minimum_margin": 15.0,
                "maximum_order_size": 2000.0, "minimum_order_size": 0.01,
                "expiration": "NA"
                },
            {
                "pair": "ltcusd", "price_precision": 5,
                "initial_margin": 30.0, "minimum_margin": 15.0,
                "maximum_order_size": 5000.0, "minimum_order_size": 0.1,
                "expiration": "NA"
                },
            {
                "pair": "ltcbtc", "price_precision": 5,
                "initial_margin": 30.0, "minimum_margin": 15.0,
                "maximum_order_size": 5000.0, "minimum_order_size": 0.1,
                "expiration": "NA"
                }
            ]
    response = client.symbol_details()
    assert expected_response == response[1]
