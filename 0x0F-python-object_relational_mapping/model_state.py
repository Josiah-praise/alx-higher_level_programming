#!/usr/bin/python3
'''
creates database table mapping for `states` using
sqlalchemy ORM
'''
from sqlalchemy.orm import declarative_base
# from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    '''
    ORM mapping to `states` table
    each attribute maps to a database column.

    __tablename__ is the verbose name of the database
    when created
    '''
    __tablename__ = 'states'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(128), nullable=False)
# Base.metadata.create_all(engine)
