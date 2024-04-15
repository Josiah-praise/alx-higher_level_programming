#!/usr/bin/python3
'''
Defines a new Model `City`
'''
from model_state import Base, State
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


engine = create_engine(
        f'mysql+mysqldb://root:Godsgrace123$$@localhost/hbtn_0e_6_usa',
        pool_pre_ping=True
        )


class City(Base):
    '''
    City Model
    '''

    __tablename__ = 'cities'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id',
                      Integer, ForeignKey(State.id), nullable=False)
    state = relationship("States", back_populates='cities')
