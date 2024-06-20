#import de bibliotecas
from os import write
import streamlit as st
import pandas as pd
from numpy.core.fromnumeric import size   
import streamlit.components.v1 as components

#import de arquivos
import controllers.ClienteControllers as ClienteController
import models.Cliente as cliente
import JPTV.inserir as pginserir
import JPTV.gestor as pggestor


st.title('Gerenciamento de Clientes JPTV')
st.sidebar.title('Menu')
jptv=st.sidebar.selectbox('Selecione a opção',['Inserir Cliente', 'Gerenciar Cliente','Paineis', 'Aplicativos'])

#cadastrar novo cliente
if jptv == 'Inserir Cliente':
    pginserir.incluir()

    

# Gerenciamento do cliente já cadastrado
    # Consulta de clientes
if jptv == 'Gerenciar Cliente':
    pggestor.consultar()

# Gestão de acessos aos porais
# if jptv == 'Paineis':


# galeria de aplicativos
# if jptv == 'Aplicativos':

