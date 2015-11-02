#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
from OFS.SimpleItem import SimpleItem


class Session(SimpleItem):

    def clear_vars(self):
        SESSION = self.REQUEST.SESSION
        for k in SESSION.keys():
            del SESSION[k]

    def set_vars(self, usuario, hash):
        " Seta as variaveis da sessao "

        SESSION = self.REQUEST.SESSION

        SESSION.set('hash_login', hash)
        SESSION.set('id_usuario', usuario[0])
        SESSION.set('email_usuario', usuario[1])
        SESSION.set('tipo_usuario', usuario[2])
        SESSION.set('usuario_logado', usuario[3])
        SESSION.set('ip_usuario', usuario[4])

    # def _temAsSessoes(self, sessaoIdLista):
    #     r = False
    #     SESSION = self.REQUEST.SESSION
    #     for i in sessaoIdLista:
    #         r = (i in SESSION.keys() and SESSION[i]) and True or False
    #         if not r:
    #             break
    #     return r

    # def get_usuario(self):
    #     " Retorna o usuario (objeto da classe Usuario) da sessao "
    #     usr = self.REQUEST.SESSION.get('50', None)
    #     if usr:
    #         return self.usuarios.obterUsuario(usr)
    #     return None

    # def get_id_usuario(self):
    #     " Retorna a id do usuario da sessao "
    #     return self.REQUEST.SESSION.get('50', None)

    # def get_ip(self):
    #     ip_orig = self.REQUEST.get('REMOTE_ADDR')

    #     return ip_user

    # def deslogar(self):
    #     " Metodo para deslogar o usuario da sessao. "
    #     usr = self.get_usuario()

    #     if usr:
    #         self.clearVars()
    #         self.usuarios.armazenarUsuario(usr)

    #     return qtde_login

    # def estaLogado(self):
    #     """
    #     Metodo para verificar se um usuario esta logado
    #     """

    #     SESSION = self.REQUEST.SESSION

    #     if len(SESSION.keys()) == 0 or not SESSION['33']:
    #         return False
    #     return True
