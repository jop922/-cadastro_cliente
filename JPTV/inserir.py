import streamlit as st
import streamlit.components.v1 as components
import controllers.ClienteControllers as ClienteController
import models.Cliente as mdcliente
import JPTV.gestor as pgconsulta




def Adicionar():
    ID_alterado = st.experimental_get_query_params()
    st.experimental_set_query_params()
    recuperado = None
    if ID_alterado.get('ID_user') != None:
        ID_alterado=ID_alterado.get('ID_user')[0]
        recuperado=ClienteController.selecionarID(ID_alterado)
        st.experimental_set_query_params(
            ID_user=[recuperado.ID_user]
        )

        st.title('Alterar Cliente')
      
    else:
        st.title('Inserir Cliente')

    with st.form(key='includecliente'):
        listserv=['','Warez', 'Live', 'Elite']
        
        
        if recuperado==None:
            input_nome=st.text_input(label='Insira o nome do cliente')
            input_user=st.text_input(label='Insira o Usuario')
            input_senha=st.text_input(label='Insira a senha',type='password')
            input_venc=st.date_input("Insira o Vencimento",value=None, format='DD/MM/YYYY')
            input_serv=st.selectbox(label='Selecione o Servidor',options=listserv) 
        else:
            input_nome=st.text_input(label='Insira o nome do cliente',value=recuperado.nome)
            input_user=st.text_input(label='Insira o Usuario',value=recuperado.user)
            input_senha=st.text_input(label='Insira a senha',type='password',value=recuperado.senha)
            input_venc = st.date_input("Insira o Vencimento")
            input_serv=st.selectbox(label='Selecione o Servidor',options=listserv,index=listserv.index(recuperado.serv))
        input_button_subtmit=st.form_submit_button(label='Enviar')
        
    if input_button_subtmit:
        if recuperado==None:
            ClienteController.incluir(mdcliente.Teste(0,input_nome,input_user,input_senha,input_venc,input_serv))
            st.success('Usuario Cadastrado com sucesso!')
 
        else:
            st.experimental_set_query_params()   
            ClienteController.alterar(mdcliente.Teste(recuperado.ID_user,input_nome,input_user,input_senha,input_venc,input_serv))
            st.success('Usuario Alterado com sucesso!')
