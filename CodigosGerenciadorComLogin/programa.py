import jogos.bd as bd
import jogos.menu as men

def addJogo():
    condition = True
    while condition:
        while True:
            try:
                while True:
                    nome = str(input('Insira o nome do jogo: ')).strip()
                    if not nome:
                        print('ERRO! O nome do jogo não pode estar vazio!')
                    else:                        
                        break            
            except (ValueError, TypeError):
                print('Valor inválido! Por favor, digite um valor válido! Valor valido: [String]')
            else:
                break
        
        while True:
            try:
                tempojogado = float(input('Insira quantas horas foram jogadas no jogo: '))
            except (ValueError, TypeError):
                print('Valor inválido! Por favor, digite um valor válido! Valor valido: [float]')
            else:
                break
        
        while True:
            try:
                conquistas = int(input('Insira quantas conquistas você adquiriu no jogo: '))
            except (ValueError, TypeError):
                print('Valor inválido! Por favor, digite um valor válido! Valor valido: [int]')
            else:
                break
        
        finalizado = int(0)
        while True:
            acabou = str(input('Ja terminou o jogo?: ')).lower()
            if(acabou == 's' or acabou == 'sim'):
                finalizado = int(1)
                break
            elif(acabou == 'n' or acabou == 'nao' or acabou == 'não'):
                finalizado = int(0)
                break
            else:
                print('Opção inválida! Por favor digite uma opção válida! Opções válidas: [sim/não]')
        bd.inserirJogo(nome,tempojogado,conquistas,finalizado)
        while True:
            resposta = str(input('Gostaria de inserir mais um jogo?: ')).lower()
            if(resposta == 's' or resposta == 'sim'):
                condition = True
                break
            elif(resposta == 'n' or resposta == 'nao' or resposta == 'não'):
                condition = False
                break
            else:
                print('Opção inválida! Por favor digite uma opção válida! Opções válidas: [sim/não]')

def verJogo():
    for dado in bd.exibirJogo():
        final = int(dado[4])
        if(final == 1):
            finalizado = 'Sim'
        elif(final == 0):
            finalizado = 'Não'
        print('ID: {}\nNome: {}\nTempo Jogado: {}\nConquistas: {}\nFinalizado?: {}\n'.format(dado[0],dado[1],dado[2],dado[3],finalizado))

def trocarNomeJogo():
    verJogo()
    condition = True
    while condition:
        while True:
            try:
                id_jogo = int(input('Insira o ID do jogo que deseja alterar o nome: '))
            except (ValueError, TypeError):
                print('Valor inválido! Por favor, digite um valor válido! Valor valido: [int]')
            else:
                break
        
        while True:            
            nome = str(input('Digite o novo nome: ')).strip()
            if not nome:
                print('ERRO! O nome do jogo não pode estar vazio!')
            else:
                break
        bd.atualizarNomeJogo(nome, id_jogo)
        while True:
            resposta = str(
                input('Gostaria de alterar o nome de mais um jogo?: ')).lower()
            if(resposta == 's' or resposta == 'sim'):
                condition = True
                break
            elif(resposta == 'n' or resposta == 'nao' or resposta == 'não'):
                condition = False
                break
            else:
                print('Opção inválida! Por favor digite uma opção válida! Opções válidas: [sim/não]')

def trocarTempojogadoJogo():
    verJogo()
    condition = True
    while condition:
        while True:
            try:
                id_jogo = int(input('Insira o ID do jogo que deseja alterar o tempo jogado: '))
            except(ValueError, TypeError):
                print('Valor inválido! Por favor, digite um valor válido! Valor valido: [int]')
            else:
                break
        
        while True:
            try:
                tempojogado = float(input('Digite o novo Tempo Jogado: '))
            except(ValueError, TypeError):
                print('Valor inválido! Por favor, digite um valor válido! Valor valido: [float]')            
            else:
                break
        bd.atualizarTempojogadoJogo(tempojogado, id_jogo)
        while True:
            resposta = str(input('Gostaria de alterar o tempo jogado de mais um jogo?: ')).lower()
            if(resposta == 's' or resposta == 'sim'):
                condition = True
                break
            elif(resposta == 'n' or resposta == 'nao' or resposta == 'não'):
                condition = False
                break
            else:
                print('Opção inválida! Por favor digite uma opção válida! Opções válidas: [sim/não]')

def trocarConquistasJogo():
    verJogo()
    condition = True
    while condition:
        while True:
            try:
                id_jogo = int(input('Insira o ID do jogo que deseja alterar as conquistas: '))
            except(ValueError, TypeError):
                print('Valor inválido! Por favor, digite um valor válido! Valor valido: [int]')
            else:
                break
        while True:
            try:
                conquistas = int(input('Digite o novo Tempo Jogado: '))
            except(ValueError, TypeError):
                print('Valor inválido! Por favor, digite um valor válido! Valor valido: [int]')
            else:
                break
        bd.atualizarConquistasJogo(conquistas, id_jogo)
        while True:
            resposta = str(input('Gostaria de alterar as conquistas de mais um jogo?: ')).lower()
            if(resposta == 's' or resposta == 'sim'):
                condition = True
                break
            elif(resposta == 'n' or resposta == 'nao' or resposta == 'não'):
                condition = False
                break
            else:
                print('Opção inválida! Por favor digite uma opção válida! Opções válidas: [sim/não]')

def trocarFinalizadoJogo():
    verJogo()
    condition = True
    while condition:
        while True:
            try:
                id_jogo = int(input('Insira o ID do jogo que deseja alterar a marcação de finalizado: '))
            except(ValueError, TypeError):
                print('Valor inválido! Por favor, digite um valor válido! Valor valido: [int]')
            else:
                break
        
        while True:
            finalizado = int(0)
            acabou = str(input('Terminou o jogo?: ')).lower()
            if(acabou == 's' or acabou == 'sim'):
                finalizado = 1
                break
            elif(acabou == 'n' or acabou == 'nao' or acabou == 'não'):
                finalizado = 0
                break
            else:
                print('Opção inválida! Por favor digite uma opção válida! Opções válidas: [sim/não]')
        bd.atualizarFinalizadoJogo(finalizado, id_jogo)
        while True:
            resposta = str(input('Gostaria de alterar o status de finalizado de mais um jogo?: ')).lower()
            if(resposta == 's' or resposta == 'sim'):
                condition = True
                break
            elif(resposta == 'n' or resposta == 'nao' or resposta == 'não'):
                condition = False
                break
            else:
                print('Opção inválida! Por favor digite uma opção válida! Opções válidas: [sim/não]')

def excluirJogo():
    verJogo()
    condition = True
    while condition:
        while True:
            try:
                id_jogo = int(input('Insira o ID do jogo que deseja excluir: '))
            except(ValueError, TypeError):
                print('Valor inválido! Por favor, digite um valor válido! Valor valido: [int]')
            else:
                break
        bd.deletarJogo(id_jogo)
        while True:
            resposta = str(input('Gostaria de excluir mais um jogo?: ')).lower()
            if(resposta == 's' or resposta == 'sim'):
                condition = True
                break
            elif(resposta == 'n' or resposta == 'nao' or resposta == 'não'):
                condition = False
                break
            else:
                print('Opção inválida! Por favor digite uma opção válida! Opções válidas: [sim/não]')

def cadastrarUsuario():    
    condition = True
    while condition:
        existe = int(0)
        validar = True
        while validar:
            while True:
                usuario = str(input('Digite seu nome de usuario: ')).strip()
                if not usuario:
                    print('ERRO! O nome de usuario não pode estar vazio!')
                else:
                    break
            for dado in bd.exibirJogador():                
                usuariocomparar = str(dado[1])
                if(usuariocomparar == usuario):
                    print('Este nome de usuario já está sendo utilizado! Por favor, digite um novo nome de usuario!')
                    existe = 1
                    validar = True
                    break
                else:
                    existe = 0
                    validar = False
            if(existe == 0):
                validar = False
            elif(existe == 1):
                validar = True
        redigitar = True
        while redigitar:
            while True:
                senha = str(input('Digite uma senha de 8 a 12 caracteres: '))
                if not senha:
                    print('ERRO! O nome do jogo não pode estar vazio!')
                elif(len(senha) > 12):
                    print('A senha pode ter no maximo 12 caracteres!')
                elif(len(senha) < 8):
                    print('A senha tem que ter no mínimo 8 caracteres!')
                else:
                    break
            senhacomparar = senha
            t = 3
            for i in range(3):
                t = t-1
                reescrever = str(input('Digite novamente sua senha: '))
                if(senhacomparar == reescrever):
                    redigitar = False
                    bd.inserirJogador(usuario, senha)
                    break
                else:
                    if(t > 0):
                        print(f'A verificação da senha não corresponde a senha digitada anteriormente. Mais {t} tentativas!')
                        redigitar = True
                    elif(t == 0):
                        print('Você tentou validar sua senha muitas vezes! Digite uma nova.\n')
                        resgistrar = True
        while True:
            resposta = str(input('Gostaria de adicionar mais um usuario?: ')).lower()
            if(resposta == 's' or resposta == 'sim'):
                condition = True
                break
            elif(resposta == 'n' or resposta == 'nao' or resposta == 'não'):
                condition = False
                break
            else:
                print('Opção inválida! Por favor digite uma opção válida! Opções válidas: [sim/não]')

def validarUsuario():
    condition = True
    while condition:
        incorreto = int(0)
        validar = True
        while validar:
            if(incorreto == 1):
                print('Usuario ou senha incorreto(s)! Por favor, digite novamente!')
            elif(incorreto == 0):
                print('Entre com seu usuario e com sua senha!\n')
            while True:
                usuario = str(input('Digite seu nome de usuario: '))
                if not usuario:
                    print('ERRO! O nome de usuario não pode estar vazio!')
                else:
                    break
            while True:
                senha = str(input('Digite sua senha: '))
                if not senha:
                    print('ERRO! O campo de senha não pode estar vazio!')
                else:
                    break
            for dado in bd.exibirJogador():
                usuariocomparar = str(dado[1])
                senhacomparar = str(dado[2])
                if(usuariocomparar == usuario and senhacomparar == senha):
                    validar = False
                    print('Você se logou!')
                    id_usuario = int(dado[0])
                    men.menu(usuario, id_usuario, senha)
                    break
                else:
                    incorreto = int(1)
                    validar = True        
        condition = False

def excluirUsuario(id_jogador):
    bd.excluirJogador(id_jogador)
