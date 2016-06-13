'''


'''

#!/usr/bin/env python3

#do we need these import statements?
from two1.wallet import Wallet
from two1.bitrequests import BitTransferRequests

HTTP_SERVER  = "http://127.0.0.1:5000"
PROXY_SERVER = "http://127.0.0.1:9000"

proxies = {"http": PROXY_SERVER}

def main():
        
        
        
        
        #test that payments-handler server is up
        #if response.status_code=50x, don't pay... 
        #close connection with satoshi-requesting server