import datetime

arquivo = './arquivo.txt'
transacoes = './transações.txt'
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
    hora = datetime.now().strftime('%d-%m-%Y')

    comprovante = open(transacoes, 'a', encoding='UTF-8')
    comprovante.writable()
    if(saqdep == 1):
        comprovante.writelines('Nome: {};Conta: {};Banco: {};saldo anterior: {};Saque: {};Novo saldo: {};Horario da transação: {};'.format(nome, conta, bco, saldo, saq, nsaldo, hora))
    else:
        comprovante.writelines('Nome: {};Conta: {};Banco: {};saldo anterior: {};Deposito: {};Novo saldo: {};Horario da transação: {};'.format(nome, conta, bco, saldo, dep, nsaldo, hora))
    comprovante.write('\n')
    comprovante.close()
    cadastro.close()

def verTransacoes():
    t = open(transacoes, 'r', encoding='UTF-8')
    for dados in t:
        print(dados.replace(';', '\n'), end = '')
    t.close

def menuPrincipal():
    menu = 'MENU PRINCIPAL'
    traco()
    print(menu.center(50),'\n\n')
    print('1 - NOVA OPERAÇÃO\n')
    print('2 - VER EXTRATO DAS OPERAÇÕES ANTERIORES\n')
    print('3 - SAIR DO PROGRAMA\n')
    print('\n')
    traco()
    opc = int(input('Escolha uma opcão: '))
    if(opc == 1):
        inicio()
    elif(opc == 2):
        verTransacoes()
    elif(opc == 3):
        print('Até a proxima!')
    else:
        print('Digite uma opção válida!')

def separador():
    separar = open(transacoes, 'r', encoding='UTF-8')
    
    soma = 0
    from datetime import datetime
    hora = datetime.now().strftime('%d-%m-%Y')
    for itens in separar:
       dado = itens.split(';')
       h = str(dado[6].replace('Horario da transação: ', ''))
       if('Saque: ' in itens and hora == h):
           d = float(dado[4].replace('Saque: ', ''))
           soma = soma + d
    
    print('A soma de todos os saques do dia {} é igual a {}!'.format(hora, soma))
    separar.close()

menuPrincipal()
separador()
