#REQUIREMENTS#
These servers were built on and run successfully on the [21.co](https://21.co) virtual network running on an instace of Amazon AWS Ubuntu 14.04. To install 21 on your AWS Ubuntu instance, run **curl https://21.co | sh** then run **21 -h** for help documentation. 

##RUNNING THE SERVERS##
First, start the following servers: _vanilla_http_server.py_ (named for its ordinariness), the _payments_handler.py_ (the paying proxy) and the _paywalled_server.py_ (merchant server) from the command line. As an example:

**~/micropayments-proxy$ python3 paywalled_server.py**

Next, start the _http_proxy_client.py_ server likewise and follow the very simple instruction on the command line. As an example:

**~/micropayments-proxy$ python3 http_proxy_client.py**

        1.VANILLA_SERVER
        2.PAYWALLED_SERVER
        3.QUIT
        
**[+] please select a number to continue to a server:**

On the command line, run **21 log** to confirm that transaction was really successful in addition to the HTTP status codes on each server. 
