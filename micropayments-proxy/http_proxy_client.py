'''
This client will invoke the micropayments-proxy, payments_handler.py,
only when the client receives an HTTP status_code 402 from some 
service running on some server to which an HTTP request has been made.
The payments-handler won't come into play under any other scenario.

---MIT Licensed
'''

#!/usr/bin/env python3

import requests, validators

VANILLA_SERVER      = "http://127.0.0.1:5050"
PAYWALLED_SERVER    = "http://127.0.0.1:5051
PAYMENTS_PROXY      = "http://127.0.0.1:9000"

#proxies dict syntax: {"protocol":"ip:port",...}
proxy = {"http": PAYMENTS_PROXY}

def main():
        #take url parameter from stdin
        '''        
        _url = input('please enter the resource locator here: ')
        
        #include the validated url in the GET function 
        if not validators.url(_url):
            print("invalid uniform resource locator format")
        '''
        #display list of online resources to client
        validurl = True
        while validurl:
            print("""
            1.VANILLA_SERVER
            2.PAYWALLED_SERVER
            3.Quit
            """)                    
        validurl = input('please select a number to continue to a server')
        if(validurl == "1" or validurl=="2"):
            res = requests.get(url=validurl)
            if(res.status_code==402):
                print("[+] " + res.status_code + ": you've hit a paywalled resource, redirecting to micropayments proxy...\n")
                
                '''pass paywalled server response to micropayments proxy 
                   micropayments proxy processes satoshi payment for client >
                   by interacting in a particular way with paywalled server >
                   and responds to http_proxy_client with HTTP 200 status_code <
                   http_proxy_client is granted access to paywalled resource <
                '''
                #continue from here...
                proxyres = requests.get(url=PAYMENTS_PROXY + "/paymentreq", proxies=proxy)
            else:
                print(res.status_code + " " + res.text)            
        elif(validurl=="3"):
            print("quitting...")
            
        try:
            if(requests.get().status_code != 402):
        
        #response from VANILLA_SERVER
        print ("You've hit the VANILLA_SERVER!".upper())
        print (requests.get(url=VANILLA_SERVER).text)           
        
        
        
        #test that payments-handler server is up
        #if response.status_code=50x, return... 
        #close connection with satoshi-requesting server