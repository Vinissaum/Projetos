import compras.bd as bd

def addCliente():
    condition = True
    while condition:
        cpf = str(input('Digite o cpf do cliente: '))
        nome = str(input('Digite o nome do cliente: '))
        email = str(input('Digite o e-mail do cliente: '))
        bd.inserirCliente(cpf, nome, email)
        while True:
            resposta = str(input('Gostaria de adicionar mais um cliente?: ')).lower()
            if(resposta == 's' or resposta == 'sim'):
                condition = True
                break
            elif(resposta == 'n' or resposta == 'nao' or resposta == 'não'):
                condition = False
                break
            else:
                print('Digite se sim ou se não!')

def addProduto():
    condition = True
    while condition:
        nome = str(input('Digite o nome do produto: '))
        quantidade = int(input('Digite a quantidade disponivel do produto: '))
        preco = float(input('Digite o preço do produto: '))
        bd.inserirProduto(nome, quantidade, preco)
        while True:
            resposta = str(input('Gostaria de adicionar mais um produto?: ')).lower()
            if(resposta == 's' or resposta == 'sim'):
                condition = True
                break
            elif(resposta == 'n' or resposta == 'nao' or resposta == 'não'):
                condition = False
                break
            else:
                print('Digite se sim ou se não!')

def exibirClientes():
    c = 'CPF'
    n = 'NOME'
    e = 'E-MAIL'
    print('{:<10}{:^10}{:>13}'.format(c,n,e))
    for dado in bd.verClientes():
        print('{:<10}{:^10}{:>13}'.format(dado[0], dado[1], dado[2]))

def exibirProdutos():
    i = 'ID'
    n = 'NOME'
    q = 'QUANTIDADE'
    p = 'PREÇO'
    print('[{}]{:>10}{:>15}{:>10}'.format(i,n,q,p))
    for dado in bd.verProdutos():
        print('[{}]{:>10}{:>15}{:>10}'.format(dado[0], dado[1], dado[2], dado[3]))

def comprar():
    precototal = float(0)
    condition = True
    cpfcomparar = str(input('Entre com o CPF do cliente: '))
    for dado in bd.verClientes():
        cpf = str(dado[0])
        if(cpfcomparar == cpf):
            nome = str(dado[1])
            while condition:
                exibirProdutos()
                idcomparar = int(input('Entre com o ID do produto desejado: '))
                for item in bd.verProdutos():
                    idproduto = int(item[0])
                    if(idcomparar == idproduto):
                        qtd = int(input('Quantos gostaria de comprar?: '))
                        quantidade = int(item[2])
                        quantidade = quantidade - qtd
                        preco = float(item[3])
                        preco = preco*qtd
                        id_produto = idcomparar
                        bd.atualizarQuantidadeProduto(id_produto, quantidade)
                while True:
                    resposta = str(input('Gostaria de comprar mais um item?: ')).lower()
                    if(resposta == 's' or resposta == 'sim'):
                        precototal = precototal + preco
                        condition = True
                        break
                    elif(resposta == 'n' or resposta == 'nao' or resposta == 'não'):
                        precototal = precototal + preco
                        condition = False
                        break
                    else:
                        print('Digite se sim ou se não!')
    print(f'A cesta do cliente {nome} deu um total de {precototal} reais!')

def editarQuantidadeProduto():
    condition = True
    while condition:
        exibirProdutos()
        id_produto = int(input('Escreva o ID do produto que deseja alterar a quantidade manualmente: '))
        quantidade = int(input('Insira a nova quantidade do produto: '))
        bd.atualizarQuantidadeProduto(id_produto, quantidade)
        resposta = str(input('Gostaria de alterar a quantidade de mais um produto?: ')).lower()
        if(resposta == 's' or resposta == 'sim'):
            condition = True
        elif(resposta == 'n' or resposta == 'nao' or resposta == 'não'):
            condition = False
        else:
            print('Digite se sim ou se não!')

def deletarProduto():
    condition = True
    while condition:
        exibirProdutos()
        id_produto = int(input('Insira o ID do produto que gostaria de excluir: '))
        bd.excluirProduto(id_produto)
        resposta = str(input('Gostaria de excluir mais um produto?: ')).lower()
        if(resposta == 's' or resposta == 'sim'):
            condition = True
        elif(resposta == 'n' or resposta == 'nao' or resposta == 'não'):
            condition = False
        else:
            print('Digite se sim ou se não!')

def editarPrecoProduto():
    condition = True
    while condition:
        exibirProdutos()
        id_produto = int(input('Escreva o ID do produto que deseja alterar o preço manualmente: '))
        preco = float(input('Insira o novo preço do produto: '))
        bd.atualizarPrecoProduto(id_produto, preco)
        resposta = str(input('Gostaria de alterar o preço de mais um produto?: ')).lower()
        if(resposta == 's' or resposta == 'sim'):
            condition = True
        elif(resposta == 'n' or resposta == 'nao' or resposta == 'não'):
            condition = False
        else:
            print('Digite se sim ou se não!')

def editarNomeProduto():
    condition = True
    while condition:
        exibirProdutos()
        id_produto = int(input('Escreva o ID do produto que deseja alterar o nome manualmente: '))
        nome = str(input('Insira o novo nome do produto: '))
        bd.atualizarNomeProduto(id_produto, nome)
        resposta = str(input('Gostaria de alterar o nome de mais um produto?: ')).lower()
        if(resposta == 's' or resposta == 'sim'):
            condition = True
        elif(resposta == 'n' or resposta == 'nao' or resposta == 'não'):
            condition = False
        else:
            print('Digite se sim ou se não!')

def editarNomeCliente():
    condition = True
    while condition:
        exibirClientes()
        cpf = int(input('Escreva o cpf do cliente que deseja alterar o nome manualmente: '))
        nome = str(input('Insira o novo nome do cliente: '))
        bd.atualizarNomeCliente(cpf, nome)
        resposta = str(input('Gostaria de alterar o nome de mais um cliente?: ')).lower()
        if(resposta == 's' or resposta == 'sim'):
            condition = True
        elif(resposta == 'n' or resposta == 'nao' or resposta == 'não'):
            condition = False
        else:
            print('Digite se sim ou se não!')

def editarEmailCliente():
    condition = True
    while condition:
        exibirClientes()
        cpf = int(input('Escreva o cpf do cliente que deseja alterar o email manualmente: '))
        email = str(input('Insira o novo email do cliente: '))
        bd.atualizarEmailCliente(cpf, email)
        resposta = str(input('Gostaria de alterar o email de mais um cliente?: ')).lower()
        if(resposta == 's' or resposta == 'sim'):
            condition = True
        elif(resposta == 'n' or resposta == 'nao' or resposta == 'não'):
            condition = False
        else:
            print('Digite se sim ou se não!')

def deletarCliente():
    condition = True
    while condition:
        exibirClientes()
        cpf = str(input('Insira o cpf do cliente que gostaria de excluir: '))
        bd.excluirCliente(cpf)
        resposta = str(input('Gostaria de excluir mais um cliente?: ')).lower()
        if(resposta == 's' or resposta == 'sim'):
            condition = True
        elif(resposta == 'n' or resposta == 'nao' or resposta == 'não'):
            condition = False
        else:
            print('Digite se sim ou se não!')
