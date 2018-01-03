def dict_to_float(d):
    """
    Converts all strings to floats from a dict
    """
    if type(d) is dict:
        for key, value in d.items():
            if type(value) is str:
                try:
                    d[key] = float(value)
                except ValueError:
                    d[key] = str(value)

    return d


def list_dict_to_float(l):
    """
    Applies dict_to_float to all elements from a list
    """
    for d in l:
        d = dict_to_float(d)

    return l

def symbol_to_request(s):
    """
    Converts from btcusd to ?pair=XBTUSD
    """
    if s[:3] == 'btc':
        s = 'XBT' + s[3:].upper()
    return "?pair={0}".format(s)

def stringify_trade_type(s):
    """
    S -> Sell, B -> Buy
    """
    if s == 's':
        return 'sell'

    return 'buy'
