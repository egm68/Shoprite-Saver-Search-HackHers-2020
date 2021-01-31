import os
from flask import Flask, render_template, request, redirect, url_for
from twilio.rest import Client

app=Flask(__name__,template_folder='templates')

number = ''
phonenumber = ''

@app.route("/", methods=["GET", "POST"])
def takeinnumber():
	if request.method == 'POST':
		phonenumber = request.form['phonenumber']
		print(phonenumber)
	return render_template('takeinnumber.html')
print(phonenumber)

@app.route("/youdoneit", methods=["POST"])
def youdoneit():
	account_sid = 'secret'
	auth_token = 'secret'
	client = Client(account_sid, auth_token)
	message=client.messages.create(
		body="Thank you for using the Shoprite Saver Search. Please reply with your zip code to get started!",
 		from_='+12564748964',
		to=phonenumber,
			)
	return render_template("youdoneit.html")

if __name__=="__main__":
	app.run(debug=True, port='8080')
