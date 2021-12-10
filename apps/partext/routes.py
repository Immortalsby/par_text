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

@blueprint.route('/partext/search/text', methods=['GET','POST'])
#@login_required
def search_text():
    data = None
    key_zh = request.args.get('key_zh')
    key_fr = request.args.get('key_fr')
    
    if len(key_fr)==0 and len(key_zh) == 0:
        print(key_zh,key_fr)
        return render_template('partext/partext.html', partext="active",data=data,
         message=":请至少输入一个关键词",key_zh=key_zh,key_fr=key_fr,text="text")
    elif len(key_zh)!=0 and len(key_fr)!=0:
        data = Partext.query.filter(Partext.zh.like("%" + key_zh + "%")).filter(Partext.fr.like("%" + key_fr + "%")).all()
        for d in data:
            d.zh = d.zh.replace(key_zh, f'<span class="tx-primary">{key_zh}</span>')
            d.fr = d.fr.replace(key_fr, f'<span class="tx-primary">{key_fr}</span>')
    elif len(key_fr)==0 and len(key_zh)!=0:
        data = Partext.query.filter(Partext.zh.like("%" + key_zh + "%")).all()
        for d in data:
            d.zh = d.zh.replace(key_zh, f'<span class="tx-primary">{key_zh}</span>')
    elif len(key_fr)!=0 and len(key_zh)==0:
        data = Partext.query.filter(Partext.fr.like("%" + key_fr + "%")).all()
        for d in data:
            d.fr = d.fr.replace(key_fr, f'<span class="tx-primary">{key_fr}</span>')
    if data:
        pass
    else:
        data = None
    try:
        return render_template('partext/partext.html', segment='index', partext="active", 
        data=data,key_zh=key_zh,key_fr=key_fr,text="text")
    except TemplateNotFound:
        return render_template('home/page-404.html'), 404
    except:
        return render_template('home/page-500.html'), 500

@blueprint.route('/partext/search/map', methods=['GET','POST'])
#@login_required
def search_map():
    data = None
    key_zh = request.args.get('key_zh')
    key_fr = request.args.get('key_fr')
    has_key = {
        'zh': False,
        'fr': False
    }
    #判断至少填了一个关键词
    if len(key_fr)==0 and len(key_zh) == 0:
        return render_template('partext/partext.html', partext="active"
        ,data=data, message=":请至少输入一个关键词",key_zh=key_zh,key_fr=key_fr,map="map")
    else:
        data = Partext.query.filter().all()
        for d in data:
            d.option = {
                'zh_color': "bg-white",
                'fr_color':"bg-white",
                'zh_opa': None,
                'fr_opa': None
            }
            if str(d.zh).find(key_zh) != -1 and len(key_zh) != 0:
                d.option['zh_color'] = "bg-primary"
                has_key['zh'] = True
                d.option['zh_opa'] = 20 + 10 * d.zh.count(key_zh) if d.zh.count(key_zh) < 9 else 100
                d.zh = d.zh.replace(key_zh, f'<span class="tx-warning">{key_zh}</span>')
            if str(d.fr).find(key_fr) != -1 and len(key_fr) != 0:
                d.option['fr_color'] = "bg-primary"
                has_key['fr'] = True
                d.option['fr_opa'] = 30 + 5 * d.fr.count(key_fr) if d.fr.count(key_fr) < 9 else 100
                d.fr = d.fr.replace(key_fr, f'<span class="tx-warning">{key_fr}</span>')
    #如果填了两个关键词，并且其中一个没有匹配
    if (has_key['fr'] == False or has_key['zh'] == False) and (len(key_fr)!=0 and len(key_zh) != 0):
        data = None
    if data:
        pass
    else:
        data = None
    try:
        return render_template('partext/partext.html', partext="active", data=data,
        key_zh=key_zh,key_fr=key_fr,map="map")
    except TemplateNotFound:
        return render_template('home/page-404.html'), 404
    except:
        return render_template('home/page-500.html'), 500

@blueprint.route('/partext/search/freq', methods=['GET','POST'])
#@login_required
def search_freq():
    data = None
    key_zh = request.args.get('key_zh')
    key_fr = request.args.get('key_fr')
    if data:
        pass
    else:
        data = None
    try:
        return render_template('partext/partext.html', partext="active", data=data,
        key_zh=key_zh,key_fr=key_fr,freq="freq")
    except TemplateNotFound:
        return render_template('home/page-404.html'), 404
    except:
        return render_template('home/page-500.html'), 500
