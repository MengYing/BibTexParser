from bibtexparser.bparser import BibTexParser
from flask import Flask , session
from flask import Blueprint, request, url_for, redirect, render_template, jsonify
from .models import db, Entry
from apps import models
from sqlalchemy.orm import sessionmaker

module = Blueprint('example', __name__)


@module.route('/')
def index():
    return redirect(url_for('example.show_entries'))

@module.route('/show')
def show_entries():
    #entries = Entry.query.all()
    p = models.Entry.query.all()
    print p
    #p = Entry.select(Entry.number == 1).execute().first()
    #p2 = p['name']
    return render_template("show.html", data = p )


@module.route('/add')
def add():
  with open('hcomp13.bib', 'r') as bibfile:
    bp = BibTexParser(bibfile.read())
    
    records_dict = bp.get_entry_dict()
    # use dic to find out
    count = 0
    for thing in records_dict.keys():
      entry = Entry(number = count, title = records_dict[thing]['title'], author = records_dict[thing]['author'], year = records_dict[thing]['year'])
      db.session.add(entry)
      db.session.commit()
      count += 1

  return jsonify(ouput="add")