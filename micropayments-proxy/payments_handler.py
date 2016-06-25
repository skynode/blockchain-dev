#!/usr/bin/env python3

from flask import Flask, request, Response
from werkzeug.datastructures import Headers

from two1.wallet import Wallet

#originally handled by the requesting client 
#Now outsourced to payment_handler.py
from two1.bitrequests import BitTransferRequests
from two1.bitrequests import BitRequestsError

app = Flask(__name__)

#instantiate a wallet
_wallet = Wallet()

#this function handles bitcoin micropayments using the wallet object 
btc_requests = BitTransferRequests(_wallet)

''' simple satoshi-payment proxy with one function:
    receive request from client and process
    payment on destination server address 
    passed as url parameter in proxy client GET request
'''
@app.route('/')
def main():
    try:        
        #create a response object to hold request result based on param url received from client
        res = btc_requests.request(
            method=request.method, 
            url=request.url,            
            data=request.data if request.data else None,
            max_price=None,
            params=request.args if request.args else None,
            timeout=10
        )            

    except BitRequestsError as biterror:
        print("BitRequestsError: {0}".format(biterror))
     
    #return response from micropayments proxy to client
    return Response(res.text if res.text else "remote server error", 
        status=res.status_code        
    )
     
if __name__=='__main__':
    app.run(host='0.0.0.0',port=9000)
        
                 
        
            


