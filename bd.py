import sqlite3

conn = sqlite3.connect("gerenciar/Estoque.bd")
cursor = conn.cursor()

def CriarTabelaItens():
    conn.execute("""create table if not exists Estoque(
                    id_item integer primary key autoincrement,
                    item text,
                    quantidade int) """)

def inserirItens(item, quantidade):
    conn.execute('insert into Estoque (item, quantidade) values (?, ?)',(item, quantidade))
    conn.commit()

def lerItens():
   return conn.execute('select id_item, item, quantidade from Estoque')

def alterarItem(id_item, item):
    conn.execute('update Estoque set item = ? where id_item = ?',(item, id_item))
    conn.commit()

def alterarQuantidade(quantidade, id_item):
    conn.execute('update Estoque set quantidade = ? where id_item = ?',(quantidade, id_item))
    conn.commit()

def excluir_item(idenviar):    
    conn.execute('delete from Estoque where id_item = ?', (idenviar, ))
    conn.commit()
