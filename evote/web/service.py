from evote.database.models.models import User

__author__ = 'balhau'
from flask import Flask
from flask import render_template
from evote.database.dbase import init_db, db_session


app=Flask(__name__)

omxProcess=None

@app.route('/')
def index():
    init_db()
    return render_template('index.html')


if __name__ == '__main__':
	app.debug=True
	app.run(host='0.0.0.0')
