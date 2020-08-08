#!/usr/bin/python3
"""Sets up an ORM for the table, city"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


class City(Base):
    """
    ------------
    CLASS: CITY
    ------------
    DESCRIPTION:
        Creates and connects an ORM to
        manage data.
    ARGS:
        Nil.
    """

    __tablename__ = 'cities'
    id = Column(Integer,
                autoincrement=True,
                unique=True,
                nullable=False,
                primary_key=True)
    name = Column(String(128),
                  nullable=False)
    state_id = Column(Integer,
                      ForeignKey('state.id'),
                      nullable=False)
