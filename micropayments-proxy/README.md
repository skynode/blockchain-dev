#DESCRIPTION#
A proxy client, http_proxy_client.py, will invoke a micropayments proxy server, payments_handler.py, when the client receives an HTTP status_code 402 - Payment Required - from some service running on some server to which an HTTP request has been made. The payments-handler won't be activated play under any other scenario. A plain vanilla server is included for comparative testing purposes. 

##REQUIREMENTS##
These servers were built on and run successfully on the [21.co](https://21.co) virtual network running on an instance of Amazon AWS Ubuntu 14.04. To install 21 on your AWS Ubuntu instance, run **curl https://21.co | sh** then run **21 -h** for help documentation. 

###RUNNING THE SERVERS###
First, start the following servers: _vanilla_http_server.py_ (named for its ordinariness), the _payments_handler.py_ (the paying proxy) and the _paywalled_server.py_ (merchant server) from the command line. As an example:

**~/micropayments-proxy$ python3 paywalled_server.py**

Next, start the _http_proxy_client.py_ server likewise and follow the very simple instruction on the command line. As an example:

**~/micropayments-proxy$ python3 http_proxy_client.py**

        1.VANILLA_SERVER
        2.PAYWALLED_SERVER
        3.QUIT
        
**[+] please select a number to continue to a server:**

On the command line, run **21 log** to confirm that transaction was really successful in addition to the HTTP status codes on each server. 
