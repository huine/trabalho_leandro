from Globals import package_home
from Globals import DTMLFile
from OFS.SimpleItem import Item, SimpleItem
from Products.ZSQLMethods.SQL import SQL
from datetime import datetime, date, timedelta
from Products.agenda.usuarios.Usuario import Usuarios
from Products.agenda.senha.Senha import Senhas
from Products.agenda.UI.ui import Ui
from Products.agenda.Login.SessionCtrl.SessionCtrl import Session
import os

global product_path
product_path = os.path.join(package_home(globals())) + '/'


class Acesso(SimpleItem):

    """
        classe acesso
    """
    usr = Usuarios()
    pwd = Senhas()
    ui = Ui()
    session = Session()

    def index_html(self):
        """exibe a pagina de login"""
        return self._index_html()

    def verifica_dados_form(self, dados=None):
        """faz a verificacao dos dados inseridos no form de login"""

        if not dados:
            dados = self.REQUEST.form

        try:
            dados_user = self.usr.get_by_email(email=dados['email'])
        except:
            dados_user = None

        if not dados_user:
            return self.prepara_erro({'erro': 'Usuario e/ou senha invalido'})

        senha_userdb = self.pwd.get_by_id(id_usuario=dados_user[0])

        senha_form = dados['senha']

        if self.pwd.get_decrypt(usr_senha=senha_form, senha_hash=senha_userdb):

            if self.validar_login(usuario=dados_user):

                hash_log = self.pwd.get_hash()

                if self.usr.logar_usuario(id_usuario=dados_user[0],
                                          hash_log=hash_log):

                    dados_user = self.usr.get_by_id(id_usuario=dados_user[0])

                    self.gravar_session(usuario=dados_user, hash_log=hash_log)

                    return self.login_success()
                else:
                    return self.prepara_erro({'erro': 'nao foi possivel'
                                              ' logar o usuario.'})
            else:
                self.gravar_session(usuario=dados_user,
                                    hash_log=self.pwd.get_hash())

                return self.login_success()
                # return self.prepara_erro({'erro': 'Usuario ja esta logado.'})
        else:
            return self.prepara_erro({'erro': 'Usuario e/ou senha invalido'})

    def login_success(self):
        """
            se o login for bem sucedido,
            redireciona para a pagina principal
        """
        return self.REQUEST.RESPONSE.redirect('/agenda/main_page/')

    def gravar_session(self, usuario, hash_log):
        self.session.set_vars(usuario=usuario, hash=hash_log)

    def validar_login(self, usuario):
        """ realiza a validacao dos dados antes do login"""
        if usuario[3] is True:
            return False

        if usuario[4] is not None:
            return False

        return True

    def prepara_erro(self, dicionario):
        self.ui.set_on_request(dicionario=dicionario)
        return self.index_html()

    def prepara_erro_cadastro(self, dicionario):
        self.ui.set_on_request(dicionario=dicionario)
        return self.REQUEST.RESPONSE.redirect('/agenda/acesso/cadastro')

    def novo_usuario(self):
        """criar um novo usuario"""
        return self.cadastro()

    def verifica_cadastro(self, dados=None):
        """faz a verificacao dos dados no form de cadstro"""

        if not dados:
            dados = self.REQUEST.form

        if dados is None:
            self.prepara_erro_cadastro(
                dicionario={'erro': 'Preencha todos os campos.'})

        if 'voltar' in dados.keys():
            return self.index_html()

        campos_obrigatorios = ['email', 'conf_email', 'senha', 'conf_senha',
                               'primeiro_nome', 'sobrenome', 'uf', 'cidade',
                               'sexo', 'rua', 'numero', 'data_nasc']
        falta = []

        erro = 'Por favor, preencha os campos:\n '

        for c in campos_obrigatorios:
            if c not in dados.keys():
                falta.append(c)
            elif len(dados[c]) == 0:
                falta.append(c)
            else:
                pass

        if len(falta) > 0:
            for i in falta:
                if i == falta[-1]:
                    erro = erro + i + '.'
                else:
                    erro = erro + i + ', '
            self.prepara_erro_cadastro({'erro': erro})

        nome_usuario = dados['primeiro_nome'] + ' ' + dados['sobrenome']

        if dados['email'] != dados['conf_email'] or\
                dados['senha'] != dados['conf_senha']:
            erro = 'E-mail e/ou senha estao diferentes de suas confirmacoes.'
            self.prepara_erro_cadastro({'erro': erro})

        senha = self.pwd.get_crypt(dados['senha'])

        cadastro = self.usr.cadastrar_usuario(email=dados['email'],
                                              senha=senha,
                                              nome=nome_usuario,
                                              uf=dados['uf'],
                                              cidade=dados['cidade'],
                                              sexo=dados['sexo'],
                                              rua=dados['rua'],
                                              numero=dados['numero'],
                                              data_nasc=dados['data_nasc'],
                                              bairro=dados['bairro'],
                                              complemento=dados['complemento'])

        if cadastro is None:
            self.prepara_erro_cadastro(
                {'erro': 'Nao foi possivel criar o usuario.'})
        elif cadastro == 0:
            self.prepara_erro_cadastro({'erro': 'Nao foi possivel concluir o cadstro.' +
                                        ' Tente novamente mais tarde.'})
        else:
            hash_log = self.pwd.get_hash()

            if self.usr.logar_usuario(id_usuario=cadastro[0],
                                      hash_log=hash_log):

                dados_user = self.usr.get_by_id(id_usuario=cadastro[0])

                self.gravar_session(usuario=dados_user, hash_log=hash_log)

                return self.login_success()
            else:
                return self.prepara_erro_cadastro({'erro': 'nao foi possivel'
                                                   ' logar o usuario.'})

    _index_html = DTMLFile('dtml/index', globals())
    login_box = DTMLFile('dtml/login_box', globals())
    cadastro = DTMLFile('dtml/cadastro', globals())
    _erro = DTMLFile('../dtml/error', globals())
