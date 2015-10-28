from OFS.SimpleItem import SimpleItem
from Globals import DTMLFile
from Products.ZPsycopgDA.DA import Connection
from Products.agenda.Login.Acesso import Acesso


class Agenda(SimpleItem):
    """Esta classe reunira' todas as configuracoes necessarias
    para o funcionamento da agenda.

    """

    acesso = Acesso()

    meta_type = 'Agenda'

    manage_options = (
                {'label': 'View', 'action': 'inicia_processo_login'},
        )

    def __init__(self, id, connection):
        """ Initialize """
        self.id = id
        self.connection = connection

    def get_database_connection(self):
        """Database Connection"""
        return self.connection

    def inicia_processo_login(self):
        """Inicia o processo de login"""
        return self.acesso.pg_login()



def manage_addAgenda(self, id, connection, RESPONSE):
    """Add Agenda to a folder."""
    conn = getattr(self, connection)
    self._setObject(id, Agenda(id, conn))
    RESPONSE.redirect(id + '/index_html')



a = globals()

manage_addAgendaForm = DTMLFile('dtml/manage_addAgendaForm', a)
