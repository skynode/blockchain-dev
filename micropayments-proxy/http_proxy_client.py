'''
This client will invoke the micropayments-proxy, payments_handler.py,
only when the client receives an HTTP status_code 402 from some 
service running on some server.
The payments-handler won't come into play under any other scenario.

---MIT Licensed
'''

#!/usr/bin/env python3

import requests

VANILLA_SERVER      = "http://127.0.0.1:5050"
PAYWALLED_SERVER    = "http://127.0.0.1:5051
PAYMENTS_PROXY      = "http://127.0.0.1:9000"

proxies = {"http": PROXY_SERVER}

def main(url):
        #take url parameter from stdin
        input('please enter the resource locator here: ')
        #include the validated url in the GET function 
        try:
            if(requests.get(url).status_code != 402):
        
        #response from VANILLA_SERVER
        print ("You've hit the VANILLA_SERVER!".upper())
        print (requests.get(url=VANILLA_SERVER).text)
        
        print ()               
        
        
        
        #test that payments-handler server is up
        #if response.status_code=50x, return... 
        #close connection with satoshi-requesting server