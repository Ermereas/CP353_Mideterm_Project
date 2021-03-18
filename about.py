from flask import Flask,render_template,request,redirect,Blueprint
from urllib.parse import quote
from urllib.request import urlopen
import json
import requests
import urllib.parse
from flask_sqlalchemy import SQLAlchemy
from models import db,info


about = Blueprint('about',__name__)

@about.route('/about')
def abouts():
    return render_template('aboutUS.html',Dev_info = info.query.all())