from OFS.SimpleItem import Item, SimpleItem
from Products.agenda.usuarios.Usuario import Usuarios
from Products.agenda.Login.SessionCtrl.SessionCtrl import Session
from Globals import DTMLFile
from Globals import package_home
import os

global product_path
product_path = os.path.join(package_home(globals())) + '/'


class Ui(SimpleItem):
    """classe que gerencia a UI"""

    meta_type = 'UI'

    usr = Usuarios()
    session = Session()

    manage_options = (
        (
            {'label': 'Contents', 'action': 'manage_main'},
        )
        + Item.manage_options
    )

    def index_html(self):
        """retorna a pagina principal da agenda"""
        return self.main_html()

    def set_on_request(self, dicionario={}):

        if len(dicionario) == 0:
            return False

        for key in dicionario.keys():
            self.REQUEST.set(key, dicionario[key])

        return True

    def deslogar(self):
        """Inicia o processo para deslogar usuario"""
        if len(self.REQUEST.SESSION.keys()) > 0:
            if self.REQUEST.SESSION['usuario_logado']:
                if self.usr.deslogar_usuario(
                        id_usuario=self.REQUEST.SESSION['id_usuario']):

                    self.session.clear_vars()

                    self.REQUEST.RESPONSE.redirect('/agenda/acesso/index_html')

        self.REQUEST.RESPONSE.redirect('/agenda/acesso/index_html')

    main_html = DTMLFile('dtml/main', globals())
