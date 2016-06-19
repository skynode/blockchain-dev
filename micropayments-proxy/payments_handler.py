#!/usr/bin/env python3

import requests


from flask import Flask, request, Response
from werkzeug.datastructures import Headers

from two1.wallet import Wallet
from two1.bitrequests import BitTransferRequests

app = Flask(__name__)

_wallet = Wallet()
requests = BitTransferRequests(_wallet)

''' simple micropayment proxy with one function:
    receive request from client and process
    payment on server address received as parameter
'''
@app.route('/')
def main():
    try:        
        #manipulate HTTP header information
        h = Headers(request.headers)
        h.add('X-Forwarded-For', request.remote_addr) #potentially prone to IP spoofing
        h.remove('HTTP_BITCOIN_MICROPAYMENT_SERVER')
        h.remove('HTTP_RETURN_WALLET_ADDRESS')
        h.remove('Bitcoin-Transfer')
        h.remove('Authorization')
        h.remove('Content-Length')
        
        #create a response object to hold request result based on param url received from client
        res = requests.request(
            method=request.method,
            url=request.url,
            headers=h,
            files=request.files if request.file else None,
            data=request.data if request.data else None,
            params=request.args if request.args else None,
            timeout=10
        )
    except(
        requests.exceptions.Timeout,
        requests.exception.ConnectTimeout,
        requests.exception.ReadTimeout
    ):
        return Response(status=504)
     except(
         requests.exceptions.ConnectionError,
         requests.exceptions.HTTPError,
         requests.exceptions.TooManyRedirects
     ):
        return Response(status=502)
     except(
         requests.exceptions.RequestException, Exception
     ) as e:
         if app.debug:
            raise e
         return Response(status=500)
     
     headers = list(res.headers.items())
     return Response(
         res.text if res.text else "internal server error",
         status=res.status_code,
         headers=headers
     )
     
if __name__='__main__':
    app.run(host='0.0.0.0',port=9000)
        
                 
        
            


