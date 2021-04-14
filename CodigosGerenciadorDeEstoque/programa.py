import gerenciar.bd as bd

def adicionarItem():
    condition = True
    while condition:
        item = str(input('\033[1;36;40mInsira o nome do item que deseja adicionar: '))
        quantidade = int(input('\033[1;36;40mInsira a quantidade disponivel desse item: '))
        bd.inserirItens(item, quantidade)
        while True:
            resposta = str(input('\033[1;32;40mGostaria de adicionar mais um item?: ')).lower()
            if(resposta == 's' or resposta == 'sim'):
                condition = True
                break
            elif(resposta == 'n' or resposta == 'nao' or resposta == 'não'):
                condition = False
                break
            else:
                print('\033[1;31;40mEscreva se sim ou não!')
                print('\033[0;37;40m')

def alterarItem():
    id_item = int(input('\033[1;36;40mDigite o id do item que deseja alterar: '))
    item = str(input('\033[1;36;40mInsira o novo nome do item: '))
    bd.alterarItem(id_item, item)

def alterarQtd():
    id_item = int(input('\033[1;36;40mDigite o id do item que deseja alterar a quantidade: '))
    quantidade = int(input('\033[1;36;40mDigite a nova quantidade do item: '))
    bd.alterarQuantidade(quantidade, id_item)

def verItens():
    item = '[ITENS]'
    quantidade = '[QUANTIDADE]'
    print('{:^35} {}'.format(item, quantidade))
    for dados in bd.lerItens():      
        print('[Id: {}] {:^20} {:>14}'.format(dados[0], dados[1],dados[2]))

def subtrairItem():
    condition = True
    while condition:
        idcomparar = int(input('\033[1;36;40mDigite o Id do item que foi usado: '))
        for dado in bd.lerItens():
            if(idcomparar == dado[0]):
                subtrai = int(input('\033[1;36;40mQuantos itens foram utilizados?: '))
                quantidade = int(dado[2])
                if(quantidade >= subtrai):
                    quantidade = quantidade - subtrai
                    id_item = idcomparar
                    bd.alterarQuantidade(quantidade, id_item)
                else:
                    print('\033[1;31;40mNão há itens suficientes!')
                    print('\033[0;37;40m')
        while True:
            resposta = str(input('\033[1;32;40mGostaria de subtrair de mais um item?: ')).lower()
            if(resposta == 's' or resposta == 'sim'):
                condition = True
                break
            elif(resposta == 'n' or resposta == 'nao' or resposta == 'não'):
                condition = False
                break
            else:
                print('\033[1;31;40mEscreva se sim ou não!')
                print('\033[0;37;40m')
        

def somaItem():
    condition = True
    while condition:
        idcomparar = int(input('\033[1;36;40mDigite o Id do item que foi reabastecido: '))
        for dado in bd.lerItens():
            if(idcomparar == dado[0]):
                somar = int(input('\033[1;36;40mQuantos itens foram reabastecidos?: '))
                quantidade = int(dado[2])
                quantidade = quantidade + somar
                id_item = idcomparar
                bd.alterarQuantidade(quantidade, id_item)
        while True:
            resposta = str(input('\033[1;32;40mGostaria de adicionar a mais um item?: ')).lower()
            if(resposta == 's' or resposta == 'sim'):
                condition = True
                break
            elif(resposta == 'n' or resposta == 'nao' or resposta == 'não'):
                condition = False
                break
            else:
                print('\033[1;31;40mEscreva se sim ou não!')
                print('\033[0;37;40m')

def excluir():
    condition = True
    verItens()
    while condition:
        try:
            idenviar = int(input('\033[1;36;40mDigite o id do item que deseja deletar: '))            
        except ValueError:
            print('\033[1;31;40mDigite um inteiro!')
            condition = True
        else:            
            bd.excluir_item(idenviar)
            condition = False
