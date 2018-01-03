# kraken-wrapper

While there are existing python libraries for most cryptocurrency exchanges,
each exchange has a different api. This results on a lot of disparities on how libraries are implemented, and as such each one has a very different usage, and return values. This library attempts to set a standardized way for exchange libraries.

Planned exchanges:

- [X] [Bitfinex](https://github.com/Vanclief/bitfinex-python)
- [X] [Kraken](https://github.com/Vanclief/kraken-python)
- [X] [Bitso](https://github.com/Vanclief/bitso-python)
- [ ] [Gdax/Coinbase](https://github.com/Vanclief/gdax-python)
- [ ] [Gemini](https://github.com/Vanclief/gemini-python)

*Note:* While I attempt to avoid making breaking changes, this library is still 
work in progress (WIP), use under your own risk.


## Instalation
Install from source with:

```py
python setup.py install
```

### Requirements

* Python 3.3+

## Usage

```py
from krakenpy.kraken import Kraken

k = Kraken()

k.ticker('btcusd')
```

## TODO

- [X]  Add tests
- [X]  Add public endpoints
- [X]  Add requirements, setup, etc.
- [ ]  Add private endpoints
- [ ]  Unify interface for trading endpoints
- [ ]  Upload to pip

## Contribution

1. Discuss changes by creating a issue.
2. Fork the project.
3. Create a branch with fix, or feature with it's proper tests.
4. Create a PR
