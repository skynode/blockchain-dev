# blockchain-dev
Studies on Distributed Computing, the Bitcoin Protocol and the Blockchain Network

## Micropayments Proxy

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
