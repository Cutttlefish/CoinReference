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
   

def make_change_reference(cents_counter):
    """Build and return a "value | coins" reference table for every cent value from 1 to `cents_counter`."""
    return ("\n".join(map(lambda x: f"{x} | {calculate_change(x)}", range(1, cents_counter + 1))))


if __name__ == "__main__":
    print(make_change_reference(100))
