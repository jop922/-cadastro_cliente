import streamlit as st
import controllers.ClienteControllers as ClienteController
import models.cliente as mdcliente

def Adicionar():
    # Inicializar o estado de ID_user
    if 'ID_user' not in st.session_state:
        st.session_state.ID_user = None

    recuperado = None
    
    # Verificar se há um ID_user para alteração
    if st.session_state.ID_user is not None:
        ID_alterado = st.session_state.ID_user
        recuperado = ClienteController.selecionarID(ID_alterado)
        st.session_state.ID_user = recuperado.ID_user
        st.title('Alterar Cliente')
    else:
        st.title('Inserir Cliente')

    with st.form(key='includecliente'):
        listserv = ['', 'Warez', 'Live', 'Elite']

        # Se recuperado é None, estamos inserindo um novo cliente
        if recuperado is None:
            input_nome = st.text_input(label='Insira o nome do cliente')
            input_user = st.text_input(label='Insira o Usuario')
            input_senha = st.text_input(label='Insira a senha', type='password')
            input_venc = st.date_input("Insira o Vencimento", value=None, format='DD/MM/YYYY')
            input_serv = st.selectbox(label='Selecione o Servidor', options=listserv) 
        else:
            # Preencher o formulário com os dados existentes
            input_nome = st.text_input(label='Insira o nome do cliente', value=recuperado.nome)
            input_user = st.text_input(label='Insira o Usuario', value=recuperado.user)
            input_senha = st.text_input(label='Insira a senha', type='password', value=recuperado.senha)
            input_venc = st.date_input("Insira o Vencimento")
            input_serv = st.selectbox(label='Selecione o Servidor', options=listserv, index=listserv.index(recuperado.serv))
        
        input_button_subtmit=st.form_submit_button(label='Enviar')
        
    if input_button_subtmit:
        if recuperado==None:
            ClienteController.incluir(mdcliente.Cliente(0, input_nome, input_user, input_senha, input_venc, input_serv))
            st.success('Usuario Cadastrado com sucesso!')
        else:
            st.session_state.ID_user = None  # Resetar o estado de ID_user após alteração
            ClienteController.alterar(mdcliente.Cliente(recuperado.ID_user, input_nome, input_user, input_senha, input_venc, input_serv))
            st.success('Usuario Alterado com sucesso!')
