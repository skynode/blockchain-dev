from flask import Flask, request
from two1.wallet import Wallet
from two1.bitserv.flask import Payment

app = Flask(__name__)

_wallet = Wallet()
_payment = Payment(app, _wallet)

#catch all requests to all resource paths on this server
@app.route('/', defaults={'path':''})
@app.route('/<path:path>')
@payment.required(1500)
def catch_call(path):
     return "payment received from micropayments proxy for paywalled resource: %s" %path

'''
@app.route("/paywalled_resource")
def confirm_proxy_payment(path):
    if "X-Forwarded-For" in request.headers:
        return "payment received from micropayments proxy for "+ "first".upper() + " paywalled resource"
    else:
        return "no proxy"      
        
@app.route("/paywalled_resource_2")
def confirm_second_proxy_payment(path):
    if "X-Forwarded-For" in request.headers:
        return "payment received from micropayments proxy for "+ "second".upper() + " paywalled resource"
    else:
        return "no proxy"      
'''  

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5051)