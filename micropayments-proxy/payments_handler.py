#!/usr/bin/env python3

import requests

from flask import Flask, request, Response
from werkzeug.datastructures import Headers

from two1.wallet import Wallet
from two1.bitserv.flask import Payment

app = Flask(__name__)

_wallet = Wallet()
_payment = Payment(app, _wallet)

@app.route('/',)

