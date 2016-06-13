#!/usr/bin/env python3
import requests

from flask import Flask, request, Response
from werkzeug.datastructures import Headers

from two1.wallet import Wallet
from two1.bitserv.flask import Payment

app = Flask(__name__)

wallet  = Wallet()
payment = Payment(app, wallet)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
@payment.required(1000)
def catch_all(path):
	try:
		#HTTP header manipulation
		h = Headers(request.headers)
		h.add('X-Forwarded-For', request.remote_addr)
		h.remove('HTTP_BITCOIN_MICROPAYMENT_SERVER')
		h.remove('HTTP_RETURN_WALLET_ADDRESS')
		h.remove('Bitcoin-Transfer')
		h.remove('Authorization')
		h.remove('Content-Length')
	
		#create a response object to hold request result parameters
		r = requests.request(
		    method=request.method,
		    url=request.url,
		    headers=h,
		    files=request.files if request.files else None,
		    data=request.data if request.data else None,
		    params=request.args if request.args else None,
		    timeout=5
		)
	except(
		requests.exceptions.Timeout,
		requests.exceptions.ConnectTimeout,
		requests.exceptions.ReadTimeout
	      ):
		return Response(status=504)
	except(
                requests.exceptions.ConnectionError,
                requests.exceptions.HTTPError,
                requests.exceptions.TooManyRedirects
              ):
		return Response(status=502)
	except(
                requests.exceptions.RequestException,
		Exception
	      ) as e:
			if app.debug:
				raise e
			return Response(status=500)

	headers = list(r.headers.items())
	return Response(
		r.text if r.text else "internal server error",
		status=r.status_code,
		headers=headers
	)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=9000)
