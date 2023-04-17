import os

from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Initializes the app
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/aquele-dia")
def thatDay():
    return render_template("thatDay.html")