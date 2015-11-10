from OFS.SimpleItem import SimpleItem
from Products.agenda.usuarios.Usuario import Usuarios
from Products.agenda.Lista.Lista import Listas, Lista
from Products.agenda.Evento.Evento import Eventos
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
    lista = Listas()
    evento = Eventos()

    manage_options = (
        (
            {'label': 'Contents', 'action': 'manage_main'},
        )
    )

    def esta_logado(self):
        return self.session.estaLogado()

    def index_html(self):
        """retorna a pagina principal da agenda"""

        return self.main_2()

    def set_on_request(self, dicionario={}):

        if len(dicionario) == 0:
            return False

        for key in dicionario.keys():
            self.REQUEST.set(key, dicionario[key])

        return True

    """ def get_listas_usuario(self):
            # if(self.session.estaLogado()):
            # self.REQUEST.SESSION["id_usuario"])
            return self.lista.get_listas_by_usuario(18)
            # return None
    """

    def get_listas_usuario(self):
        listas = self.lista.get_listas_by_usuario(18)

        if listas is None:
            return []

        result = []

        for l in listas:
            temp = Lista(titulo=l['titulo'], id_lista=l[
                'id_lista'], eventos=self.evento.get_all_from_lista(int(l['id_lista'])))
            result.append(temp)

        return result

    def logoff(self):
        """Inicia o processo para deslogar usuario"""
        if len(self.REQUEST.SESSION.keys()) > 0:
            if self.REQUEST.SESSION['usuario_logado']:
                if self.usr.deslogar_usuario(
                        id_usuario=self.REQUEST.SESSION['id_usuario']):

                    self.session.clear_vars()

                    self.REQUEST.RESPONSE.redirect('/agenda/acesso/index_html')

        self.REQUEST.RESPONSE.redirect('/agenda/acesso/index_html')

    def prepara_erro(self, dicionario):
        self.set_on_request(dicionario=dicionario)
        return self._erro()

    def valida_lista(self, dados=None):
        """faz a verificacao dos dados inseridos no form de login"""

        return self.REQUEST
        if not dados:
            dados = self.REQUEST.form

        # if not self.session.estaLogado():
        #    return self.prepara_erro({'erro': ' usuario nao logado'})

        id_usuario = 18  # self.REQUEST.SESSION['id_usuario']
        try:
            titulo = dados['titulo']
        except:
            return self.prepara_erro({'erro': 'erro'})

        self.lista.add_lista(id_usuario=id_usuario, titulo=titulo)

        return self.REQUEST.RESPONSE.redirect('/agenda/login/')

    main_2 = DTMLFile('dtml/main_2', globals())
    main_html = DTMLFile('dtml/main', globals())
    add_card_modal = DTMLFile('dtml/add_card_modal', globals())
    add_lista_modal = DTMLFile('dtml/add_lista_modal', globals())
    card_div = DTMLFile('dtml/card_div', globals())
    card_info_modal = DTMLFile('dtml/card_info_modal', globals())
    lista_div = DTMLFile('dtml/lista_div', globals())
    _erro = DTMLFile('../dtml/error', globals())
