from flask import Flask,render_template,request,redirect,Blueprint
from urllib.parse import quote
from urllib.request import urlopen
import json
import requests
import urllib.parse
from flask_sqlalchemy import SQLAlchemy

stored = Blueprint('stored',__name__)
@stored.route("/stored")
def stored_page():
    stored=Storeds()
    return render_template("stored.html",stored=stored)

def Storeds():
    store_url ="https://www.cheapshark.com/api/1.0/stores"
    response = requests.request("GET", store_url)
    r = response.json()
    show = []
    for x in range(len(r)) :
        storeID = r[x]['storeID']
        storeName = r[x]['storeName']
        
        show.append({"storeID":storeID,"storeName":storeName})
    
    return show