#!/usr/bin/python3
""" Model City """

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import State, Base


class City(Base):
    ''' class to create the table cities '''
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
