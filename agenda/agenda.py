from OFS.SimpleItem import SimpleItem
from Globals import DTMLFile
from Products.ZPsycopgDA.DA import Connection
from Products.agenda.Login.Acesso import Acesso
from Products.agenda.UI.ui import Ui


class Agenda(SimpleItem):
    """Esta classe reunira' todas as configuracoes necessarias
    para o funcionamento da agenda.

    """

    acesso = Acesso()
    main_page = Ui()

    # padrao para todas as paginas
    header = DTMLFile('dtml/header', globals())
    footer = DTMLFile('dtml/footer', globals())
    css_header = DTMLFile('dtml/css/materialize.css', globals())
    materialize_js = DTMLFile('dtml/js/materialize.js', globals())

    meta_type = 'Agenda'

    manage_options = (
        {'label': 'View', 'action': 'login'},
    )

    def __init__(self, id, connection):
        """ Initialize """
        self.id = id
        self.connection = connection

    def get_database_connection(self):
        """Database Connection"""
        return self.connection

    def login(self):
        """redireciona para a pagina de login"""
        return self.REQUEST.RESPONSE.redirect('/agenda/acesso/index_html')


def manage_add_agenda(self, id, connection, RESPONSE):
    """Add Agenda to a folder."""
    conn = getattr(self, connection)
    self._setObject(id, Agenda(id, conn))
    RESPONSE.redirect(id + '/index_html')


a = globals()

manage_addAgendaForm = DTMLFile('dtml/manage_addAgendaForm', a)
