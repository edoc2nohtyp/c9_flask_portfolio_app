from flask import Flask, render_template, request, redirect
import datetime
import pytz # timezone 
import requests
import os



app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
	return render_template('index.html')

@app.route('/<name>')
def profile(name):
	if name != 'None':
		new_name = 'Hello ' + str(name) + ', fell free to have a look at my work!'
        return render_template('index.html', name=new_name)
    else:
        new_name = 'Hello, fell free to have a look at my work!'
        return render_template('index.html', name=new_name)




if __name__ == '__main__':
	app.run(debug=True)
