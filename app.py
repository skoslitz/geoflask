#!/usr/bin/env python2.7
# -*- coding: utf8 -*-

import markdown
import os
from flask import Flask, render_template, url_for, json
from flaskext.coffee import coffee
from flask_flatpages import FlatPages

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    FLATPAGES_EXTENSION='.md',
    SECRET_KEY='You_will_never_know_:)'
)

coffee(app)
pages = FlatPages(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/blog')
def blog():
    return render_template('blog.html', articles=pages)


@app.route('/blog/<path:path>/')
def article(path):
    article = pages.get_or_404(path)
    return render_template('article.html', article=article)


@app.route('/python')
def python():
    return render_template('python.html')


@app.route('/charts')
def charts():
    return render_template('charts/charts.html')


@app.route('/charts/HIS-HF')
def hisHf():
    return render_template('charts/hisHf.html')


@app.route('/teeatlas')
def teeatlas():
    return render_template('teeatlas/teeatlas.html')


@app.route('/teeatlas/taiwan')
def taiwan():
    return render_template('teeatlas/taiwan.html')


@app.route('/teeatlas/indien')
def indien():
    return render_template('teeatlas/indien.html')


@app.route('/teeatlas/s_america')
def s_america():
    return render_template('teeatlas/s_america.html')


@app.route('/teeatlas/world')
def world():
    return render_template('teeatlas/world.html')


@app.route('/d3mockup')
def d3mockup():
    return render_template('d3mockup/d3mockup.html')


@app.route('/d3mockup/circles')
def d3circles():
    return render_template('d3mockup/d3circles.html')


@app.route('/projektmanagement/projektstruktur')
def projektstruktur():
    return render_template('projektmanagement/projektstruktur.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')


if __name__ == '__main__':
    app.run()
