from Globals import package_home
from Globals import DTMLFile
from OFS.SimpleItem import Item, SimpleItem
from Products.ZSQLMethods.SQL import SQL
from datetime import datetime, date, timedelta
from Products.agenda.usuarios.Usuario import Usuarios
# from Products.agenda.senha.Senha import Senhas
import os

global product_path
product_path = os.path.join(package_home(globals())) + '/'

class Acesso(SimpleItem):

    def pg_login(self):
        index_html = DTMLFile('dtml/index', globals())
        return index_html()
