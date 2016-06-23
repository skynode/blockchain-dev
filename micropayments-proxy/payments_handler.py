#!/usr/bin/env python3

import requests as pyreq

from flask import Flask, request, Response
from werkzeug.datastructures import Headers

from two1.wallet import Wallet

#originally handled by the requesting client 
#Now outsourced to payment_handler.py
from two1.bitrequests import BitTransferRequests

app = Flask(__name__)

#instantiate a wallet
_wallet = Wallet()

#this function handles bitcoin payments using the wallet object as parameter
btc_reqs = BitTransferRequests(_wallet)

''' simple satoshi-payment proxy with one function:
    receive request from client and process
    payment on destination server address 
    passed as url parameter in proxy client GET request
'''
@app.route('/<path:url>')
def main(url):
    try:        
        #manipulate HTTP header information
        h = Headers(request.headers)
        h.add('X-Forwarded-For', request.remote_addr) #potentially prone to IP spoofing
        
        #would work with a proxy server that has the @payment.required() descriptor
        '''
        h.remove('HTTP_BITCOIN_MICROPAYMENT_SERVER')
        h.remove('HTTP_RETURN_WALLET_ADDRESS')
        h.remove('Bitcoin-Transfer')
        h.remove('Authorization')
        h.remove('Content-Length')
        '''
        
        #create a response object to hold request result based on param url received from client
        res = pyreq.request(
            method=request.method, 
            url=request.url,
            headers=h,
            files=request.files if request.files else None,
            data=request.data if request.data else None,
            params=request.args if request.args else None,
            timeout=10
        )
    except(pyreq.exceptions.Timeout, 
        pyreq.exception.ConnectTimeout,
        pyreq.exception.ReadTimeout
    ):
        return Response(status=504)
    except(pyreq.exceptions.ConnectionError, 
        pyreq.exceptions.HTTPError,
        pyreq.exceptions.TooManyRedirects
    ):
        return Response(status=502)
    except(pyreq.exceptions.RequestException, Exception) as e:
        if app.debug:
           raise e
        return Response(status=500)
     
    headers = list(res.headers.items())
    return Response(res.text if res.text else "internal server error", 
        status=res.status_code,
        headers=headers
     )
     
if __name__=='__main__':
    app.run(host='0.0.0.0',port=9000)
        
                 
        
            


