# -*- coding: UTF-8 -*-
"""
flask_redirect: Redirects requests to appropriate URL
"""
import os
import requests
from flask import Flask, redirect  # From module flask import class Flask
app = Flask(__name__)    # Construct an instance of Flask class for our webapp

@app.route('/redirect/<redirect_url>')
def redirect(redirect_url):
    if "BASE_URL" in os.environ:
        base_url = os.environ.get('BASE_URL')
        final_url = redirect_url + '.' + base_url
        redirect('https://'+final_url)
    if "BASE_URL" not in os.environ:
        return render_template('error.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=True)
