from Globals import package_home
from OFS.SimpleItem import Item, SimpleItem
from Products.ZSQLMethods.SQL import SQL
from datetime import datetime, date, timedelta
from sha import sha
import uuid
import os

global product_path
product_path = os.path.join(package_home(globals())) + '/'


class Senhas(SimpleItem):

    "Factory"

    meta_type = 'Senhas'

    def obter_senha(self, id_usuario=None, email=None):
        r = self._zsql_busca_senha_usuarios(
            id_usuario=id_usuario, email=email)
        if len(r):
            q = r[0]

        else:
            q = None

        return self.fabricar_senha(q)

    def fabricar_senha(self, dados_busca):
        """ Classe que entrega os dados para o
        construtor construir um objeto tipo Usuario """
        if dados_busca:
            pwd = Senha.from_dict(dados_busca)

            return pwd
        return None

    def get_by_email(self, email):
        return self.obter_senha(email=email)

    def get_by_id(self, id_usuario):
        return self.obter_senha(id_usuario=id_usuario)

    def get_crypt(self, senha):
        return Senha.crypt(senha)

    def get_decrypt(self, usr_senha, senha_hash):
        return Senha.decrypt(usr_senha=usr_senha, senha_hash=senha_hash)

    def get_hash(self):
        return Senha.gerar_hash()

    _zsql_busca_senha_usuarios = SQL(
        id='zsql_busca_senha', title='', connection_id='connection',
        arguments='id_usuario\nemail', template=open(
            product_path + 'sql/zsql_busca_senha.sql').read()
    )


class Senha(SimpleItem):
    """
        senha do usuario da agenda
    """

    def __init__(self, senha):
        self._senha = senha

    @classmethod
    def from_dict(cls, data):
        test = lambda x: data[x]  # x in data and data[x] or None
        new_pwd = (test('senha'))

        return new_pwd

    def to_dict(self):
        data = {'senha': self._senha}

        return data

    @classmethod
    def gerar_hash(cls):
        salt = sha(uuid.uuid4().hex).hexdigest()

        return salt

    @classmethod
    def crypt(cls, senha):
        """ encripta a senha """
        salt = uuid.uuid4().hex
        new_senha = sha(
            salt.encode() + senha.encode()).hexdigest() + ':*:' + salt

        return new_senha

    @classmethod
    def decrypt(cls, usr_senha, senha_hash):
        """ encripta a senha """
        senha, salt = senha_hash.split(':*:')

        return senha == sha(salt.encode() + usr_senha.encode()).hexdigest()
