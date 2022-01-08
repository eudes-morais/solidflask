# -*- coding: utf-8 -*-
from flask_admin.contrib.sqla import ModelView
from config import app_config, app_active
from model.EnderecoEmpresa import EnderecoEmpresa

config = app_config[app_active]

class UserView(ModelView):
    column_labels = {
        'funcao': 'Função',
        'username': 'Nome de usuário',
        'email': 'E-mail',
        'date_created': 'Data de criação',
        'last_update': 'Última atualização',
        'active': 'Ativo',
        'password': 'Senha',
    }

    column_descriptions = {
        'funcao': 'Função no painel administrativo',
        'username': 'Nome de usuário no sistema',
        'email': 'E-mail do usuário no sistema',
        'date_created': 'Data de criação do usuário no sistema',
        'last_update': 'Última atualização desse usuário no sistema',
        'active': 'Estado ativo ou inativo no sistema',
        'password': 'Senha do usuário no sistema',
    }

    column_exclude_list = ['password', 'recovery_code']
    form_excluded_columns = ['last_update', 'recovery_code']

    form_widget_args = {
        'password': {
            'type': 'password'
        }
    }

    can_set_page_size = True
    can_view_details = True
    column_searchable_list = ['username', 'email']
    column_filters = ['username', 'email', 'role']
    column_editable_list = ['username', 'email', 'role', 'active']
    create_modal = True
    edit_modal = True
    can_export = True
    column_sortable_list = ['username']
    column_default_sort = ('username', True)
    column_details_exclude_list = ['password', 'recovery_code']
    column_export_exclude_list = ['password', 'recovery_code']
    export_types = ['json', 'yaml', 'csv', 'xls', 'df']
    
    def on_model_change(self, form, User, is_created):
        if 'password' in form:
            if form.password.data is not None:
                User.set_password(form.password.data)
            else:
                del form.password

class EmpresaView(ModelView):
    column_labels = {
        'numeropasta': 'Número da pasta',
        'razaosocial': 'Razão Social',
        'inscricaoestadual': 'Inscrição Estadual',
        'cnpj': 'CNPJ',
        'caixapostal': 'Caixa Postal',
        'email': 'E-mail',
        'telefone1': 'Telefone Celular',
        'telefone2': 'Telefone Fixo',
    }

    can_set_page_size = True
    can_view_details = True
    column_searchable_list = ['razaosocial', 'cnpj']
    # column_filters = ['razaosocial', 'cnpj']
    column_editable_list = ['numeropasta', 'email', 'telefone1', 'telefone2']
    # create_modal = True
    # edit_modal = True
    can_export = True
    column_default_sort = ('razaosocial', True)
    export_types = ['json', 'yaml', 'csv', 'xls', 'df']

    inline_models = [EnderecoEmpresa] # Só funciona se for feito o downgrade para a versão wtforms==2.3.3