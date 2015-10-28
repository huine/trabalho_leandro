from OFS.SimpleItem import SimpleItem
from Globals import DTMLFile
from Globals import package_home
import os

global product_path
product_path = os.path.join(package_home(globals())) + '/'


class Ui(SimpleItem):
    """classe que gerencia a UI"""

    def pg_principal(self):
        """retorna a pagina principal"""
        return main_html()

    main_html = DTMLFile('dtml/main', globals())
