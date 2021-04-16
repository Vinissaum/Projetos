import compras.bd as bd
import compras.programa as prog

def opcoes():
    print('1 - Adicionar cliente\n2 - Adicionar produto\n3 - Editar\n4 - Excluir\n5 - Comprar\n6 - Ver\n7 - Sair do programa\n')

def titulo():
    title = 'MENU PRINCIPAL'
    print(title.center(50))

def linha():
    traco = '*'
    print(traco*50)

def menu():
    linha()
    titulo()
    opcoes()
    linha()
    escolha()

def escolha():    
    escolhe = int(input('Escolha uma opção: '))
    if(escolhe == 1):
        prog.addCliente()
        menu()
    elif(escolhe == 2):
        prog.addProduto()
        menu()
    elif(escolhe == 3):
        print('1 - Clientes\n2 - Produtos\n')
        while True:
            editar = str(input('Qual deseja editar?: ')).lower()
            if(editar == '1' or editar == 'clientes' or editar == 'cliente'):
                print('1 - Nome\n2 - E-mail\n')
                condition = True
                while condition:
                    editarcliente = str(input('O que gostaria de editar em Clientes?: ')).lower()
                    if(editarcliente == '1' or editarcliente == 'nome'):
                        prog.editarNomeCliente()
                        condition = False
                    elif(editarcliente == '2' or editarcliente == 'email' or editarcliente == 'e-mail' or editarcliente == 'e mail'):
                        prog.editarEmailCliente()
                        condition = False
                    else:
                        print('Opção inválida! Por favor, digite uma opção válida!')
                        condition = True
                break
            elif(editar == '2' or editar == 'produtos' or editar == 'produto'):
                print('1 - Nome\n2 - Quantidade\n3 - Preço\n')
                condition = True
                while condition:
                    editarproduto = str(input('O que gostaria de editar em Produtos?: ')).lower()
                    if(editarproduto == '1' or editarproduto == 'nome'):
                        prog.editarNomeProduto()
                        condition = False
                    elif(editarproduto == '2' or editarproduto == 'quantidade'):
                        prog.editarQuantidadeProduto()
                        condition = False
                    elif(editarproduto == '3' or editarproduto == 'preco' or editarproduto == 'preço'):
                        prog.editarPrecoProduto()
                        condition = False
                    else:
                        print('Opção inválida! Por favor, digite uma opção válida!')
                        condition = True
                break
            else:
                print('Opção inválida! Por favor, digite uma opção válida!')
        menu()
    elif(escolhe == 4):
        print('1 - Clientes\n2 - Produtos\n')
        while True:
            excluir = str(input('Qual deseja excluir?: ')).lower()
            if(excluir == '1' or excluir == 'clientes' or excluir == 'cliente'):
                prog.deletarCliente()
                break
            elif(excluir == '2' or excluir == 'produtos' or excluir == 'produto'):
                prog.deletarProduto()
                break
            else:
                print('Opção inválida! Por favor, digite uma opção válida!')
        menu()
    elif(escolhe == 5):
        menucompras = 'MENU DE COMPRAS'
        linha()
        print(menucompras.center(50))
        linha()
        prog.comprar()
        menu()
    elif(escolhe == 6):
        print('1 - Clientes\n2 - Produtos\n')
        while True:
            dados = str(input('Qual deseja ver os dados disponiveis?: ')).lower()
            if(dados == '1' or dados == 'clientes' or dados == 'cliente'):
                prog.exibirClientes()
                break
            elif(dados == '2' or dados == 'produtos' or dados == 'produto'):
                prog.exibirProdutos()
                break
            else:
                print('Opção inválida! Por favor, digite uma opção válida!')
        menu()
    elif(escolhe == 7):
        print('Saindo...')
    else:
        print('Opção inválida! Por favor, digite uma opção válida!')
        escolha()

bd.criarTabelaCliente()
bd.criarTabelaProdutos()
menu()
