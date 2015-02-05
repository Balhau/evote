__author__ = 'balhau'

from flask import Flask
from flask import render_template
from flask import request
import json
from database.dbase import init_db, db_session
from database.models.models import User

init_db()

app=Flask(__name__)

omxProcess=None

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/newuser",methods=['POST'])
def newuser():
    try:
        data=json.loads(request.data)
        name=data['name']
        pubkey=data['pubkey']
        mail=data['mail']
        u = User(name,pubkey,mail)
        db_session.add(u)
        db_session.commit()
        return '{"status":"ok"}'
    except:
        return '{"status":"fail"}'

@app.route("/regkey",methods=['POST'])
def regkey():
    try:
        return '{"status":"ok"}'
    except:
        return '{"status":"fail"}'
if __name__ == '__main__':
	app.debug=True
	app.run(host='0.0.0.0')
