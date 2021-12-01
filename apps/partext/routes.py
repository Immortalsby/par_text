# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - present Boyuanshi.com
"""

from apps.partext import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound
from .models import Partext
from .util import is_contains_chinese


@blueprint.route('/partext', methods=['GET','POST'])
@login_required
def index():
    return render_template('partext/partext.html', partext="active")

@blueprint.route('/partext/search', methods=['GET','POST'])
@login_required
def search():
    key = request.args.get('key')
    if is_contains_chinese(key):
        data = Partext.query.filter(Partext.zh.like("%" + key + "%")).all()
    else:
        data = Partext.query.filter(Partext.fr.like("%" + key + "%")).all()
    return render_template('partext/partext.html', segment='index', partext="active", data=data,key=key)
