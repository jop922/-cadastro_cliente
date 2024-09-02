#import de bibliotecas
import streamlit as st

#import de arquivos
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
    """, unsafe_allow_html=True
)

with st.container():
    st.markdown('***<p class="header"> Gerenciamento de Clientes </p>***', unsafe_allow_html=True)

image_path = 'LOGO.png'
st.sidebar.image(image_path, width=70, use_column_width=False)
st.sidebar.title('Menu')

JPTV = st.sidebar.selectbox('Selecione a opção', ['Usuario', 'Meus Usuarios', 'Paineis', 'Aplicativos'])

# Inicializar variáveis de estado
if 'ID_user' not in st.session_state:
    st.session_state.ID_user = None

# Cadastrar novo cliente
if JPTV == 'Usuario':
    st.session_state.ID_user = None  # Reseta o estado de ID_user ao mudar para a página de inserção
    pginserir.Adicionar()

# Consulta de clientes
elif JPTV == 'Meus Usuarios':
    pgconsulta.Consulta()
    pgconsulta.exportar()

# Gestão de acessos aos paineis
elif JPTV == 'Paineis':
    pgpaineis.Paineis()

# Galeria de aplicativos
elif JPTV == 'Aplicativos':
    pgaplicativos.Aplicativos()
