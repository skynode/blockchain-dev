First, start the following servers: _(vanilla_http_server.py)_ (named for its ordinariness), the _(payments_handler.py)_ and the _(paywalled_server.py)_ from the command line. As an example:

*~/micropayments-proxy$ python3 paywalled_server.py*

Next, start the _(http_proxy_client.py)_ server likewise and follow the very simple instruction on the command line. As an example:

*~/micropayments-proxy$ python3 http_proxy_client.py*

        1.VANILLA_SERVER
        2.PAYWALLED_SERVER
        3.QUIT
        
*[+] please select a number to continue to a server:*

On the command line, run *21 log* to confirm that transaction was really successful in addition to the HTTP status codes on each server
