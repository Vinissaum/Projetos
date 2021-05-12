import caixaeletronico.bd as bd
import caixaeletronico.gerador as gerador
import caixaeletronico.menu as men
import caixaeletronico.codigos as cod

def adicionarCliente():    
    existe = int(0)
    condition = True
    while condition:
        validar = True
        while validar:
            while True:
                cpf = str(input('Entre com seu CPF: ')).strip()
                if not cpf:
                    print('O CPF não pode ficar em branco!')
                else:
                    break
            for dado in bd.exibirCliente():                
                cpfcomparar = str(dado[0])
                if(cpf == cpfcomparar):
                    while True:
                        entrar = str(input('Já existe uma conta com esse CPF! gostaria de acessa-la?: ')).lower()
                        if(entrar == 's' or entrar == 'sim'):
                            cod.validar()                            
                        elif(entrar == 'n' or entrar == 'nao' or entrar == 'não'):
                            print('Por favor, entre com outro CPF.')
                            existe = 1
                            break
                        else:
                            print('Opção inválida! Porfavor, insira uma opção válida! Opções válidas: [sim/não]')
                else:
                    existe = 0
                    validar = False
            if(existe == 0):
                validar = False
            elif(existe == 1):
                validar = True
        while True:
            nome = str(input('Entre com seu nome: ')).strip()
            if not nome:
                print('O nome não pode ficar em branco!')
            else:
                break
        while True:
            try:
                while True:
                    senha = str(input('Crie uma senha de 6 digitos: '))
                    if(len(senha)< 6):
                        print('A senha precisa conter 6 caracteres!')
                    elif(len(senha)> 6):
                        print('A senha precisa conter 6 caracteres!')
                    else:
                        break
            except(ValueError, TypeError):
                print('Tipo invalido!')
            else:
                break
        conta = gerador.gerarConta()
        agencia = gerador.gerarAgencia()
        saldo = float(0.0)
        
        bd.inserirCliente(cpf, nome, agencia, conta, saldo, senha)
        while True:
            resposta = str(input('Gostaria de adicionar mais um cliente?: ')).lower()
            if(resposta == 's' or resposta == 'sim'):
                break
            elif(resposta == 'n' or resposta == 'nao' or resposta == 'não'):
                condition = False
                break
            else:
                print('Opção inválida! Porfavor, insira uma opção válida! Opções válidas: [sim/não]')

def verClientes():
    for dado in bd.exibirCliente():        
        print('CPF: {}\nNome: {}\nAgencia: {}\nConta: {}\nSaldo: {}\n'.format(dado[0],dado[1],dado[2],dado[3],dado[4]))

def depositar(cpf, nome):
    condition = True
    while condition:
        while True:
            quem = str(input('Deseja depositar em sua conta ou em outra conta?: ')).lower()
            if(quem == '1' or quem == 'minha' or quem == 'minha conta'):
                icpf = cpf
                break
            elif(quem == '2' or quem == 'outra' or quem == 'outra conta'):
                icpf = str(input('Insira o cpf da conta que deseja fazer o depósito: '))
                break
            else:
                print('Opção inválida!Porfavor digite uma opção válida!')
        while True:
            try:
                deposito = float(input('Insira o valor do depósito: '))
            except(ValueError, TypeError):
                print('Valor inválido, porfavor, insira um valor válido!')
            else:
                break
        for dado in bd.exibirCliente():
            cpfcomparar = str(dado[0])
            if(icpf == cpfcomparar):
                saldo = float(dado[4])
                saldo = saldo + deposito
                from datetime import datetime
                hora = datetime.now().strftime('%d/%m/%Y %H:%M')
                regdep = './caixaeletronico/registros/deposito.txt'
                registro = open(regdep, 'a', encoding='UTF - 8')
                registro.writelines('Data/Hora: {}\nNome: {}\nAgencia: {}\nConta: {}\nSaldo anterior: {}\nDeposito: {}\nNovo saldo: {}\nDepositado por: {}\n\n'.format(hora,dado[1],dado[2],dado[3],dado[4],deposito,saldo,nome))
                registro.close()
                bd.atualizarClienteSaldo(saldo, icpf)
                print('\nData/Hora: {}\nNome: {}\nAgencia: {}\nConta: {}\nSaldo anterior: {}\nDeposito: {}\nNovo saldo: {}\nDepositado por: {}\n\n'.format(hora,dado[1],dado[2],dado[3],dado[4],deposito,saldo,nome))
                break
        while True:
            resposta = str(input('Gostaria de realizar mais um deposito?: ')).lower()
            if(resposta == 's' or resposta == 'sim'):
                break
            elif(resposta == 'n' or resposta == 'nao' or resposta == 'não'):
                condition = False
                break
            else:
                print('Opção inválida! Porfavor, insira uma opção válida! Opções válidas: [sim/não]')

def sacar(cpf):
    condition = True
    while condition:        
        for dado in bd.exibirCliente():
            cpfcomparar = str(dado[0])
            if(cpf == cpfcomparar):
                saldo = float(dado[4])
                while True:
                    try:
                        saque = float(input('Insira o valor do saque: '))
                    except(ValueError, TypeError):
                        print('Valor inválido, porfavor, insira um valor válido!')
                    else:
                        break
                if(saldo>saque):
                    saldo = saldo - saque
                else:
                    print('Você não tem saldo suficiente na conta para realizar este saque!')
                    saque = float(0.0)
                    saldo = saldo - saque
                from datetime import datetime
                hora = datetime.now().strftime('%d/%m/%Y %H:%M')
                regsaq = './caixaeletronico/registros/saque.txt'
                registro = open(regsaq, 'a', encoding='UTF - 8')
                registro.writelines('Data/Hora: {}\nNome: {}\nAgencia: {}\nConta: {}\nSaldo anterior: {}\nsaque: {}\nNovo saldo: {}\n\n'.format(hora,dado[1],dado[2],dado[3],dado[4],saque,saldo))
                registro.close()
                bd.atualizarClienteSaldo(saldo,cpf)
                print('\nData/Hora: {}\nNome: {}\nAgencia: {}\nConta: {}\nSaldo anterior: {}\nsaque: {}\nNovo saldo: {}\n\n'.format(hora,dado[1],dado[2],dado[3],dado[4],saque,saldo))
                break
        while True:
            resposta = str(input('Gostaria de realizar mais um saque?: ')).lower()
            if(resposta == 's' or resposta == 'sim'):
                break
            elif(resposta == 'n' or resposta == 'nao' or resposta == 'não'):
                condition = False
                break
            else:
                print('Opção inválida! Porfavor, insira uma opção válida! Opções válidas: [sim/não]')

def esqueceuSenha():
    existe = int(0)
    validar = True
    while validar:
        cpf = str(input('Insira seu cpf: '))
        for dado in bd.exibirCliente():
            cpfcomparar = str(dado[0])
            if(cpf == cpfcomparar):
                while True:
                    senha = str(input('Insira sua nova senha de 6 digitos: '))
                    if(len(senha)!=6):
                        print('A senha precisa conter 6 digitos!')
                    else:
                        break
                existe = 1
            else:
                existe = 0
        if(existe == 1):
            bd.atualizarClienteSenha(senha,cpf)
            print('Senha atualizada com sucesso!\n')
            validar = False
        elif(existe == 0):
            while True:
                criar = str(input('CPF não encontrado! Gostaria de criar uma conta?: ')).lower()
                if(criar == 's' or criar == 'sim'):
                    cod.adicionarCliente()
                    validar = False
                elif(criar == 'n' or criar == 'não' or criar == 'nao'):
                    print('Tente digitar o CPF novamente, e confira se todos os numeros e espaçamentos estão corretos!')
                    break
                else:
                    print('Opção inválida! Porfavor, insira uma opção válida! Opções válidas: [sim/não]')

def validar():
    caso = 0
    validar = True
    while validar:        
        if(caso == 1):
            print('CPF ou senha incorreto(s)!')
            while True:
                esqueceu = str(input('Esqueceu a senha?: ')).lower()
                if(esqueceu == 's' or esqueceu == 'sim'):
                    cod.esqueceuSenha()
                    break
                elif(esqueceu == 'n' or esqueceu == 'nao' or esqueceu == 'não'):
                    print('Tente novamente. Digite os dados com atenção!')
                    break
                else:
                    print('Opção inválida! Por favor, insira uma opção válida! Opções válidas: [sim/não]')
        caso = 0
        cpf = str(input('Insira seu cpf: '))
        senha = str(input('Insira sua senha: '))
        for dado in bd.exibirCliente():
            cpfcomparar = str(dado[0])
            senhacomparar = str(dado[5])
            if(cpf == cpfcomparar and senha == senhacomparar):
                print('\nConectado com sucesso!\n')
                validar = False
                nome = str(dado[1])                
                men.menu(cpf, nome)
                break
            else:
                caso = 1