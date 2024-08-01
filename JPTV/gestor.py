import streamlit as st
import pandas as pd 
import services.database as db
import streamlit.components.v1 as components
import controllers.ClienteControllers as ClienteController
import models.Cliente as mdcliente
import JPTV.inserir as pginserir
from io import BytesIO
from datetime import datetime
import pyodbc


def consultabd():
    query = 'SELECT ID_user, clinome, cliuser, clisenha, CONVERT(VARCHAR, clivenc, 103) AS vencimento, cliserv FROM cliente'
    conn=pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=JOAO;DATABASE=cadastro_cliente;Trusted_connection=yes')
    df = pd.read_sql_query(query, conn)
    # Fechar a conexão
    conn.close()
    return df

def Consulta():
    
    param_id = st.experimental_get_query_params()
    if param_id =={}:
        colunas = st.columns((1,2,2,2,2,2,2,2))
        campos = ['Nº','Nome','Usuario','Senha','Vencimento','Servidor', 'Excluir','Alterar']
        
        for col, campo_nome in zip(colunas,campos):
            col.write(campo_nome)
        
        for x, item in enumerate(ClienteController.selecionartodos()):
            col1,col2,col3,col4,col5,col6,col7,col8 = st.columns((1,2,2,2,2,2,2,2))

            col1.write(item.ID_user)   
            col2.write(item.nome)   
            col3.write(item.user)   
            col4.write(item.senha)
            col5.write(item.venc)   
            col6.write(item.serv)   
            button_space_Excluir=col7.empty()
            on_click_Excluir=button_space_Excluir.button('Excluir','btnDeletar' + str(item.ID_user))

            button_space_Alterar=col8.empty()
            on_click_Alterar=button_space_Alterar.button('Alterar','btnAlterar' + str(item.ID_user))
            if on_click_Excluir:
                ClienteController.deletar(item.ID_user)
                st.experimental_rerun()
            if on_click_Alterar:
                st.experimental_set_query_params(
                    ID_user=[item.ID_user])
                st.experimental_rerun()
    else:    
        on_click_voltar=st.button('Voltar')
        if on_click_voltar:
            st.experimental_set_query_params()
            st.experimental_rerun()
        pginserir.Adicionar()

# Função principal da aplicação
def exportar():
    st.title("Exportar base de dados")
    # Carregar os dados
    df = consultabd()
 # Interação com o usuário
    if st.button('Exportar clientes'):
        download = BytesIO()
        df.to_excel(download,index=False)
        download.seek(0)
        st.download_button(
            label="Download",
            data=download,
            file_name='Clientes.xlsx',
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )

if __name__ == "__main__":
    exportar()

