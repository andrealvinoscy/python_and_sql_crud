# Tentativa crud 01
import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="(removi)",
    database="agenda_contatos"
)

cursor = conexao.cursor()

def add_contatos():
    nome_contato = input('Nome: ')
    while nome_contato == "":
        nome_contato = input('Nome é obrigatório. Digite novamente: ')

    email_contato = input('E-mail: ')

    celular_contato = input('Celular: ')
    while celular_contato == "":
        celular_contato = input('Celular é obrigatório. Digite novamente: ')

    telefone_contato = input('Telefone: ')

    sql = "INSERT INTO contatos (nome, email, celular, telefone) VALUES (%s, %s, %s, %s)"
    valores = (nome_contato, email_contato, celular_contato, telefone_contato)

    cursor.execute(sql, valores)
    conexao.commit()

    print("Contato adicionado com sucesso!")

add_contatos()
