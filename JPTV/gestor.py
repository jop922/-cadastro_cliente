import streamlit as st
import pandas as pd 
import pyodbc
from io import BytesIO

import controllers.ClienteControllers as ClienteController
# import models.Cliente as mdcliente
import JPTV.inserir as pginserir

def consultabd():
    query = 'SELECT ID_user, clinome, cliuser, clisenha, CONVERT(VARCHAR, clivenc, 103) AS vencimento, cliserv FROM cliente ORDER BY vencimento ASC'
    conn=pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=JOAO;DATABASE=cadastro_cliente;Trusted_connection=yes')
    df = pd.read_sql_query(query, conn)
    # Fechar a conexão
    conn.close()
    return df

def Consulta():
    df = consultabd()


    if 'ID_user' not in st.session_state:
        st.session_state.ID_user = None

    if st.session_state.ID_user is None:
        colunas = st.columns((1, 2, 2, 2, 2, 2, 2, 2))
        campos = ['Nº', 'Nome', 'Usuario', 'Senha', 'Vencimento', 'Servidor', 'Excluir', 'Alterar']
                
        for col, campo_nome in zip(colunas,campos):
            col.write(campo_nome)
        
        for index, row in df.iterrows():
            col1, col2, col3, col4, col5, col6, col7, col8 = st.columns((1, 2, 2, 2, 2, 2, 2, 2))
        
            col1.write(row['ID_user'])   
            col2.write(row['clinome'])   
            col3.write(row['cliuser'])   
            col4.write(row['clisenha'])
            col5.write(row['vencimento'])   
            col6.write(row['cliserv']) 
            button_space_Excluir=col7.empty()
            on_click_Excluir=button_space_Excluir.button('Excluir','btnDeletar' + str(row.ID_user))

            button_space_Alterar=col8.empty()
            on_click_Alterar=button_space_Alterar.button('Alterar','btnAlterar' + str(row.ID_user))
            if on_click_Excluir:
                ClienteController.deletar(row.ID_user)
                st.rerun()
            if on_click_Alterar:
                st.session_state.ID_user = row.ID_user
                st.rerun()
    else:    
        on_click_voltar = st.button('Voltar')
        if on_click_voltar:
            st.session_state.ID_user = None
            st.rerun()
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

