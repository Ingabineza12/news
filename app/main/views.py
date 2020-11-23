from flask import render_template,request,redirect,url_for
from app import app
from .request import get_sources

# Views
@app.route('/')

def index():

    '''
    view toot page
    '''

    business_sources=get_sources('business')
    sports_sources=get_sources('sports')

    technology_sources=get_sources('technology')

    entertainment_sources=get_sources('entertainment')
    title="News Highlighte"
    return render_template('index.html', title=title, business=business_sources,sports=sports_sources,technology=technology_sources,entertainment=entertainment_sources)
