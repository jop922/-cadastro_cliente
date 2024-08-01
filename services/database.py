import pyodbc
import pandas as pd


server = 'JOAO'
database = 'cadastro_cliente'
username = 'Joao'
password = '97519242'
cnxn=pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=JOAO;DATABASE=cadastro_cliente;Trusted_connection=yes')
cursor=cnxn.cursor()