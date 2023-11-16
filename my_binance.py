from binance.client import Client

# Использование функции для получения баланса конкретной монеты (например, BTC)

api_key = 'O9KtcRoFwVLHrQJjSEiDEWyiBzUzP421AanVNggjB4Eg7GNKUDUPBsB5QUyMgjU2'
api_secret = 'JWIlyD0Ku94wzs8v1c4MsAkDqVYewI3FNjDDiRnooO898yIqK4eoraqkI9hzt6b2'

def get_binance_balance(api_key, api_secret, symbol):
    client = Client(api_key, api_secret)
    account_info = client.get_account()
    balances = {}

    for asset in account_info['balances']:
        if float(asset['free']) > 0.0:
            balances[asset['asset']] = float(asset['free'])

    if symbol in balances:
        return balances[symbol]
    else:
        return 0.0

# Запрашиваем баланс Bitcoin (BTC)
btc_balance = get_binance_balance(api_key, api_secret, 'BTC')
print(f"Баланс BTC: {btc_balance}")

# Запрашиваем баланс Ethereum (ETH)
eth_balance = get_binance_balance(api_key, api_secret, 'ETH')
print(f"Баланс ETH: {eth_balance}")

# Запрашиваем баланс Tether (USDT)
usdt_balance = get_binance_balance(api_key, api_secret, 'USDT')
print(f"Баланс USDT: {usdt_balance}")