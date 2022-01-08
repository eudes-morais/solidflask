# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from config import app_active, app_config

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class Orgao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nomeorgao = db.Column(db.String(150))
    contato = db.Column(db.String(50))
    telefone1 = db.Column(db.String(15))
    telefone2 = db.Column(db.String(15))
    logradouro = db.Column(db.String(150))
    complemento = db.Column(db.String(100))
    bairro = db.Column(db.String(100))
    cidade = db.Column(db.String(100))
    estado = db.Column(db.String(20))
    cep = db.Column(db.String(8))