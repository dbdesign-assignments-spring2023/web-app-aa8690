#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, url_for, make_response,jsonify
from markupsafe import escape
import pymongo
import datetime
from bson.objectid import ObjectId
import os
import subprocess
from pymongo import MongoClient

client = MongoClient("mongodb+srv://aa8690:AAbsm07172038@cat-database.xrbv2kl.mongodb.net/?retryWrites=true&w=majority")
db = client.cats
cat_collection = db['cat']

# instantiate the app
app = Flask(__name__)

# load credentials and configuration options from .env file
# if you do not yet have a file named .env, make one based on the template in env.example
import credentials
config = credentials.get()

# turn on debugging if in development mode
if config['FLASK_ENV'] == 'development':
    # turn on debugging, if in development
    app.debug = True # debug mnode

""" # make one persistent connection to the database
connection = pymongo.MongoClient(config['MONGO_HOST'], 27017, 
                                username=config['MONGO_USER'],
                                password=config['MONGO_PASSWORD'],
                                authSource=config['MONGO_DBNAME'])
db = connection[config['MONGO_DBNAME']] # store a reference to the database
 """

for cat in cat_collection.find():
    cat_collection.update_one(
        {'_id': cat['_id']},
        {'$set': {'orig_short_descr': cat['short_descr']}}
    )

# set up the routes
@app.route('/home')
def home():
    """
    Route for the home page
    """
    return render_template('base.html')

@app.route('/cat/<name>')
def cat(name):
    cat_collection = db.cat
    cat = cat_collection.find_one({'name': name})
    print(cat) # print the cat information to the console
    return render_template('cat.html', cat=cat, name=name)

@app.route('/search', methods=['POST'])
def search_cat():
    cat_collection = db.cat
    search_query = request.form.get('search_query')
    matching_cat = cat_collection.find_one({'name': search_query})
    print(matching_cat)
    if matching_cat:
        return redirect(f'/cat/{matching_cat["name"]}')
    return redirect(url_for('home'))

@app.route('/edit/<name>', methods=['GET', 'POST'])
def edit_cat(name):
    cat_collection = db.cat
    cat = cat_collection.find_one({'name': name})

    if request.method == 'POST':
        new_descr = request.form['new_descr']
        cat_collection.update_one({'name': name}, {'$set': {'short_descr': new_descr}})
        return redirect(f'/cat/{name}')

    return render_template('edit.html', cat=cat)

@app.route('/delete/<name>', methods=['GET', 'POST'])
def delete_cat(name):
    cat_collection = db.cat
    cat = cat_collection.find_one({'name': name})

    if request.method == 'POST':
        cat_collection.update_one({'name': name}, {'$set': {'short_descr': ""}})
        print(f'{cat["name"]} has been deleted')
        return redirect(f'/cat/{name}')

    return render_template('delete.html', cat=cat)

@app.route('/restore/<name>', methods=['POST'])
def restore_cat(name):
    cat_collection = db.cat
    cat = cat_collection.find_one({'name': name})

    if cat and cat['short_descr'] != cat['orig_short_descr']:
        cat_collection.update_one({'name': name}, {'$set': {'short_descr': cat['orig_short_descr']}})
    
    return redirect(f'/cat/{name}')

@app.errorhandler(Exception)
def handle_error(e):
    """
    Output any errors - good for debugging.
    """
    return render_template('error.html', error=e) # render the edit template

if __name__ == "__main__":
    #import logging
    #logging.basicConfig(filename='/home/ak8257/error.log',level=logging.DEBUG)
    app.run(debug = True)