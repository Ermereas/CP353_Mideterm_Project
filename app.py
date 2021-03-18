from flask import Flask,render_template,request,redirect,Blueprint
from urllib.parse import quote
from urllib.request import urlopen
import json
import requests
import urllib.parse
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from models import db,info
from search import search
from news import news
from about import about
from stored import stored

app = Flask(__name__)
app.register_blueprint(search)
app.register_blueprint(news)
app.register_blueprint(about)
app.register_blueprint(stored)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Dev_info.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Game_URL ="https://www.cheapshark.com/api/1.0/deals"

NEWS_URL ="http://newsapi.org/v2/everything?q=videogame&from={YMD}}&sortBy=publishedAt&apiKey=3f9a09e2092a46febac3ba21fef17969"
YMD = datetime.today().strftime('%Y-%m-%d')

db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

@app.route("/")
def home():
    game=Game()
    return render_template("home.html",game=game)

def Game():
    
    url ="https://www.cheapshark.com/api/1.0/deals"
    store_url ="https://www.cheapshark.com/api/1.0/stores"
    response2 = requests.request("GET", store_url)
    R = response2.json()
    response = requests.request("GET", url)
    r = response.json()
    show = []
    for x in range(len(R)) :
        name = r[x]['title']
        normalPrice = r[x]['normalPrice']
        salePrice = r[x]['salePrice']
        savings = round(float(r[x]['savings']),2)
        thumb = r[x]['thumb']
        storeID = r[x]['storeID']
        dealID = r[x]['dealID']

        show.append({"title":name,"normalPrice":normalPrice,"salePrice":salePrice,"savings":savings,"thumb":thumb,"storeID":storeID,"dealID":dealID})
    
    return show 

app.run(debug=True,use_reloader=True)