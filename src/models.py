import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Favs(Base):
    __tablename__ = 'favs'
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    type_id = Column(Integer, ForeignKey('type.id'), nullable=False)
    

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True) 
    name = Column(String(250), nullable=False)  

class Ships(Base):
    __tablename__ = 'ships'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)  

class Type(Base):
    __tablename__ = 'type'
    id = Column(Integer, primary_key=True)
    characters_id = Column(Integer, ForeignKey('characters.id'), nullable=True)
    planets_id = Column(Integer, ForeignKey('planets.id'), nullable=True)
    ships_id = Column(Integer, ForeignKey('ships.id'), nullable=True)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
