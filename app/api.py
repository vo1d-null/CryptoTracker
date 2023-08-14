import requests


def get_crypto_prices():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum,ripple",  # Replace with the cryptocurrencies you want
        "vs_currencies": "usd",
    }

    response = requests.get(url, params=params)
    data = response.json()
    return data
