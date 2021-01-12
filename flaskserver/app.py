import os
from flask import Flask, render_template, request, redirect
import pika
import hashlib
from random import randint, choice
import string
import csv

app = Flask(__name__,)

@app.route("/", methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		text = request.form['hash']
		connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
		channel = connection.channel()
		channel.queue_declare(queue='md5')
		channel.basic_publish(exchange='', routing_key='md5', body=text)
		connection.close()
		url = "/" + text
		return redirect(url)
	else:
		return render_template("index.html")	

@app.route("/random")
def random():
	length = randint(1,4)
	letters = string.ascii_lowercase
	result_str = ''.join(choice(letters) for i in range(length))
	final = str.encode(result_str)
	hash = hashlib.md5(final)
	return hash.hexdigest()

@app.route("/api/<md5>/<result>")
def api(md5, result):
	print(md5)
	print(result)
	csvfile = csv.reader(open('/data/hash.csv', 'r'))
	for row in csvfile:
		if md5==row[0]:
			return 'Recieved'
	with open('/data/hash.csv', mode = 'a') as csvfile:
		csvfile.write(md5 + ", " + result + "\n")
	return 'Recieved'

@app.route("/data")
def data():
	return render_template("data.html")

@app.route("/<md5>")
def check(md5):
	print(md5)
	csvfile = csv.reader(open('/data/hash.csv', 'r'))
	for row in csvfile:
		if md5==row[0]:
			return render_template("data.html", hash=md5, result=row[1])
	return render_template("cracking.html", hash=md5)

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)