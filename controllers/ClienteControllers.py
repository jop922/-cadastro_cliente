import services.database as db

def incluir(cliente):
    count = db.cursor.execute("""
    INSERT INTO SalesLT.Product (clinome, cliuser, clisenha, clivenc, cliserv)
    VALUES(?,?,?,?,?)""",
    cliente.nome,cliente.user,cliente.senha,cliente.venc,cliente.serv).rowcount
    db.cnxx.commit()