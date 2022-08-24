from flask import Flask, jsonify
from models import Venue
from models import Category
from settings import DATABASE, DB_USER

import os
import psycopg2

app = Flask(__name__)

app.config.mapping(
    DB_NAME = DATABASE,
    USER = DB_USER
)

def get_db():
    conn = psycopg2.connect(
        database = app.config['DB_NAME'],
        user = app.config['USER'],
        password = 'postgres')
    cursor = conn.cursor()

    return cursor


@app.route('/venues')
def venues():
    cursor = get_db()
    cursor.execute('SELECT * FROM venues;')
    venues = cursor.fetchall()
    venue_objs = [Venue(venue).__dict__ for venue in venues]
    return jsonify(venue_objs)

@app.route('/venues/<id>')
def show_venue(id):
    cursor = get_db()
    cursor.execute("SELECT * FROM venues WHERE id = %s LIMIT 1;", id)
    venue_values = cursor.fetchone()
    return jsonify(Venue(venue_values).__dict__)

app.run(debug = True)
