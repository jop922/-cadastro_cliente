import models.Cliente as cliente
import services.database as db
from typing import List

def incluir(cliente):
    count = db.cursor.execute("""
    INSERT INTO cliente (clinome, cliuser, clisenha, clivenc, cliserv)
    VALUES(?,?,?,?,?)""",
    cliente.nome,cliente.user,cliente.senha,cliente.venc,cliente.serv).rowcount
    db.cnxn.commit()


def selecionartodos():
    db.cursor.execute('select * from cliente')
    costumerList=[]

    for row in db.cursor.fetchall():
        costumerList.append(cliente.Cliente(row[0],row[1],row[2],row[3],row[4],row[5]))
    return costumerList