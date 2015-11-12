from Globals import package_home
from OFS.SimpleItem import Item, SimpleItem
from Products.ZSQLMethods.SQL import SQL
from datetime import datetime, date, timedelta
import os

global product_path
product_path = os.path.join(package_home(globals())) + '/'


class Usuarios(SimpleItem):

    "Factory"

    meta_type = 'Usuarios'

    def obter_usuario(self, id_usuario=None, email="", tipo_usuario=None,
                      logado=False, ip_login=""):

        r = self._zsql_sel_usuarios(
            id_usuario=id_usuario, email=email)
        if len(r):
            q = r[0]

        else:
            q = None

        return self.fabricar_usuario(q)

    def fabricar_usuario(self, dados_busca):
        """ Classe que entrega os dados para o
        construtor construir um objeto tipo Usuario """
        if dados_busca:
            usr = Usuario.from_dict(dados_busca)

            return usr
        return None

    def get_by_email(self, email):
        return self.obter_usuario(email=email)

    def get_by_id(self, id_usuario):
        return self.obter_usuario(id_usuario=id_usuario)

    def logar_usuario(self, id_usuario, hash_log):
        """loga o usuario no BD"""
        try:
            self._zsql_logar_usuario(id_usuario=id_usuario,
                                     ip_login=self.REQUEST['REMOTE_ADDR'],
                                     hash=hash_log)
        except:
            return False
        return True

    def deslogar_usuario(self, id_usuario):
        try:
            self._zsql_deslogar_usuario(id_usuario=id_usuario)
        except:
            return False

        return True

    _zsql_sel_usuarios = SQL(
        id='zsql_sel_usuarios', title='', connection_id='connection',
        arguments='id_usuario\nemail', template=open(
            product_path + 'sql/zsql_sel_usuario.sql').read()
    )

    _zsql_logar_usuario = SQL(
        id='zsql_logar_usuario', title='', connection_id='connection',
        arguments='id_usuario\nip_login\nhash', template=open(
            product_path + 'sql/zsql_logar_usuario.sql').read()
    )

    _zsql_deslogar_usuario = SQL(
        id='zsql_deslogar_usuario', title='', connection_id='connection',
        arguments='id_usuario', template=open(
            product_path + 'sql/zsql_deslogar_usuario.sql').read()
    )


class Usuario(SimpleItem):

    """
    Usuarios da agenda.

    """
    meta_type = "Usuario"

    manage_options = (
        (
            {'label': 'Contents', 'action': 'manage_main'},
        )
        + Item.manage_options
    )

    def __init__(self, id, email, tipo_usuario, nome_usuario,logado=False, ip_login=""):
        self._id = id
        self._email = email
        self._tipo_usuario = tipo_usuario
        self._logado = logado
        self._ip_login = ip_login
        self._nome_usuario = nome_usuario

    @classmethod
    def from_dict(cls, data):
        test = lambda x: data[x]  # x in data and data[x] or None
        new_usr = (test('id_usuario'), test('email'), test('id_tipo_usuario'),
                   test('logado'), test('ip_login'),test('nome_usuario'))

        return new_usr

    def to_dict(self):
        data = {
            'id': self._id,
            'email': self._email,
            'id_tipo_usuario': self._tipo_usuario,
            'logado': self._logado,
            'ip_login': self._ip_login,
            'nome_usuario':self._nome_usuario
        }

        return data

    def login(self, ip=''):
        """ Loga o usuario """
        self._logado = True
        self._ip_login = ip

    def logout(self):
        """ desloga o usuario """
        self._logado = False

    def get_login(self):
        return self._email

    def get_id(self):
        return self._id

    def get_tipo_acesso(self):
        tipo = self._tipo_usuario

        return tipo

    def set_email(self, email):
        self._email = email

    def set_tipo_acesso(self, tipo_usuario):
        """ Modifica o tipo de acesso """
        self._tipo_usuario = tipo_usuario

    def set_status_login(self):
        self._logado = True

    def set_status_login_false(self):
        self._logado = False

    def is_logged_in(self):
        """ Returns true if user is logged in """
        return self._logado and True
