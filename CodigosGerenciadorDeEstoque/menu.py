import gerenciar.bd as bd
import gerenciar.programa as prog

def traco():
    traco = '*'
    print(traco*50)

def titulo():
    titulo = 'MENU PRINCIPAL'
    print(titulo.center(50), '\n')

def opcoes():
    print('1 - Adicionar novo item\n2 - Reduzir do total\n3 - Aumentar do total\n4 - Editar manualmente o item\n5 - Excluir item\n6 - Ver todos os itens\n7 - Sair do programa\n')


def menu():
    
    traco()
    titulo()
    opcoes() 
    traco()
    escolher()

def escolher():    
    condition = True
    while condition:
        try:       
            escolha = int(input('Escolha uma opção: '))
        except ValueError:
            print('Por favor, digite um numero inteiro para a opção!')
            condition = True
        except KeyboardInterrupt:
            print('Por favor, digite alguma coisa!')
            condition = True
        else:
            condition = False
            funcoes(escolha)

def funcoes(escolha):
    if(escolha == 1):        
        prog.adicionarItem()
        menu()
    elif(escolha == 2):
        prog.verItens()
        prog.subtrairItem()
        menu()
    elif(escolha == 3):
        prog.verItens()
        prog.somaItem()
        menu()
    elif(escolha == 4):
        while True:
            editar = str(input('Gostaria de alterar o item ou a quantidade?[1 - item 2 - quantidade]: ')).lower()
            if(editar == 'item' or editar == '1'):
                prog.verItens()
                prog.alterarItem()
                break            
            elif(editar == 'quantidade' or editar == '2'):
                prog.verItens()
                prog.alterarQtd()
                break
            else:
                print('Escolha uma opção válida!')
        menu()
    elif(escolha == 5):        
        prog.excluir()
        menu()
    elif(escolha == 6):
        prog.verItens()
        menu()
    elif(escolha == 7):
        print('saindo...')
    else:
        print('Digite uma opção válida!')
        escolher()

bd.CriarTabelaItens()
menu()
