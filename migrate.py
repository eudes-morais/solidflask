# Devido à alguns erros, deve-se fazer um downgrade dos pacotes:
# flask==1.1.4 e Flask-Migrate==2.1.1

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy.dialects.postgresql.array import ARRAY
from config import app_active, app_config

config = app_config[app_active]
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

class Role(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(40),unique=True,nullable=False)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(40),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    password = db.Column(db.String(80),nullable=False)
    date_created = db.Column(db.DateTime(6),default=db.func.current_timestamp(),nullable=False)
    last_update = db.Column(db.DateTime(6),onupdate=db.func.current_timestamp(),nullable=True)
    recovery_code = db.Column(db.String(200),nullable=True)
    active = db.Column(db.Boolean(),default=1,nullable=True)
    role_id = db.Column(db.Integer,db.ForeignKey(Role.id),nullable=False)
    
class Atividade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(150))

class Cnae(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(7))
    descricao = db.Column(db.String(200))

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

class EnderecoEmpresa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    logradouro = db.Column(db.String(150))
    complemento = db.Column(db.String(100))
    bairro = db.Column(db.String(100))
    cidade = db.Column(db.String(100))
    estado = db.Column(db.String(20))
    cep = db.Column(db.String(8))
    empresa_id = db.Column(db.Integer, db.ForeignKey(Empresa.id), nullable=False)

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

class EnderecoFuncionario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    logradouro = db.Column(db.String(150))
    complemento = db.Column(db.String(100))
    bairro = db.Column(db.String(100))
    cidade = db.Column(db.String(100))
    estado = db.Column(db.String(20))
    cep = db.Column(db.String(8))
    funcionario_id = db.Column(db.Integer, db.ForeignKey(Funcionario.id), nullable=False)

class Estado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.Integer)
    sigla = db.Column(db.String(2))
    nome = db.Column(db.String(20))

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

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codprodutoncm = db.Column(db.String(11))
    codncm = db.Column(db.String(8))
    descricao = db.Column(db.String(150))
    quantidade = db.Column(db.Float)
    unidademedida = db.Column(db.String(12))

class Licenca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numerolicenca = db.Column(db.String(20))
    datainicial = db.Column(db.DateTime)
    datafinal = db.Column(db.DateTime)
    valorlicenca = db.Column(db.Float)
    orgao_id = db.Column(db.Integer, db.ForeignKey(Orgao.id), nullable=False)
    empresa_id = db.Column(db.Integer, db.ForeignKey(Empresa.id), nullable=False)
    produto_id = db.Column(ARRAY(db.Integer))
    atividade_id = db.Column(ARRAY(db.Integer))

class Telefone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ddd = db.Column(db.Integer)
    numero = db.Column(db.Integer)
    empresa_id = db.Column(db.Integer)
    funcionario_id = db.Column(db.Integer)
    orgao_id = db.Column(db.Integer)

if __name__ == '__main__':
    manager.run()