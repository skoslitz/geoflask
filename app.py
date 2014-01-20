#!/usr/bin/env python2.7
# -*- coding: utf8 -*-

import os
from flask import Flask, render_template, url_for, json
from flaskext.coffee import coffee

app = Flask(__name__)
app.config.update(
  DEBUG=True,
  SECRET_KEY='You_will_never_know_:)'
)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')
coffee(app) 

@app.route('/')
def index():
    return render_template('index.jade')

@app.route('/python')
def python():
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	json_url = os.path.join(SITE_ROOT, "static/data", "taiwan.json")
	data = json.load(open(json_url))
	return render_template('python.jade', data=data)

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

@app.route('/d3mockup')
def d3mockup():
	return render_template('d3mockup/d3mockup.jade')

@app.route('/d3mockup/circles')
def d3circles():
	return render_template('d3mockup/d3circles.jade')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.jade')

if __name__ == '__main__':
    app.run()
