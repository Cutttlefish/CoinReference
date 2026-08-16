COIN_TYPES = ((25,"Q"), (10, "D"), (5,"N"), (1,"P"))


def calculate_change(cents, coins=COIN_TYPES):
    """Return the minimum-coin representation of `cents` as a string of coin-face characters.

    Recurses through `coins` from largest to smallest denomination (greedy)
    """
    if cents == 0:
        return ""
    value, coin = coins[0]
    count, remainder = divmod(cents, value)
    # drop current coin-face, recurse on the rest
    return coin * count + calculate_change(remainder, coins[1:])
   

