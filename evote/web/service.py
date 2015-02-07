from web.controlls.operations import newUser, newSurvey, listSurveys, STATUS_OK, STATUS_FAIL, regSurveyKey

__author__ = 'balhau'

from flask import Flask
from flask import render_template
from flask import request
import json
from functools import wraps
from database.dbase import init_db, db_session
from database.models.models import User

init_db()

app=Flask(__name__)




def getStatus(status):
    return '{"status": "%s"}'% status


#Decorator to wrap the status of the request into the controller
def withStatus(f):
    @wraps(f)
    def wrapper():
        status=f()
        return getStatus(status)
    return wrapper


@app.route('/')
@withStatus
def index():
    return render_template('index.html')


@app.route("/newuser",methods=['POST'])
@withStatus
def newuser():
    try:
        data=json.loads(request.data)
        newUser(data['name'],data['pubkey'],data['mail'])
        return STATUS_OK
    except:
        return STATUS_FAIL

@app.route("/regkey",methods=['POST'])
@withStatus
def regkey():
    try:
        data=json.loads(request.data)
        regSurveyKey(data['user'],data['key'],data['signature'])
        return STATUS_OK
    except:
        return STATUS_FAIL


@app.route("/newsurvey",methods=['POST'])
@withStatus
def newsurvey():
    try:
        data=json.loads(request.data)
        newSurvey(data['surveyname'],data['description'])
        return STATUS_OK
    except Exception, e:
        print e
        return STATUS_FAIL


@app.route("/listsurveys",methods=['GET'])
def listSurvey():
    return listSurveys()


if __name__ == '__main__':
	app.debug=True
	app.run(host='0.0.0.0')
