from flask import render_template
from app import app

# Views
@app.route('/')

def index():

    '''
    view toot page
    '''
    sources=get_sources('general')
    business_sources = get_sources('business')
    sports_sources=get_sources('sports')

    technology_sources=get_sources('technology')

    entertainment_sources=get_sources('entertainment')
    title="News Highlighter"
    return render_template('index.html', title=title, sources=sources ,business_sources=business_sources,sports_sources=sports_sources,technology_sources=technology_sources,entertainment_sources=entertainment_sources)
