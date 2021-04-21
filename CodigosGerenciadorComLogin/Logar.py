import jogos.bd as bd
import jogos.menu as men
import jogos.programa as prog

def traco():
    linha = '*'
    print(linha*50)

def titulo():
    title = 'MENU DE LOGIN'
    print(title.center(50))

def opcoes():
    print('1 - Cadastrar\n2 - Logar\n3 - Sair')

def logar():
    traco()
    titulo()
    traco()
    opcoes()
    traco()
    escolha()

def escolha():
    escolhe = str(input('O que gostaria de fazer?: ')).lower()
    if(escolhe == '1' or escolhe == 'cadastrar'):
        prog.cadastrarUsuario()
        logar()
    elif(escolhe == '2' or escolhe == 'logar'):
        prog.validarUsuario()
    elif(escolhe == '3' or escolhe == 'sair'):
        print('saindo...')
        exit()
    else:
        print('Opção inválida! Por favor, escolha uma opção válida! Opções Válidas [//1 - Cadastrar//2 - Logar//3 - Sair//]')
        escolha()

bd.criarTabelaJogo()
bd.criarTabelaJogador()
logar()
