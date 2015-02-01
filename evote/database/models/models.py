from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey


__author__ = 'balhau'

from sqlalchemy import Column, Integer, String
from evote.database.dbase import Base

class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True)
    name=Column(String(50),unique=True)
    email=Column(String(120),unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)


class Vote(Base):
    __tablename__='vote'

    id=Column(Integer,primary_key=True)
    idSurvey=Column(Integer,ForeignKey("survey.id"))
    vote=Column(String(50))
    pubkey=Column(String)
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
    votes=relationship("Vote")




