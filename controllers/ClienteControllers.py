import models.Cliente as mdcliente
import services.database as db
from typing import List
import pandas as pd
import streamlit as st 


#Incluir cliente na base de dados
def incluir(teste):
    count = db.cursor.execute("""
    INSERT INTO teste (clinome, cliuser, clisenha, clivenc, cliserv)
    VALUES(?,?,?,?,?)""",
    teste.nome,teste.user,teste.senha,teste.venc,teste.serv).rowcount
    db.cnxn.commit()

# Excluir Cliente da base de dados
def deletar(ID_user):
    count = db.cursor.execute("""
    delete from teste where ID_user = ? """,
    ID_user).rowcount
    db.cnxn.commit()


def selecionarID(ID_user):
    db.cursor.execute("""
    SELECT ID_user, clinome, cliuser, clisenha, CONVERT(VARCHAR, clivenc, 103) AS vencimento, cliserv 
    FROM teste 
    WHERE ID_user = ?
    """, ID_user)
    costumerList=[]
    for row in db.cursor.fetchall():
        costumerList.append(mdcliente.Teste(row[0],row[1],row[2],row[3],row[4],row[5]))
    return costumerList[0]


def alterar(teste):
    count = db.cursor.execute("""
    update cliente
    SET clinome = ?, cliuser = ?, clisenha = ?, clivenc = ?, cliserv = ?
    WHERE ID_user = ?
    """,
    teste.nome,teste.user,teste.senha,teste.venc,teste.serv, teste.ID_user).rowcount
    db.cnxn.commit()
    st.experimental_rerun()

def selecionartodos():
    db.cursor.execute("""
    SELECT ID_user, clinome, cliuser, clisenha, clivenc, cliserv 
    FROM teste
    """)
    costumerList=[]
    for row in db.cursor.fetchall():
        costumerList.append(mdcliente.Teste(row[0],row[1],row[2],row[3],row[4],row[5]))
    return costumerList
    st.experimental_rerun()


