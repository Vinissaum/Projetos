import sqlite3

conn = sqlite3.connect('compras/Banco.bd')
def criarTabelaCliente():
    conn.execute("""create table if not exists Clientes(
                    cpf text primaty key,
                    nome text,
                    email text) """)

def criarTabelaProdutos():
    conn.execute("""create table if not exists Produtos(
                    id_produto integer primary key autoincrement,
                    nome text,
                    quantidade int,
                    preco float) """) 

def inserirCliente(cpf, nome, email):
    conn.execute('insert into Clientes (cpf, nome, email) values(?, ?, ?)',(cpf, nome, email))
    conn.commit()

def inserirProduto(nome, quantidade, preco):
    conn.execute('insert into Produtos (nome, quantidade, preco) values(?, ?, ?)',(nome, quantidade, preco))
    conn.commit()

def verClientes():
    return conn.execute('select cpf, nome, email from Clientes')

def verProdutos():
    return conn.execute('select id_produto, nome, quantidade, preco from Produtos')

def atualizarNomeCliente(cpf, nome):
    conn.execute("update Clientes set nome = '{}' where cpf = '{}'".format(nome, cpf))
    conn.commit()

def atualizarEmailCliente(cpf, email):
    conn.execute("update Clientes set email = '{}' where cpf = '{}'".format(email, cpf))
    conn.commit()

def atualizarNomeProduto(id_produto, nome):
    conn.execute('update Produtos set nome = ? where id_produto = ?',(nome, id_produto))
    conn.commit()

def atualizarQuantidadeProduto(id_produto, quantidade):
    conn.execute('update Produtos set quantidade = ? where id_produto = ?',(quantidade, id_produto))
    conn.commit()

def atualizarPrecoProduto(id_produto, preco):
    conn.execute('update Produtos set preco = ? where id_produto = ?',(preco, id_produto))
    conn.commit()

def verProdutos():
    return conn.execute('select id_produto, nome, quantidade, preco from Produtos')

def verClientes():
    return conn.execute('select cpf, nome, email from Clientes')

def excluirProduto(id_produto):
    conn.execute('delete from Produtos where id_produto = ?',(id_produto))
    conn.commit()

def excluirCliente(cpf):
    conn.execute("delete from Clientes where cpf = '{}'".format(cpf))
    conn.commit()
