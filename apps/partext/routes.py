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
#@login_required
def index():
    return render_template('partext/partext.html', partext="active")

@blueprint.route('/partext/search', methods=['GET','POST'])
#@login_required
def search():
    data = None
    key_zh = request.args.get('key_zh')
    key_fr = request.args.get('key_fr')
    
    if len(key_fr)==0 and len(key_zh) == 0:
        print(key_zh,key_fr)
        return render_template('partext/partext.html', segment='index', partext="active",data=data, message=":请至少输入一个关键词",key_zh=key_zh,key_fr=key_fr)
    elif len(key_zh)!=0 and len(key_fr)!=0:
        data = Partext.query.filter(Partext.zh.like("%" + key_zh + "%")).filter(Partext.fr.like("%" + key_fr + "%")).all()
        if data:
            for d in data:
                d.zh = d.zh.replace(key_zh, f'<span class="tx-primary">{key_zh}</span>')
                d.fr = d.fr.replace(key_fr, f'<span class="tx-primary">{key_fr}</span>')
        else:
            data = None
    elif len(key_fr)==0 and len(key_zh)!=0:
        print('2')
        data = Partext.query.filter(Partext.zh.like("%" + key_zh + "%")).all()
        for d in data:
            d.zh = d.zh.replace(key_zh, f'<span class="tx-primary">{key_zh}</span>')
    elif len(key_fr)!=0 and len(key_zh)==0:
        print('3')
        data = Partext.query.filter(Partext.fr.like("%" + key_fr + "%")).all()
        for d in data:
            d.fr = d.fr.replace(key_fr, f'<span class="tx-primary">{key_fr}</span>')
    return render_template('partext/partext.html', segment='index', partext="active", data=data,key_zh=key_zh,key_fr=key_fr)
