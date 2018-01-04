# kraken-python
Unofficial Python3 library for the Kraken API

While there are existing python libraries for most cryptocurrency exchanges,
each exchange has a different api. This results on a lot of disparities on how libraries are implemented, and as such each one has a very different usage, and return values. This library attempts to set a standardized way for exchange libraries.

Supported exchanges:

* [Bitfinex](https://github.com/Vanclief/bitfinex-python)
* [Kraken](https://github.com/Vanclief/kraken-python)
* [Bitso](https://github.com/Vanclief/bitso-python)
* [Gdax](https://github.com/Vanclief/gdax-python)
* [Gemini](https://github.com/Vanclief/gemini-python)

*Note:* While I attempt to avoid making breaking changes, this library is still work in progress (WIP), use under your own risk.

## TODO

- [X]  Add public endpoints
- [ ]  Add private endpoints
- [ ]  Upload to pip

## Instalation
Install from source with:

```py
python setup.py install
```

### Requirements

* Python 3.3+

## Usage

Some of the most relevant endpoints:

```py
from krakenpy.kraken import Kraken

client = Kraken()

# Get ticker
client.ticker('btcusd')
ticker = {
  "mid": 333.985,
  "bid": 333.98,
  "ask": 333.99,
  "last_price": 333.99,
  "low": 321.1, # Not supported by some exchanges
  "high": 345.9, # Not supported by some exchanges
  "volume": 5957.11914015,
  "timestamp": 1447533963.0
}

# Get orderbook
client.orderbook('btcusd')
orderboook = {
  "bids": [
    {
      "price": 295.96,
      "amount": 4.39088265,
      "timestamp": 1420674445.201
    } ...
  ],
   "asks": [
    {
       "price": 295.97,
       "amount": 25.23542881,
       "timestamp": 1420674445.201
    } ...
   ]
}

# Get trades
client.trades('btcusd')
trades = expected_response = [
  {
    "timestamp": 1415398768.0,
    "tid": 74,
    "price": 10.0,
    "amount": 0.01,
    "exchange": "Kraken",
    "type": "buy"
  } ...
]

# Get symbols
client.symbols()
symbols = ["bchusd", "ltceur", "ltcusd"]
```

## Contribution

1. Discuss changes by creating a issue.
2. Fork the project.
3. Create a branch with fix, or feature with it's proper tests.
4. Create a PR
