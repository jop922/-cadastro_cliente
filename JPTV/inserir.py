import streamlit as st
import pandas as pd 
import streamlit.components.v1 as components
import controllers.ClienteControllers as ClienteController
import models.Cliente as cliente


def incluir():
    with st.form(key='inserir_cliente'):
        input_nome=st.text_input(label='Insira o nome do cliente')
        input_user=st.text_input(label='Insira o Usuario')
        input_senha=st.text_input(label='Insira a senha')
        input_venc=st.date_input("Insira o Vencimento", value=None, format="DD/MM/YYYY")
        input_serv=st.selectbox(label='Selecione o Servidor',options=['Warez', 'Live', 'Elite'])
        input_button_subtmit=st.form_submit_button(label='Adicionar Usuario')

    if input_button_subtmit:
        
        cliente.nome = input_nome
        cliente.user = input_user
        cliente.senha = input_senha
        cliente.venc= input_venc
        cliente.serv = input_serv

        ClienteController.incluir(cliente.Cliente(0,input_nome,input_user,input_senha,input_venc,input_serv))
        st.success('Usuario Cadastrado com sucesso!')