from os import write
import streamlit as st
from numpy.core.fromnumeric import size   
import controllers.ClienteControllers as ClienteController
import models.cliente as cliente


st.title('Gerenciamento de Clientes JPTV')
st.sidebar.title('Menu')

paginaselecionada=st.sidebar.selectbox('Selecione a opção',['Inserir Cliente', 'Gerenciar Cliente'])

if paginaselecionada == 'Inserir Cliente':
    with st.form(key='inserir_cliente'):
        input_nome=st.text_input(label='Insira o nome do cliente')
        input_user=st.text_input(label='Insira o Usuario')
        input_senha=st.text_input(label='Insira a senha')
        input_venc=st.text_input(label='Insira a data de Vencimento')
        input_serv=st.selectbox(label='Selecione o Servidor',options=['Warez', 'Live', 'Elite'])
        input_button_subtmit=st.form_submit_button(label='Adicionar Usuario')

    if input_button_subtmit:
        st.write('Usuario Cadastrado com sucesso!')
        cliente.nome = input_nome
        cliente.user = input_user
        cliente.senha = input_senha
        cliente.venc= input_venc
        cliente.serv = input_serv

        ClienteController.incluir(cliente)


    elif paginaselecionada == 'Gerenciar Cliente':
        st.title('Gerenciar Cliente')
