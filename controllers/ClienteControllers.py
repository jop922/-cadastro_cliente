import models.Cliente as mdcliente
import services.database as db
from typing import List
import pandas as pd
import streamlit as st 
import io
import pyodbc


#Incluir cliente na base de dados
def incluir(cliente):
    count = db.cursor.execute("""
    INSERT INTO cliente (clinome, cliuser, clisenha, clivenc, cliserv)
    VALUES(?,?,?,?,?)""",
    cliente.nome,cliente.user,cliente.senha,cliente.venc,cliente.serv).rowcount
    db.cnxn.commit()

# Excluir Cliente da base de dados
def deletar(ID_user):
    count = db.cursor.execute("""
    delete from cliente where ID_user = ? """,
    ID_user).rowcount
    db.cnxn.commit()


def selecionarID(ID_user):
    db.cursor.execute("""
    SELECT ID_user, clinome, cliuser, clisenha, CONVERT(VARCHAR, clivenc, 103) AS vencimento, cliserv 
    FROM cliente 
    WHERE ID_user = ?
    """, ID_user)
    costumerList=[]
    for row in db.cursor.fetchall():
        costumerList.append(mdcliente.Cliente(row[0],row[1],row[2],row[3],row[4],row[5]))
    return costumerList[0]


def alterar(cliente):
    count = db.cursor.execute("""
    update cliente
    SET clinome = ?, cliuser = ?, clisenha = ?, clivenc = ?, cliserv = ?
    WHERE ID_user = ?
    """,
    cliente.nome,cliente.user,cliente.senha,cliente.venc,cliente.serv, cliente.ID_user).rowcount
    db.cnxn.commit()
    st.experimental_rerun()

def selecionartodos():
    db.cursor.execute("""
    SELECT ID_user, clinome, cliuser, clisenha, CONVERT(VARCHAR, clivenc, 103) AS vencimento, cliserv 
    FROM cliente
    """)
    costumerList=[]
    for row in db.cursor.fetchall():
        costumerList.append(mdcliente.Cliente(row[0],row[1],row[2],row[3],row[4],row[5]))
    return costumerList
    st.rerun()


