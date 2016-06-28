# Micropayments Proxy
A proxy client, `http_proxy_client.py`, will invoke a Bitcoin micropayments proxy server, `payments_handler.py`, when the client receives an HTTP status code 402 - `Payment Required` - from some service running on some server, `paywalled_server.py`, to which an HTTP request has been made. The payments proxy won't be activated under any other scenario. A plain vanilla server is included for testing purposes.

##REQUIREMENTS##
These servers were built on and run successfully on the [21.co](https://21.co) virtual network running on an instance of Amazon AWS Ubuntu 14.04. To install 21 on your AWS Ubuntu instance, run `curl https://21.co | sh` then run `21 --help` for help documentation. 
 
### How it Works

1. Start the following servers: `vanilla_http_server.py` (named for its
ordinariness), the `payments_handler.py` and the `paywalled_server.py` from the
command line. For example:
```
 ~/micropayments-proxy$ python3 paywalled_server.py
 ```
 2. Then start the `http_proxy_client.py` server likewise and follow the very simple
 instructions on the command line. For example:
 ```
 ~/micropayments-proxy$ python3 http_proxy_client.py
 
         1.VANILLA_SERVER
         2.PAYWALLED_SERVER
         3.QUIT
 [+] please select a number to continue to a server:
 ```
 
 And that's it! Easy! For any problems or questions, [please open an
 issue](https://github.com/skynode/blockchain-dev/issues/new).
