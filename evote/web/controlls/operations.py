import json
from __builtin__ import dict
from database.dbase import db_session
from database.models.models import User, Survey, as_dict

__author__ = 'balhau'

row2dict = lambda r: {c.name: str(getattr(r, c.name)) for c in r.__table__.columns}

def newUser(name,pubkey,email):
    u = User(name,pubkey,email)
    db_session.add(u)
    db_session.commit()

def newSurvey(name,desc):
    s=Survey(name,desc)
    db_session.add(s)
    db_session.commit()

def listSurveys():
    list=[]
    for el in db_session.query(Survey).all():
        list.append(as_dict(el))
    return json.dumps(list)


