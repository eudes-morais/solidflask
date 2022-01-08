# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref, relationship
from config import app_active, app_config
from model.Cnae import Cnae

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class Empresa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numeropasta = db.Column(db.Integer)
    razaosocial = db.Column(db.String(150))
    inscricaoestadual = db.Column(db.String(15))
    cnpj = db.Column(db.String(14))
    caixapostal = db.Column(db.String(10))
    email = db.Column(db.String(50))
    telefone1 = db.Column(db.String(15))
    telefone2 = db.Column(db.String(15))
    cnae_id = db.Column(db.Integer, db.ForeignKey(Cnae.id), nullable=False)
    cnae = relationship(Cnae)
    # enderecoempresa = relationship(EnderecoEmpresa, backref='empresa')