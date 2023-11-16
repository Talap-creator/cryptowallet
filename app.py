from flask import Flask, jsonify, render_template
from binance.client import Client


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

app = Flask(__name__)

@app.route('/')
def index():
    # Здесь получайте балансы и передавайте их в HTML шаблон
    btc_balance = get_binance_balance(api_key, api_secret, 'BTC')
    eth_balance = get_binance_balance(api_key, api_secret, 'ETH')
    usdt_balance = get_binance_balance(api_key, api_secret, 'USDT')
    return render_template('index.html', btc_balance=btc_balance, eth_balance=eth_balance, usdt_balance=usdt_balance)

@app.route('/update_balance')
def update_balance():
    btc_balance = get_binance_balance(api_key, api_secret, 'BTC')
    eth_balance = get_binance_balance(api_key, api_secret, 'ETH')
    usdt_balance = get_binance_balance(api_key, api_secret, 'USDT')
    return jsonify({'btc_balance': btc_balance, 'eth_balance': eth_balance, 'usdt_balance': usdt_balance})



if __name__ == '__main__':
    app.run(debug=True)
