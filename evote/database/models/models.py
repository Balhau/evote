from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table


__author__ = 'balhau'

from sqlalchemy import Column, Integer, String
from database.dbase import Base

survey_user_table = Table('survey_user', Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('survey_id', Integer, ForeignKey('survey.id'))
)


def as_dict(obj):
    return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}

class User(Base):
    __tablename__='user'
    id=Column(Integer,primary_key=True)
    name=Column(String(50),unique=True)
    email=Column(String(120),unique=True)
    pubKey=Column(String)
    surveys=relationship('Survey',secondary=survey_user_table)

    def __init__(self, name=None, pubkey=None ,email=None):
        self.name = name
        self.email = email
        self.pubKey=pubkey

    def __repr__(self):
        return '<User %r, %r>' % (self.name,self.pubKey)


class PubKey(Base):
    __tablename__='pubkey'

    id=Column(Integer,primary_key=True)
    idSurvey=Column(Integer,ForeignKey('survey.id'))
    pubkey=Column(String)



class Vote(Base):
    __tablename__='vote'

    id=Column(Integer,primary_key=True)
    idSurvey=Column(Integer,ForeignKey('survey.id'))
    idPubKey=Column(Integer,ForeignKey("pubkey.id"))
    vote=Column(String(50))
    signature=Column(String)

    def __init__(self,vote,pubkey,signature):
        self.vote=vote
        self.pubkey=pubkey
        self.signature=signature

    def __repr__(self):
        return "<Vote %r, %r, %r>" % (self.vote,self.pubkey,self.signature)


class Survey(Base):

    __tablename__='survey'

    id=Column(Integer,primary_key=True)
    name=Column(String(50),unique=True)
    description=Column(String)
    votes=relationship('Vote')

    def __init__(self, name=None,description=None):
        self.name = name
        self.description=description

    def __repr__(self):
        return '<Survey %r, %r>' % (self.name,self.description)

