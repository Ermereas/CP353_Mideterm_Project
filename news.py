from flask import Flask,render_template,request,redirect,Blueprint
from urllib.parse import quote
from urllib.request import urlopen
import json
import requests
import urllib.parse
from flask_sqlalchemy import SQLAlchemy

news = Blueprint('news',__name__)


NEWS_URL = "http://newsapi.org/v2/everything?q={0}&from=2021-3-11&sortBy=publishedAt&apiKey={1}"

NEWS_KEY = "125abe47c9fb4dccb9241c39c7f1abeb" 

@news.route('/news')
def newss():
    word = request.args.get('word')
    if not word:
        word = 'game+steam'
   
    news = get_news(word, NEWS_KEY)
    return render_template('news.html',news=news)

def get_news(word,NEWS_KEY):
    word = convert_to_unicode(word)
    url = NEWS_URL.format(word, NEWS_KEY)
    data = urlopen(url).read()
    parsed = json.loads(data)
    news = []
    
    for i in range(len(parsed['articles'])):
        title = parsed['articles'][i]['title']
        description = parsed['articles'][i]['description']
        img = parsed['articles'][i]['urlToImage']
        link = parsed['articles'][i]['url']
        news.append({"title":title,"description":description,"link":link,"img":img})
    
    return news

def convert_to_unicode(txt):
    encode = urllib.parse.quote(txt)
    return encode