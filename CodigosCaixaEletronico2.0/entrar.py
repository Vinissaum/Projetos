import caixaeletronico.bd as bd
import caixaeletronico.codigos as cod
import caixaeletronico.menu as men

def titulo():
    title = 'MENU DE CADASTRO/ENTRADA'
    print(title.center(50))

def opcoes():
    print('1 - Criar conta\n2 - Acessar conta\n3 - Encerrar\n')

def traco():
    linha = '*'
    print(linha*50)

def menu():
    traco()
    titulo()
    traco()
    opcoes()
    choose()

def choose():
    escolha = str(input('O que deseja fazer?: ')).lower()
    if(escolha == '1' or escolha == 'criar' or escolha == 'cadastrar' or escolha == 'criarconta' or escolha == 'criar conta'):
        cod.adicionarCliente()
        menu()
    elif(escolha == '2' or escolha == 'acessar' or escolha == 'entrar' or escolha == 'acessarconta' or escolha == 'acessar conta'):
        cod.validar()
        return
    else:
        print('Opção inválida, porfavor escolha uma opção válida!')
        choose()

bd.criarTabelaCliente()
menu()