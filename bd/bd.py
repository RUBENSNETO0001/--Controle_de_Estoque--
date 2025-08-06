import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host='localhost',
        database='estoque',
        user='root',
        password=''
    )
    if conexao.is_connected():
        print("Conexão bem sucedida")
        return conexao
    return None

def fechar_conexao(conexao, cursor):
    if cursor:
        cursor.close()
    if conexao and conexao.is_connected():
        conexao.close()