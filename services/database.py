import pyodbc

conn_str = 'DRIVER={SQL Server};SERVER=server_name;DATABASE=db_name;UID=your_username;PWD=your_password'

connection_string = 'DSN=YourDSNName;UID=your_username;PWD=your_password'

SERVER = 'FFW'
DATABASE = 'cadastro'
USERNAME = 'joaop'
PASSWORD = '97519242'
cnxn=pyodbc.connect('SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}')
cursor=cnxn.cursor()
