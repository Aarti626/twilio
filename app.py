
# Download the helper library from https://www.twilio.com/docs/python/install# Download the helper library 
from twilio.rest import Client
from flask import Flask
from flask import request
import os 
import glob, os
from os import environ
import io
from flask_cors import CORS

# Your Account Sid and Auth Token from twilio.com/console
app = Flask(__name__)
CORS(app)

@app.route("/call",methods=["POST"])
def call():
	account_sid = 'ACb78bda6471d6cb3bf521a5520990ca7a'
	auth_token = 'f83cbe3c67248ab5a0c4c1acb90a56a1'
	client = Client(account_sid, auth_token)
	call = client.calls.create(
						url='https://demo.twilio.com/welcome/voice/',
						to='+919770445436',
						from_='+18446523945'
					)
	print(call.sid)
	return call.sid

if __name__ == "__main__":
	call()
	print("call is in progress")
	port = int(os.environ.get("PORT", 8080))
	app.run(host='0.0.0.0', port=port)
