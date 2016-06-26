'''
----Demonstration of Bitcoin Micropayment Proxy Using the 21.co API----

This client will invoke a micropayments proxy server, payments_handler.py,
when the client receives an HTTP status_code 402 from some service
running on some server to which an HTTP request has been made.
The payments-handler won't be activated play under any other scenario.

---MIT Licensed
'''
#!/usr/bin/env python3

#import the HTTP python library for humans
import requests as reqs

VANILLA_SERVER      = "http://127.0.0.1:5050"
PAYWALLED_SERVER    = "http://0.0.0.0:5051"    
PAYMENTS_PROXY      = "http://127.0.0.1:9000"

#proxies dict syntax: {"protocol":"ip:port",...}
proxy = {"http": PAYMENTS_PROXY}

def main():
        validurl = True
        #we run this loop once
        while validurl:
            print("""
                    1.VANILLA_SERVER
                    2.PAYWALLED_SERVER
                    3.Quit
            """)     
            break           
        validurl = input('[+] please select a number to continue to a server: ')
        if(validurl == "1"):
            res = reqs.get(url=VANILLA_SERVER) 
            if(res.status_code == 200):
                print("[+] " + str(res.status_code) + " thank you for checking into the VANILLA_SERVER!")
                print("[+] quitting...\n")

        '''If we hit some paywalled resource on the network, pass the
           paywalled server response params to a micropayments proxy. 
           Micropayments proxy processes satoshi payment for client 
           by interacting in a particular way with the paywalled server 
           and responds to http_proxy_client with HTTP 200 status_code.
           http_proxy_client is then granted access to paywalled resource 
        '''
        elif(validurl == "2"):
            res = reqs.get(url=PAYWALLED_SERVER)
            print("[-] " + str(res.status_code) + " - you've hit a paywalled resource, redirecting to micropayments proxy...\n")
            if(res.status_code == 402):
                res = reqs.get(url=PAYWALLED_SERVER, proxies=proxy)
                print(res.text)                                        
        else:
            print("[+] quitting...\n")              

if __name__=='__main__':
    main()
    
            
        