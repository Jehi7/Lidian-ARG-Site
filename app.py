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

@app.route("/quem-e-voce", methods=["GET", "POST"])
def who():
    if request.method == "POST":
        channelI = request.form.get("channel")
        volI = request.form.get("vol")

        if channelI == "13" and volI == "47":
            return render_template("who.html")
        return redirect("/aquele-dia")
    
    return render_template("who.html")

@app.route("/menu", methods=["GET", "POST"])
def hub():
    if request.method == "POST":
        name = request.form.get("nome").capitalize()

        if name == "Carla" or name == "Maya" or name == "Sua mãe":
            return render_template("carla.html")
        elif name == "Lidian" or name == "Rebecca" or name == "Becca" or name == "Seu pai":
            return render_template("lidian.html")
        elif name == "Carlos" or name == "Kim":
            return render_template("carlos.html")
        elif name == "Nathan" or name == "Bea" or name == "Beatrice" or name == "Seu irmão":
            return render_template("nathan.html")
        elif name == "Você":
            return render_template("carla.html")

    return render_template("who.html")