#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    # return app.send_static_file("index.html")
    # above in the Microsoft vscode-remote-try-python [dev container: python3]
    return "Welcome to the index"

@app.route('/about')
def about():
    return " About us"
    
if __name__ == '__main__':
    app.run()
