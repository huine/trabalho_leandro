from Globals import package_home
from OFS.SimpleItem import Item, SimpleItem
from Products.ZSQLMethods.SQL import SQL
from datetime import datetime, date, timedelta
from sha import sha
import uuid
import os
import time
from Globals import DTMLFile

global product_path
product_path = os.path.join(package_home(globals())) + '/'


class Eventos(SimpleItem):
    """alo"""

    "Factory"

    meta_type = 'evento'

    def obter_evento(self, id_evento=None):

        result = self._zsql_busca_eventos(
            id_lista=None, id_evento=id_evento)

        q = None

        if len(result) == 1:
            q = Evento(result[0])

        return q

    def obter_lista_evento(self, id_lista=None):

        result = self._zsql_busca_eventos(
            id_lista=id_lista, id_evento=None)

        q = []

        if len(result) > 0:
            for ev in result:
                temp = Evento(ev)
                q.append(temp)

        return q

    def get_all_from_lista(self, id_lista):
        return self.obter_lista_evento(id_lista=id_lista)

    def get_by_id(self, id_evento):
        return self.obter_evento(id_evento=id_evento)

    _zsql_busca_eventos = SQL(
        id='zsql_busca_evento', title='', connection_id='connection',
        arguments='id_lista\nid_evento', template=open(
            product_path + 'sql/zsql_busca_evento.sql').read()
    )


"""id_evento, id_lista, titulo_evento, data_inicio, data_fim, hora_inicio, 
       hora_fim, descricao, stamp, prioridade, id_usuario_criador, local_evento"""


class Evento(SimpleItem):
    """
        evento de uma lista da agenda
    """

    def __init__(self, list):
        self.id_evento = list["id_evento"]
        self.titulo_evento = list["titulo_evento"]
        self.hora_fim = list["hora_fim_form"]
        self.data_inicio = list["data_inicio_form"]
        self.data_fim = list["data_fim_form"]
        self.descricao = list["descricao"]
        self.prioridade = list["prioridade"]
        self.local_evento = list["local_evento"]
        self.hora_inicio = list["hora_inicio_form"]
