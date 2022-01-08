# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from config import app_active, app_config

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class Telefone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ddd = db.Column(db.Integer)
    numero = db.Column(db.Integer)
    empresa_id = db.Column(db.Integer)
    funcionario_id = db.Column(db.Integer)
    orgao_id = db.Column(db.Integer)