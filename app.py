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
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')
coffee(app)

pages = FlatPages(app)


@app.route('/')
def index():
    return render_template('index.jade')


@app.route('/blog')
def blog():
    return render_template('blog.jade', articles=pages)


@app.route('/blog/<path:path>/')
def article(path):
    article = pages.get_or_404(path)
    return render_template('article.jade', article=article)


@app.route('/python')
def python():
    pass


@app.route('/charts')
def charts():
    return render_template('charts/charts.jade')


@app.route('/charts/HIS-HF')
def hisHf():
    return render_template('charts/hisHf.jade')


@app.route('/teeatlas')
def teeatlas():
    return render_template('teeatlas/teeatlas.jade')


@app.route('/teeatlas/taiwan')
def taiwan():
    return render_template('teeatlas/taiwan.jade')


@app.route('/teeatlas/indien')
def indien():
    return render_template('teeatlas/indien.jade')


@app.route('/teeatlas/s_america')
def s_america():
    return render_template('teeatlas/s_america.jade')


@app.route('/teeatlas/world')
def world():
    return render_template('teeatlas/world.jade')


@app.route('/d3mockup')
def d3mockup():
    return render_template('d3mockup/d3mockup.jade')


@app.route('/d3mockup/circles')
def d3circles():
    return render_template('d3mockup/d3circles.jade')


@app.route('/projektmanagement/projektstruktur')
def projektstruktur():
    return render_template('projektmanagement/projektstruktur.jade')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.jade')


if __name__ == '__main__':
    app.run()
