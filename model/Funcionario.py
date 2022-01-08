# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from config import app_active, app_config
from model.Empresa import Empresa

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class Funcionario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nomefuncionario = db.Column(db.String(150))
    cpf = db.Column(db.String(11))
    rg = db.Column(db.String(11))
    orgaoexpedidor = db.Column(db.String(11))
    grauinstrucao = db.Column(db.String(25))
    nacionalidade = db.Column(db.String(40))
    ufnascimento = db.Column(db.Integer)
    municipionascimento = db.Column(db.String(100))
    datanascimento = db.Column(db.DateTime)
    estadocivil = db.Column(db.String(13))
    profissao = db.Column(db.String(50))
    nomepai = db.Column(db.String(150))
    nomemae = db.Column(db.String(150))
    email = db.Column(db.String(50))
    cargo = db.Column(db.String(50))
    telefone1 = db.Column(db.String(15))
    telefone2 = db.Column(db.String(15)) 
    empresa_id = db.Column(db.Integer, db.ForeignKey(Empresa.id), nullable=False)
    # empresasfunc = db.relationship('Empresa', backref='funcionarios', uselist=False)