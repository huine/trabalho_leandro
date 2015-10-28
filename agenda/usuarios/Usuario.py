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

    def obterUsuario(self, id_usuario=None, email=None, tipo_usuario=None):
        r = self._zsql_sel_usuarios(
            id_usuario=id_usuario, email=login, tipo_acesso=tipo_acesso)
        if len(r):
            q = r[0]

        else:
            q = None

        return self.fabricarUsuario(q)

    def fabricarUsuario(self, dados_busca):
        """ Classe que entrega os dados para o
        construtor construir um objeto tipo Usuario """
        if dados_busca:
            usr = Usuario.fromDict(dados_busca)

            return usr
        return None

    def getByEmail(self, email):
        return self.obterUsuario(email=email)

    def getById(self, id_usuario):
        return self.obterUsuario(id_usuario=id_usuario)

    _zsql_sel_usuarios = SQL(
        id='zsql_sel_usuarios', title='', connection_id='connection',
        arguments='email\nid_usuario', template=open(
            product_path + 'sql/zsql_sel_usuario.sql').read()
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

    def __init__(self, id, email, tipo_usuario, logado = False, ip_login = ""):
        self._id = id
        self._email = email
        self._tipo_usuario = tipo_usuario


    @classmethod
    def fromDict(cls, data):
        test = lambda x: data[x]  # x in data and data[x] or None
        newUsr = (test('id'),test('email'),test('id_tipo_usuario'))
        newUsr._logado = test('logado')
        newUsr._ip_login = test('ip_login')

        return newUsr

    def toDict(self):
        data = {
            'id': self._id,
            'email': self._email,
            'id_tipo_usuario': self._tipo_usuario,
            'logado': self._logado,
            'ip_login':self._ip_login
        }

        return data

    def login(self, ip=''):
        """ Loga o usuario """
        self._logado = True
        self._ip_login = ip

    def logout(self):
        """ Subtrai 1 da quantidade de logins e retorna o novo
            numero. Se sobrou 0 login o usuario eh deslogado. """
        self._status_login = False

        return 0

    def getLogin(self):
        return self._email

    def getId(self):
            return self._id

    def getTipoAcesso(self):
            tipo = self._tipo_usuario

            return tipo

    def setEmail(self, email):
            self._email = email

    def set_tipo_acesso(self, tipo_usuario):
            """ Modifica o tipo de acesso """
            self._tipo_usuario = tipo_usuario

    def setStatusLogin(self):
            self._logado = True

    def setStatusLoginFalse(self):
            self._logado = False

    def isLoggedIn(self):
            """ Returns true if user is logged in """
            return self._logado and True
