#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

#for requests to the root hierarchy, say hello
@app.route("/")
def hello():
	if not request.headers.getlist("X-Forwarded-For"):
    	return "you've reached the VANILLA HTTP SERVER\n"

#start vanilla HTTP server 
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5050)
