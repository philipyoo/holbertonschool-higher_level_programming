#!/usr/bin/python3
# Write a file that contains class defns of a City and an instance
# Base = delcarative_base()
# City class:
# inherits from Base class, links to MySQL table 'cities',
# has columns id, name, and state_id
# Must use SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import State

Base = declarative_base()


class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
