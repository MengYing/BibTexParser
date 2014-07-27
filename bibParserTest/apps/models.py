# -*- coding: utf-8 -*-
from flask.ext.sqlalchemy import SQLAlchemy

__all__ = ('db', 'Entries')

db = SQLAlchemy()

class Entry(db.Model):
    __tablename__ = 'entry'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number = db.Column(db.Integer)
    title = db.Column(db.String(), nullable=False)
    author = db.Column(db.String(), nullable=False)
    year = db.Column(db.Integer)

    def __init__(self, number, title, author, year):
        self.number = number
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return '<number %d, title %s, author %s, year %d >' % (self.number, self.title, self.author, self.year)
