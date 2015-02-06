from database.dbase import db_session
from database.models.models import User, Survey

__author__ = 'balhau'


def newUser(name,pubkey,email):
    u = User(name,pubkey,email)
    db_session.add(u)
    db_session.commit()

def newSurvey(name,desc):
    s=Survey(name,desc)
    db_session.add(s)
    db_session.commit()

def listSurveys():
    #todo
    print "Return a list of surveys"