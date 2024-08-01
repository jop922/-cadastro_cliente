import JPTV.gestor as pgconsulta

class Cliente:

    def __init__(self, ID_user, nome, user, senha, venc, serv):
        self.ID_user=ID_user
        self.nome=nome
        self.user=user
        self.senha=senha
        self.venc=venc
        self.serv=serv
