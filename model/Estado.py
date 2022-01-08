# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from config import app_active, app_config

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class Estado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.Integer)
    sigla = db.Column(db.String(2))
    nome = db.Column(db.String(20))