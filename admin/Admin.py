# -*- coding: utf-8 -*-
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuLink

from model.Role import Role
from model.User import User
from model.Empresa import Empresa
from model.Funcionario import Funcionario
from model.Licenca import Licenca
from model.Orgao import Orgao

from admin.Views import UserView, EmpresaView

def start_views(app, db):
    admin = Admin(app, name='Solid Consulting', template_mode='bootstrap4')
    admin.add_view(ModelView(Role, db.session, "Funções", category="Usuários"))
    admin.add_view(UserView(User, db.session, "Usuários", category="Usuários"))
    admin.add_view(EmpresaView(Empresa, db.session, 'Empresas', category="Empresas"))
    admin.add_view(ModelView(Funcionario, db.session, "Funcionários", category="Funcionários"))
    admin.add_view(ModelView(Licenca, db.session, "Licenças", category="Licenças"))
    admin.add_view(ModelView(Orgao, db.session, "Órgãos", category="Órgãos"))
    admin.add_link(MenuLink(name='Logout', url='/logout'))