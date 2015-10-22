from OFS.SimpleItem import SimpleItem
from Globals import DTMLFile
from Products.ZPsycopgDA.DA import Connection


class Agenda(SimpleItem):
    """Esta classe reunira' todas as configuracoes necessarias
    para o funcionamento da agenda.

    """
    meta_type = 'Agenda'

    manage_options = (
                {'label': 'View', 'action': 'index_html'},
        )


    manage_config = DTMLFile('dtml/manage_config', globals())

    index_html = DTMLFile('dtml/index', globals())



    def __init__(self, id, connection):
        """ Initialize """
        self.id = id
        self.connection = connection
        # self.view = getattr(self, 'view')

    def get_database_connection(self):
        """Database Connection"""
        return self.connection

    def manage_edit(self, connection, RESPONSE):
        "Atualiza as configuracoes da agenda"
        conexao = getattr(self, connection).connection_string
        self.connection = Connection(
            'connection',                   # ID
            'conexao com o banco',  # Title
            conexao,                        # string connection
            None,                           # zdatetime, None = datetime/python
            encoding='ISO-8859-1')
        self._p_changed = 1
        RESPONSE.redirect('manage_config')


def manage_addAgenda(self, id, connection, RESPONSE):
    """Add Agenda to a folder."""
    conn = getattr(self, connection)
    self._setObject(id, Agenda(id, conn))
    RESPONSE.redirect(id + '/index_html')

a = globals()
manage_addAgendaForm = DTMLFile('dtml/manage_addAgendaForm', a)
