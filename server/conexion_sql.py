import mysql.connector


def conecciones():
    # print("Entrando....")
    basededatos = mysql.connector.connect(host="localhost", user="root", password="ande18!", db="proyecto_carro", port=3306)
    # print('Database is Connected!')
    return basededatos