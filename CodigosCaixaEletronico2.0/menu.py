import caixaeletronico.codigos as cod
import caixaeletronico.bd as bd

def titulo():
    title = 'MENU PRINCIPAL'
    print(title.center(50))

def opcoes():
    print('1 - Ver detalhes\n2 - Depositar\n3 - Sacar\n4 - Encerrar sessão\n')

def traco():
    linha = '*'
    print(linha*50)

def menu(cpf, nome):
    print('Bem vindo {}!'.format(nome))
    traco()
    titulo()
    traco()
    opcoes()
    choose(cpf, nome)

def choose(cpf, nome):
    escolha = str(input('O que deseja fazer?: ')).lower()
    if(escolha == '1' or escolha == 'detalhes' or escolha == 'verdetalhes' or escolha == 'ver detalhes'):
        for dado in bd.exibirCliente():
            cpfcomparar = str(dado[0])
            if(cpf == cpfcomparar):
                print('CPF: {}\nNome: {}\nAgencia: {}\nConta: {}\nSaldo: {}\n'.format(dado[0],dado[1],dado[2],dado[3],dado[4]))
        menu(cpf, nome)
    elif(escolha == '2' or escolha == 'deposito' or escolha == 'dep' or escolha == 'depositar'):
        traco()
        print('1 - Minha conta\n2 - Outra conta')
        traco()
        cod.depositar(cpf, nome)
        menu(cpf, nome)
    elif(escolha == '3' or escolha == 'saque' or escolha == 'saq' or escolha == 'sacar'):
        cod.sacar(cpf)
        menu(cpf, nome)
    elif(escolha == '4' or escolha == 'sair' or escolha == 'encerrar'):
        print('Encerrando sessão...')
        exit()
    else:
        print('Opção inválida, porfavor escolha uma opção válida!')
        choose(cpf, nome)