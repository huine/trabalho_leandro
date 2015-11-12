from Globals import package_home
from OFS.SimpleItem import Item, SimpleItem
from Products.ZSQLMethods.SQL import SQL
from datetime import datetime, date, timedelta
from sha import sha
import uuid
import os
from Products.agenda.Evento.Evento import Eventos

global product_path
product_path = os.path.join(package_home(globals())) + '/'


class Listas(SimpleItem):

    "Factory"

    meta_type = 'Listas'

    ev = Eventos()

    def obter_eventos_from_lista(self, id_lista=None):
        return self.ev.get_all_from_lista(id_lista)

    def obter_listas_usuario(self, id_usuario=None, id_lista=None):
        r = self._zsql_busca_lista(
            id_usuario=id_usuario, id_lista=id_lista)

        q = None
        if len(r):
            q = r

        return q

    def valida_relacao_lista_usuario(self, id_usuario, id_lista):

        if self.obter_listas_usuario(id_usuario, id_lista) is not None:
            return True
        else:
            return False

    def get_listas_by_usuario(self, id_usuario):
        return self.obter_listas_usuario(id_usuario=id_usuario)

    def get_by_id(self, id_lista):
        return self.obter_listas_usuario(id_lista=id_lista)

    def get_all_eventos_by_id(self, id_lista):
        return self.obter_eventos_from_lista(id_lista=id_lista)

    def get_all_by_usuario(self, id_usuario):

        return self.obter_senha(id_usuario=id_usuario)

    def add_lista(self, id_usuario, titulo):
        r = self._zsql_add_lista(id_usuario=int(
            id_usuario), titulo=str(titulo))

    _zsql_busca_lista = SQL(
        id='zsql_busca_lista', title='', connection_id='connection',
        arguments='id_usuario\nid_lista', template=open(
            product_path + 'sql/zsql_busca_lista.sql').read()
    )
    _zsql_add_lista = SQL(
        id='zsql_add_lista', title='', connection_id='connection',
        arguments='id_usuario\ntitulo', template=open(
            product_path + 'sql/zsql_add_lista.sql').read()
    )


class Lista(SimpleItem):
    """
        senha do usuario da agenda
    """

    _titulo = ""
    _id = -1
    _eventos = {}

    def __init__(self, titulo, id_lista, eventos):
        self._titulo = titulo
        self._id = id_lista
        self._eventos = eventos

    def get_titulo(self):
        return self._titulo

    def get_id(self):
        return self._id

    def get_eventos(self):
        return self._eventos
