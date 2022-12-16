import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Fav(Base):
    __tablename__ = 'fav'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    type_id = Column(Integer, ForeignKey('type.id'), nullable=False)
    user = relationship(User)
    

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True) 
    name = Column(String(250), nullable=False)  

class Ship(Base):
    __tablename__ = 'ship'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)  

class Type(Base):
    __tablename__ = 'type'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    ship_id = Column(Integer, ForeignKey('ship.id'), nullable=True)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
