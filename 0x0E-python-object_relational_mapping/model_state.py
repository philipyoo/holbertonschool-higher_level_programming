#!/usr/bin/python3
# Write a file that contains class defns of a State and an instance
# Base = delcarative_base()
# State class:
# inherits from Base class, links to MySQL table 'states',
# has columns id and name
# Must use SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
