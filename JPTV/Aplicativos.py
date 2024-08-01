import streamlit as st
import pandas as pd 
import streamlit.components.v1 as components
import controllers.ClienteControllers as ClienteController
import models.Cliente as mdcliente


def Aplicativos():
    st.markdown('''## Acesso as Lojas de aplicativos''')
    colunas = st.columns((2,2,2))
    campos = ['Lojas','Download Direto','Codigo Downloader']
    for col, campo_nome in zip(colunas,campos):
          col.write(campo_nome)

    col1, col2,col3 = st.columns(3)
    
    with col1: 
        st.link_button('Loja de Aplicativos Live','https://aplicativos.live/')
        st.link_button('Loja de Aplicativos CW','https://w.stapps.cc/equipecw')
        st.link_button('Loja WPlay','https://lojawplay.com')
    with col2:
        st.link_button('Smarters Player - Windows','https://iptv-smarters-pro.br.uptodown.com/windows#google_vignette')
        st.link_button('Aplicativo IBOPLayer apk','http://ibodesk.com/media.apk')
        st.link_button('Aplicativo ibopro apk','http://ibodesk.com/ibopro.apk')
        st.link_button('Aplicativo iboprotv apk','http://ibodesk.com/iboprotv.apk')
        st.link_button('Aplicativo bobPlayer apk','http://ibodesk.com/bob.apk')

    with col3:
         st.write('VU Player Pro - ', '917475')
         st.write('CWPRO - ', '123625')
         st.write('Ibopromulti - ', '583650')
         st.write('Smartersmulti - ', '322957')
         st.write('unitv - ', '386140')
         st.write('Iptvsmarters - ', '78522')
         st.write('XCIPTV - ', '63207')

    # with col4:
    #      st.write('⚙️ DNS STB Wplay App:','15.204.233.167')
    #      st.write('⚙️ DNS STB TV Antiga:','149.56.44.24')
    #      st.write('⚙️ DNS STB V2:','198.50.195.225')
    #      st.write('⚙️ DNS STB V3:','104.194.10.27')
    #      st.write('⚙️ DNS STB v3²:','149.56.45.112')


def aplicativos():
    st.markdown('''## Acesso as Lojas de aplicativos''')
    colunas = st.columns((2,2,2))
    campos = ['DNS Warez','DNS Live','DNS Elite']
    for col, campo_nome in zip(colunas,campos):
          col.write(campo_nome)
          
          col4, col5,col6 = st.columns(3)
          with col4:
               st.write('VU Player Pro - ', '917475')
          with col5:
             st.write('VU Player Pro - ', '917475')
          with col6:
              st.write('VU Player Pro - ', '917475')
	
	
 	
	