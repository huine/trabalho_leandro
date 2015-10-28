from Globals import package_home
from Globals import DTMLFile
from OFS.SimpleItem import Item, SimpleItem
from Products.ZSQLMethods.SQL import SQL
from datetime import datetime, date, timedelta
from Products.agenda.usuarios.Usuario import Usuarios
from Products.agenda.senha.Senha import Senhas
from Products.agenda.UI.ui import Ui
import os

global product_path
product_path = os.path.join(package_home(globals())) + '/'


class Acesso(SimpleItem):

    """
        classe acesso
    """
    usr = Usuarios()
    pwd = Senhas()
    ui = Ui('ee')

    def pg_login(self):
        """exibe a pagina de login"""
        return self.index_html()

    def verifica_dados_form(self, RESPONSE, dados=None):
        """faz a verificacao dos dados inseridos no form de login"""

        erro = 'Login e/ou senha Invalido.'

        if not dados:
            dados = self.REQUEST.form

        dados_user = self.usr.get_by_email(email=dados['email'])

        if not dados_user:
            self.REQUEST.set('erro', erro)
            return self._erro()

        senha_user = self.pwd.get_by_id(id_usuario=dados_user[0])

        senha_form = self.pwd.get_crypt(dados['senha'])

        if senha_user == senha_form:
            return self.ui.pg_principal()
        else:
            self.REQUEST.set('erro', erro)
            return self._erro()

    index_html = DTMLFile('dtml/index', globals())
    _erro = DTMLFile('dtml/error', globals())
