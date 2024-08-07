#!/usr/bin/python3

"""
This module defines a State class and creates a MySQL table `states`
using SQLAlchemy ORM. The table includes columns for id and name.

Usage:
    - Ensure SQLAlchemy is installed: pip install SQLAlchemy
    - Replace <username>, <password>, and <database_name> with your MySQL credentials
    - Run the script to create the table in the specified MySQL database
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()


class State(Base):
        '''class defination of a table'''
         __tablename__ = 'states'

         id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
         name = Column(String(128), nullable=False)
