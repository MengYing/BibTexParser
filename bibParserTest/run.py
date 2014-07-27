#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from flask.ext.script import Manager, prompt_bool, Server
from apps import db, app
from apps import create_app


manager = Manager(create_app)
#manager.add_command("runserver",Server())

@manager.command
def initdb():
    '''Creates all database tables.'''
    db.create_all()


@manager.command
def dropdb():
    '''Drops all database tables.'''
    if prompt_bool('Are you sure to drop your databse?'):
        db.drop_all()
if __name__ == '__main__':
	#manager.run()
    app.run()
