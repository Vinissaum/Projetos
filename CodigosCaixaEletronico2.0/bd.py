import sqlite3

conn = sqlite3.connect("caixaeletronico/database.bd")
cursor = conn.cursor()

def criarTabelaCliente():
    conn.execute("""CREATE TABLE IF NOT EXISTS cliente(
                cpf TEXT PRIMARY KEY,
                nome TEXT NOT NULL,
                agencia TEXT,
                conta TEXT,
                saldo FLOAT,
                senha TEXT)""")

def inserirCliente(cpf, nome, agencia, conta, saldo, senha):
    conn.execute("INSERT INTO cliente (cpf, nome, agencia, conta, saldo, senha) values(?,?,?,?,?,?)",(cpf, nome, agencia, conta, saldo, senha))
    conn.commit()

def atualizarClienteSenha(senha, cpf):
    conn.execute("UPDATE cliente SET senha = {} WHERE cpf = {}".format(senha,cpf))
    conn.commit()

def atualizarClienteSaldo(saldo, cpf):
    conn.execute("UPDATE cliente SET saldo = {} WHERE cpf = {}".format(saldo,cpf))
    conn.commit()

def deletarCliente(cpf):
    conn.execute("DELETE FROM cliente WHERE cpf = {}".format(cpf))
    conn.commit()

def exibirCliente():
    return conn.execute("SELECT * FROM cliente")
