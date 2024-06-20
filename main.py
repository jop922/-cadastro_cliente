import streamlit as st
import datetime

st.title('Informe uma data')
venc = st.date_input("When's your birthday", value=None, format="DD/MM/YYYY")



