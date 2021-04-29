import sqlite3

conn = sqlite3.connect('jogos/DataBase.bd')
cursor = conn.cursor()

def criarTabelaJogo():
    conn.execute("""create table if not exists Jogo(
                id_jogo integer primary key autoincrement,
                usuario txt not null,
                nome text not null,
                tempojogado float not null,
                conquistas int,
                finalizado int,
                data txt not null)""")

def inserirJogo(usuario, nome, tempojogado, conquistas, finalizado,data):
    conn.execute('insert into Jogo (usuario,nome,tempojogado,conquistas,finalizado,data) values(?,?,?,?,?,?)',(usuario, nome,tempojogado,conquistas,finalizado,data))
    conn.commit()

def exibirJogo():
    return conn.execute('select * from Jogo')

def atualizarNomeJogo(nome, id_jogo):
    conn.execute('update Jogo set nome = ? where id_jogo = ?',(nome, id_jogo))
    conn.commit()

def atualizarTempojogadoJogo(tempojogado, id_jogo):
    conn.execute('update Jogo set tempojogado = ? where id_jogo = ?',(tempojogado, id_jogo))
    conn.commit()

def atualizarConquistasJogo(conquistas, id_jogo):
    conn.execute('update Jogo set conquistas = ? where id_jogo = ?',(conquistas, id_jogo))
    conn.commit()

def atualizarFinalizadoJogo(finalizado, id_jogo):
    conn.execute('update Jogo set finalizado = ? where id_jogo = ?',(finalizado, id_jogo))
    conn.commit()

def deletarJogo(id_jogo):
    conn.execute('delete from Jogo where id_jogo = ?',(id_jogo, ))
    conn.commit()

def criarTabelaJogador():
    conn.execute("""create table if not exists Jogador(
                id_jogador integer primary key autoincrement,
                usuario text not null,
                senha varchar(12) not null)""")

def inserirJogador(usuario, senha):
    conn.execute('insert into Jogador (usuario, senha) values(?,?)',(usuario, senha))
    conn.commit()

def exibirJogador():
    return conn.execute('select * from Jogador')

def atualizarUsuarioJogador(usuario, id_jogador):
    conn.execute('update Jogador set usuario = ? where id_jogador = ?',(usuario, id_jogador))
    conn.commit()

def atualizarSenhaJogador(senha, id_jogador):
    conn.execute('update Jogador set senha = ? where id_jogador = ?',(senha, id_jogador))
    conn.commit()

def excluirJogador(id_jogador):
    conn.execute('delete from Jogador where id_jogador = ?',(id_jogador, ))
    conn.commit()
