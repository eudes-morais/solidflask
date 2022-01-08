# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from config import app_active, app_config
from model.Empresa import Empresa

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class EnderecoEmpresa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    logradouro = db.Column(db.String(150))
    complemento = db.Column(db.String(100))
    bairro = db.Column(db.String(100))
    cidade = db.Column(db.String(100))
    estado = db.Column(db.String(20))
    cep = db.Column(db.String(8))
    empresa_id = db.Column(db.Integer, db.ForeignKey(Empresa.id), nullable=False)
    empresa = relationship(Empresa, backref='endereço')

    def __repr__(self):
        return self.empresa_id
