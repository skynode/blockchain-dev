#!/usr/bin/env python3

import requests

'''
from flask import Flask, request, Response
from werkzeug.datastructures import Headers

from two1.wallet import Wallet
from two1.bitserv.flask import Payment
'''

from two1.wallet import Wallet
from two1.bitrequests import BitTransferRequests


app = Flask(__name__)

_wallet = Wallet()
requests = BitTransferRequests(_wallet)

''' simple micropayment proxy with one function:
    just receive request from client and process
    payment on server address received as parameter
'''
@app.route('/', defaults={'path': ''})
def main(path):
        #res = requests.get(url)





