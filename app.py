#!/usr/bin/env python2.7
# -*- coding: utf8 -*-

from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config.update(
  DEBUG=True,
  SECRET_KEY='You_will_never_know_:)'
)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

from flaskext.coffee import coffee
coffee(app) 

@app.route('/')
def index():
    return render_template('index.jade')

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

@app.route('/d3mockup')
def d3mockup():
	return render_template('d3mockup/d3mockup.jade')

@app.route('/d3mockup/circles')
def d3circles():
	return render_template('d3mockup/d3circles.jade')

if __name__ == '__main__':
    app.run()
