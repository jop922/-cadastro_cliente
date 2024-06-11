import streamlit as st;

with st.form(key='incluir_cliente'):
    input_nome=st.text_input(label='Insira o nome do cliente')
    input_user=st.text_input(label='Insira o Usuario')
    input_senha=st.text_input(label='Insira a senha')
    input_venc=st.text_input(label='Insira a data de Vencimento')
    input_serv=st.selectbox(label='Selecione o Servidor',options=['Warez', 'Live', 'Elite'])
    input_button_subtmit=st.form_submit_button(label='Adicionar Usuario')

