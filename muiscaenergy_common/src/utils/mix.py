import pandas as pd


def parse_custom_freq(freq):
    num = ""
    unit = ""

    for char in freq:
        if char.isdigit():
            num += char
        else:
            unit += char

    if not num:
        num = "1"

    if unit == 'T':
        return pd.Timedelta(minutes=int(num))
    elif unit == 'H':
        return pd.Timedelta(hours=int(num))
    elif unit == 'D':
        return pd.Timedelta(days=int(num))
    else:
        raise ValueError("Invalid value for 'freq'.")
