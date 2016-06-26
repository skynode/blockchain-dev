#!/usr/bin/env python3

import requests

from flask import Flask, request
from two1.wallet import Wallet
from two1.bitserv.flask import Payment

from werkzeug.datastructures import Headers

app = Flask(__name__)

_wallet = Wallet()
_payment = Payment(app, _wallet)

#catch all requests to all resource paths on this server
@app.route('/', defaults={'path':''})
@app.route('/<path:path>')
@_payment.required(1500)
def catch_all(path):

    #retrieve and type-cast the header data
    hed = Headers(request.headers)

    #remove the bitcoin micropayment headers to receive payment from micropayments proxy
    hed.remove('HTTP_BITCOIN_MICROPAYMENT_SERVER')
    hed.remove('HTTP_RETURN_WALLET_ADDRESS')
    hed.remove('Bitcoin-Transfer')
    hed.remove('Authorization')
    hed.remove('Content-Length')

    #send payment notification to micropayments proxy
    return "[+] " + str(requests.codes['OK']) + " - payment received from micropayments proxy for paywalled resource\n" 

if __name__ == "__main__":
    app.run(host='0.0.0.1', port=5051)