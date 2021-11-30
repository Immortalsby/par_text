# -*- encoding: utf-8 -*-

from apps.db import db

class Partext(db.Model):

    __tablename__ = 'Par_Text'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    zh = db.Column(db.Text)
    fr = db.Column(db.Text)


def init_partext_db(zh,fr):
    zh_datas = fr_datas = ''
    with open(zh,'r',encoding='utf-8') as f_zh:
        zh_data = f_zh.read()
        zh_data = zh_data.split('#')
    with open(fr,'r',encoding='utf-8') as f_fr:
        fr_data = f_fr.read()
        fr_data = fr_data.split('#')
    for zh_datas,fr_datas in zip(zh_data,fr_data):
        data = Partext(zh=zh_datas, fr=fr_datas)
        db.session.add(data)
        db.session.commit()
