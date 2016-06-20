'''
This client will invoke the micropayments-proxy, payments_handler.py,
when the client receives an HTTP status_code 402 from some service
running on some server to which an HTTP request has been made.
The payments-handler won't come into play under any other scenario.

---MIT Licensed
'''

#!/usr/bin/env python3

import requests as reqs, validators

VANILLA_SERVER      = "http://127.0.0.1:5050"
PAYWALLED_SERVER    = "http://127.0.0.1:5051"    
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
        validurl = input('[+] please select a number to continue to a server')
        if(validurl == "1" or validurl=="2"):
            res = reqs.get(url=validurl)            
            if(res.status_code==402):
                print("[+] " + res.status_code + ": you've hit a paywalled resource, redirecting to micropayments proxy...\n")
                
                '''pass paywalled server response params to micropayments proxy 
                   micropayments proxy processes satoshi payment for client 
                   by interacting in a particular way with paywalled server 
                   and responds to http_proxy_client with HTTP 200 status_code
                   http_proxy_client is granted access to paywalled resource 
                '''
                proxy_response = reqs.get(url=validurl, proxies=proxy)
            else:
                print(res.status_code + " " + res.text)            
        else:
            print("quitting...")

if __name__='__main__':
    main()
    
            
        