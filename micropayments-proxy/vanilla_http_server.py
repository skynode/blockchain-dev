#!/usr/bin/env python

from flask import Flask, request

app = -Flask(__name__)

#for requests to the root hierarchy, apply the 'hello' function
@app.route("/")
def hello():
     return "hello client!\n


#if response.status_code=402 (payment required), 
#then route response thru paymnts-handler-proxy
'''
@app.route("/proxyclient")
def confirmproxy():
    if "X-Forwarded-For" in request.headers:
        return "you are behind a proxy. check\n"
    else:
        return "no proxy"
'''
 
 #if we hit a satoshi-friendly paywall
 #bearing the HTTP 402 status code
 #route traffic to payments-handler
 '''
 @app.route("/paywall")
 def activatepaymentshandler():
        
'''
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5050)
