# -*- coding: utf-8 -*-
#!pip install flask-ngrok

from flask import Flask, render_template
from flask_ngrok import run_with_ngrok

app = Flask(__name__, template_folder='/templates')

run_with_ngrok(app)

@app.route('/')
def index():
  return "<h1>Welcome</h1> <p>Under construction</p>"

@app.route('/about')
def about():
  return "About Us"

@app.route('/profile/mammoth')
def profile():
  return "<h2>Welcome to profile Mammoth</h2>"

@app.route('/product/<name>')
def product_page(name):
  return "<h3>Product " + name + "</h3>"

@app.route('/product/<name>/<price>')
def product_information(name, price):
  return "<h4>About " + name + ":</h4> <p>Price: " + price + "</p>"

@app.route('/first-template')
def first_template():
  return render_template('first_template.html')

@app.route('/profile/<username>')
def show_profile(username):
  return render_template('profile.html', name=username)

if __name__ == '__main__':
  app.run()
