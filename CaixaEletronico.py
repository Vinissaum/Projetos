import datetime

arquivo = './arquivo.txt'

bancos = 'BANCOS DISPONIVEIS'
cadastrar = 'TELA DE CADASTRO'

def inicio():
    traco()
    print(cadastrar.center(50), '\n')
    add()
    traco() 


def traco():
    traco = '*'
    print(traco*50)

def banco():
    banco = open(arquivo, 'w', encoding='UTF-8')
    banco.writelines(' Bradesco\nSantander\nItaú\nBanco do Brasil\n')
    banco.write('\n')
    banco.close()
    lerbancos()

def lerbancos():
    banco = open(arquivo, 'r', encoding='UTF-8')
    for nome in banco:
        print(nome, end=' ')
    banco.close()

def verbancos():
    traco()
    print(bancos.center(50), '\n')
    banco()
    traco()

def add():
    cadastro = open(arquivo, 'a', encoding='UTF-8')
    cadastro.writable()
    nome = str(input('Digite seu nome completo: '))
    conta = int(input('Digite sua Conta: '))
    verbancos()
    bco = str(input('Escolha seu banco: '))
    saldoopc = str(input('Deseja inserir um saldo em sua conta? [s/n]: '))
    if (saldoopc=='s' or saldoopc=='S'):
        saldo = float(input('Digite a quantia que deseja adicionar: '))
    else:
        saldo = 0
        
    saqueopc = str(input('Deseja fazer um saque ou deposito?[s/n]: '))
    if (saqueopc =='s' or saqueopc=='S'):
        saqdep = int(input('Digite 1 para saque e 2 para deposito: '))
    else:
        print('Tenha um bom dia, volte sempre!')
        return
      
    if (saqdep==1):
        saq = float(input('Digite quanto deseja sacar: '))
        nsaldo = saldo - saq
    else:
        dep = float(input('Digite quanto deseja depositar: '))
        nsaldo = saldo + dep
    
    cadastro.write('\n')
    from datetime import datetime
    hora = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    comprovante = open('transações.txt', 'a', encoding='UTF-8')
    comprovante.writable()
    if(saqdep == 1):
        comprovante.writelines('Nome: {}\nConta: {}\nBanco: {}\nsaldo anterior: {}\nSaque: {}\nNovo saldo: {}\nHorario da transação: {}\n'.format(nome, conta, bco, saldo, saq, nsaldo, hora))
    else:
        comprovante.writelines('Nome: {}\nConta: {}\nBanco: {}\nsaldo anterior: {}\nDeposito: {}\nNovo saldo: {}\nHorario da transação: {}\n'.format(nome, conta, bco, saldo, dep, nsaldo, hora))
    comprovante.write('\n')
    comprovante.close()
    cadastro.close()

inicio()