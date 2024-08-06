#import de bibliotecas
import streamlit as st

#import de arquivos
# import controllers.ClienteControllers as ClienteController
# import models.Cliente as mdcliente
import JPTV.inserir as pginserir
import JPTV.gestor as pgconsulta
import JPTV.Paineis as pgpaineis
import JPTV.Aplicativos as pgaplicativos

st.markdown("""
    <style>
    .header {
        font-size:60px !important;
        color: #e63633;
            
        }
    </style>
    """,
    unsafe_allow_html=True
)
with st.container():
    st.markdown('***<p class="header"> Gerenciamento de Clientes </p>***', unsafe_allow_html=True)

image_path = 'LOGO.png'
st.sidebar.image(image_path, width=70, use_column_width=False)
st.sidebar.title('Menu')

JPTV=st.sidebar.selectbox('Selecione a opção',['Usuario', 'Meus Usuarios','Paineis', 'Aplicativos'])


#cadastrar novo cliente
if JPTV == 'Usuario':
    st.experimental_set_query_params()
    pginserir.Adicionar()


  
# Consulta de clientes
if JPTV == 'Meus Usuarios':
    pgconsulta.Consulta()
    pgconsulta.exportar()


# Gestão de acessos aos paineis
if JPTV == 'Paineis':
    pgpaineis.Paineis()


# galeria de aplicativos
if JPTV == 'Aplicativos':
    pgaplicativos.Aplicativos()