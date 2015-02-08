from Crypto.PublicKey import RSA
import M2Crypto
import base64
import json
from __builtin__ import dict
from crypto.keypair import KeyPair
from database.dbase import db_session
from database.models.models import User, Survey, as_dict, PubKey

__author__ = 'balhau'

row2dict = lambda r: {c.name: str(getattr(r, c.name)) for c in r.__table__.columns}

STATUS_OK=('ok','')
STATUS_FAIL=lambda desc: ('fail',desc)

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


def regSurveyKey(user,key,signature,survey):
    u=db_session.query(User).filter_by(name=user).first()
    s=db_session.query(Survey).filter_by(name=survey).first()
    #If the user and the survey don't exists...
    if u == None or s == None:
        return STATUS_FAIL("The user or the survey don't exist")

    #todo: Check if the user is already registered for that survey

    kp=KeyPair()
    kp.loadPublicKeyFromString(u.pubKey)
    if kp.verifyB4sha1(key,signature):
        pk=PubKey(key,s.id)
        db_session.add(pk)
        db_session.commit()
        return STATUS_OK
    return STATUS_FAIL("The signature is not valid")

