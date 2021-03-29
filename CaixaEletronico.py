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
    banco.writelines('1 - Bradesco\n2 - Santander\n3 - Itaú\n4 - Banco do Brasil\n')
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
    condition = True
    while condition:
        bcoi = str(input('Escolha seu banco: ')).lower()
        if(bcoi == '1' or bcoi == 'bradesco'):
            bco = 'Bradesco'
            condition = False
        elif(bcoi == '2' or bcoi == 'santander'):
            bco = 'Santander'
            condition = False
        elif(bcoi == '3' or bcoi == 'itau' or bcoi == 'itaú' ):
            bco = 'Itaú'
            condition = False
        elif(bcoi == '4' or bcoi == 'banco do brasil'):
            bco = 'Banco do Brasil'
            condition = False
        else:
            print('Opção inválida!')
    print('O banco selecionado foi o {}!'.format(bco))
    condition = True
    while condition:
        saldoopc = str(input('Deseja inserir um saldo em sua conta? [s/n]: ')).lower()
        if (saldoopc=='s' or saldoopc=='sim'):
            saldo = float(input('Digite a quantia que deseja adicionar: '))
            condition = False
        elif(saldoopc == 'n' or saldoopc=='nao' or saldoopc == 'não' ):
            saldo = 0
            condition = False
        else:
            print("Digite uma opção válida!")
    
    condition = True    
    
    while condition:
        saqueopc = str(input('Deseja fazer um saque ou deposito?[s/n]: ')).lower()
        if (saqueopc =='s' or saqueopc=='sim'):
            saqdep = int(input('Digite 1 para saque e 2 para deposito: '))
            condition = False
        elif(saqueopc == 'n' or saqueopc == 'nao' or saqueopc == 'não'):
            print('Tenha um bom dia, volte sempre!')
            condition = False
            return
        else:
            print("Digite uma opção válida!")        
  
    if (saqdep == 1):
        saq = float(input('Digite quanto deseja sacar: '))
        if(saldo > saq):
            nsaldo = saldo - saq            
        else:
            print('Você não tem saldo suficiente em conta para um saque de {} reais. Seu saldo atual é de {} reais!'.format(saq, saldo))
            saq = float(0.0)
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
        comprovante.writelines('Nome: {};Conta: {};Banco: {};saldo anterior: {};Saque: {};Novo saldo: {};Data da transação: {};'.format(nome, conta, bco, saldo, saq, nsaldo, hora))
    else:
        comprovante.writelines('Nome: {};Conta: {};Banco: {};saldo anterior: {};Deposito: {};Novo saldo: {};Data da transação: {};'.format(nome, conta, bco, saldo, dep, nsaldo, hora))
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
    condition = True
    while condition:
        opc = str(input('Escolha uma opcão: '))
        if(opc == '1'):
            inicio()
            condition = False
        elif(opc == '2'):
            verTransacoes()
            condition = False
        elif(opc == '3'):
            print('Até a proxima!')
            condition = False
        else:
            print('Digite uma opção válida!')

def separador():
    separar = open(transacoes, 'r', encoding='UTF-8')
    
    soma = 0
    from datetime import datetime
    hora = datetime.now().strftime('%d-%m-%Y')
    for itens in separar:
       dado = itens.split(';')
       h = str(dado[6].replace('Data da transação: ', ''))
       if('Saque: ' in itens and hora == h):
           d = float(dado[4].replace('Saque: ', ''))
           soma = soma + d
    
    print('A soma de todos os saques do dia {} é igual a {}!'.format(hora, soma))
    separar.close()

menuPrincipal()
separador()
