#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------
#to get this to run in the container use run Python Debugger: using launch.json
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    # return app.send_static_file("index.html")
    # above in the Microsoft vscode-remote-try-python [dev container: python3]
    # return "Welcome to the index"
    return "<h1>Welcome</h1>  <p>Under construction</p>"

@app.route('/about')
def about():
    return "About us"

@app.route('/profile/mammoth')    
def profile():
    return "<h2>Welcome to profile</h2>"

@app.route('/product/<name>') #<name> is whatever is passed in <> alligator brackets :-)
def product_page(name):
    return "<h3>Product " + name + "</h3>"

@app.route('/product/<name>/<price>')
def product_information(name,price):
    return "<h4>About " + name + ": </h4> <p>Price: " + price + "</p>"



if __name__ == '__main__':
    app.run()
