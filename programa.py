import gerenciar.bd as bd

def adicionarItem():
    item = str(input('Insira o nome do item que deseja adicionar: '))
    quantidade = int(input('Insira a quantidade disponivel desse item: '))
    bd.inserirItens(item, quantidade)

def alterarItem():
    id_item = int(input('Digite o id do item que deseja alterar: '))
    item = str(input('Insira o novo nome do item: '))
    bd.alterarItem(id_item, item)

def alterarQtd():
    id_item = int(input('Digite o id do item que deseja alterar a quantidade: '))
    quantidade = int(input('Digite a nova quantidade do item: '))
    bd.alterarQuantidade(quantidade, id_item)

def verItens():
    for dados in bd.lerItens():
        print('Id: {:<20} Item: {:^20} Quantidade: {:>20}'.format(dados[0], dados[1],dados[2]))

def subtrairItem():
    idcomparar = int(input('Digite o Id do item que foi usado: '))
    for dado in bd.lerItens():
        if(idcomparar == dado[0]):
            subtrai = int(input('Quantos itens foram utilizados?: '))
            quantidade = int(dado[2])
            quantidade = quantidade - subtrai
            id_item = idcomparar
            bd.alterarQuantidade(quantidade, id_item)

def somaItem():
    idcomparar = int(input('Digite o Id do item que foi reabastecido: '))
    for dado in bd.lerItens():
        if(idcomparar == dado[0]):
            somar = int(input('Quantos itens foram reabastecidos?: '))
            quantidade = int(dado[2])
            quantidade = quantidade + somar
            id_item = idcomparar
            bd.alterarQuantidade(quantidade, id_item)

def excluir():
    condition = True
    verItens()
    while condition:
        try:
            idenviar = int(input('Digite o id do item que deseja deletar: '))            
        except ValueError:
            print('Digite um inteiro!')
            condition = True
        else:            
            bd.excluir_item(idenviar)
            condition = False
