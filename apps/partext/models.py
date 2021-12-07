# -*- encoding: utf-8 -*-

from apps.db import db
from .util import get_head,deal_star

class Partext(db.Model):

    __tablename__ = 'Par_Text'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    zh = db.Column(db.Text)
    fr = db.Column(db.Text)
    param = db.Column(db.String(256), unique=True)


def init_partext_db(file):
    with open(file,'r',encoding='utf-8') as f_zh:
        datas = f_zh.read()
        datas = [x for x in datas.split('$') if x]
    data_heads = []
    data_fr = []
    data_zh = []
    for data in datas:
        data = '$' + data
        data = data.strip('\n')
        head = get_head(data)
        data_heads.append(head)
    for i, data in enumerate(datas):
        data = '$' + data
        data = data.strip('\n')
        if '*' in data:
            data = deal_star(data)
        if 'ZH' in data_heads[i]:
            data = data.replace(' ','')
            data_zh.append(data.replace(data_heads[i], ''))
        else:
            data_fr.append(data.replace(data_heads[i], ''))
    for d_zh, d_fr, d_head in zip(data_zh,data_fr,data_heads):
        data = Partext(zh=d_zh, fr=d_fr, param=d_head)
        db.session.add(data)
        db.session.commit()
