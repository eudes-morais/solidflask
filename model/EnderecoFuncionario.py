# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from config import app_active, app_config
from model.Funcionario import Funcionario

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class EnderecoFuncionario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    logradouro = db.Column(db.String(150))
    complemento = db.Column(db.String(100))
    bairro = db.Column(db.String(100))
    cidade = db.Column(db.String(100))
    estado = db.Column(db.String(20))
    cep = db.Column(db.String(8))
    funcionario_id = db.Column(db.Integer, db.ForeignKey(Funcionario.id), nullable=False)
    # funcionarios = db.relationship('Funcionario', backref='funcionarios', uselist=False)