import streamlit as st
import pandas as pd 
import streamlit.components.v1 as components
import controllers.ClienteControllers as ClienteController
import models.Cliente as cliente

def consultar():
    colunas = st.columns((1,1,1,1,1,1,1))
    campos = ['Nº','Nome','Usuario','Senha','Vencimento','Servidor', 'excluir']
    for col, campo_nome in zip(colunas,campos):
        col.write(campo_nome)

    for item in ClienteController.selecionartodos():
        col1,col2,col3,col4,col5,col6,col7 = st.columns((1,1,1,1,1,1,1))
        col1.write(item.ID_user)   
        col2.write(item.nome)   
        col3.write(item.user)   
        col4.write(item.senha)   
        col5.write(item.venc)   
        col6.write(item.serv)   
        button_space=col7.empty()
        on_click=button_space.button('Excluir','btnexcluir' + str(item.ID_user))   





    # costumerList = []

    #for item in ClienteController.selecionartodos():
    #     costumerList.append([item.nome, item.user, item.senha, item.venc, item.serv])

    # df=pd.DataFrame(
    #     costumerList,
    #     columns=['Nome', 'Usuario', 'Senha', 'Vencimento', 'Servidor']
    # )
    # st.table(df)


