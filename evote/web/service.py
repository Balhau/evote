from evote.evote.database.models.models import User

__author__ = 'balhau'
from flask import Flask
from flask import render_template
from flask import request
from evote.evote.database.dbase import init_db, db_session


app=Flask(__name__)

omxProcess=None

@app.route('/')
def index():
    init_db()
    u = User("digri","digri@digri.com")
    db_session.add(u)
    db_session.commit()
    return render_template('index.html')


@app.route("/newuser",methods=['POST'])
def newuser():
    try:
        name=request.form['name']
        pubkey=request.form['pubkey']
        mail=request.form['mail']
        u = User(name,pubkey,mail)
        db_session.add(u)
        db_session.commit()
        return '{"status":"ok"}'
    except:
        return '{"status":"fail"}'


if __name__ == '__main__':
	app.debug=True
	app.run(host='0.0.0.0')
