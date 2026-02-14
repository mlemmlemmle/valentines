#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  7 22:11:18 2026

@author: ruiyang
"""

from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/yay")
def yay():
    return render_template("yay.html")
if __name__ == "__main__":
    app.run(debug=True)
    

