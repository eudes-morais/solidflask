# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from config import app_active, app_config

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class Cnae(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(7))
    descricao = db.Column(db.String(200))

    def __repr__(self):
        return '%s - %s' % (self.codigo, self.descricao)