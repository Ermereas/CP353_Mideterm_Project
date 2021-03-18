from flask import Flask,render_template,request,redirect,Blueprint
from urllib.parse import quote
from urllib.request import urlopen
import json
import requests
import urllib.parse
from flask_sqlalchemy import SQLAlchemy

search = Blueprint('search',__name__)

@search.route("/search")
def searchh():
    findGame = find_game()
    return render_template('search.html',findGame=findGame)

def find_game():
    find_url = "https://www.cheapshark.com/api/1.0/games?title={0}&limit=60&exact=0"
    word = request.args.get('word')
    url = find_url.format(str(word).replace(" ",""))
    data = urlopen(url).read()
    r = json.loads(data)
    show = []
    for x in range(len(r)) :
        name = r[x]['external']
        thumb = r[x]['thumb']
        steamAppID = r[x]['steamAppID']
        cheapest = r[x]['cheapest']
        cheapestDealID = r[x]['cheapestDealID']
        show.append({"external":name,"thumb":thumb,"steamAppID":steamAppID,"cheapest":cheapest,"cheapestDealID":cheapestDealID})
    return show

