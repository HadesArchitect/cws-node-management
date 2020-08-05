from flask import Flask
from markupsafe import escape
from flask import jsonify
import sqlite3
from flask import g
app = Flask(__name__)
DATABASE = './database.db'

@app.route('/node/<nodeid>/lease', methods=['POST'])
def node_lease_increase(nodeid):
    cur = get_db().cursor()
    # get or create in db
    # +24 
    # save in db
    app.logger.info("Extended lease time for node ID %s" % nodeid)
    return jsonify()

@app.route('/node/<nodeid>/lease', methods=['GET'])
def node_lease_get(nodeid):
    # find in db
    # return time or 404
    return jsonify()

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
