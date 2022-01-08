# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from config import app_active, app_config

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codprodutoncm = db.Column(db.String(11))
    codncm = db.Column(db.String(8))
    descricao = db.Column(db.String(150))
    quantidade = db.Column(db.Float)
    unidademedida = db.Column(db.String(12))