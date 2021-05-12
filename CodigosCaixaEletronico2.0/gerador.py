import random

def gerarConta():
    numero = 0
    conta = ''
    contaArray = []
    for i in range (5):
        contaArray.append(random.randint(0,9))    
    for i in contaArray:        
        digito = str(contaArray[numero])
        conta = conta + digito
        numero = numero + 1
    digfinal = str(random.randint(0,9))
    conta = conta + "-" + digfinal
    return conta

def gerarAgencia():
    numero = 0
    agencia = ''
    agenciaArray = []
    for i in range(4):
        agenciaArray.append(random.randint(0,9))
    for i in agenciaArray:
        digito = str(agenciaArray[numero])
        agencia = agencia + digito
        numero = numero + 1
    return agencia
