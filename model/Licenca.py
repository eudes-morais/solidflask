# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from config import app_active, app_config
from sqlalchemy.dialects.postgresql import ARRAY
from model.Empresa import Empresa

from model.Orgao import Orgao

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class Licenca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numerolicenca = db.Column(db.String(20))
    datainicial = db.Column(db.DateTime)
    datafinal = db.Column(db.DateTime)
    valorlicenca = db.Column(db.Float)
    orgao_id = db.Column(db.Integer, db.ForeignKey(Orgao.id), nullable=False)
    # orgaos = db.relationship('Orgao', backref='licenca')
    empresa_id = db.Column(db.Integer, db.ForeignKey(Empresa.id), nullable=False)
    # empresas = db.relationship('Empresa', backref='licenca')
    produto_id = db.Column(ARRAY(db.Integer))
    atividade_id = db.Column(ARRAY(db.Integer))