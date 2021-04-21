import jogos.bd as bd
import jogos.programa as prog


def traco():
    linha = '*'
    print(linha*50)


def titulo():
    title = 'MENU PRINCIPAL'
    print(title.center(50))


def opcoes():
    print('1 - Cadastrar Jogo\n2 - Ver Jogos\n3 - Alterar Jogo\n4 - Deletar Jogo\n5 - Opções de Usuario\n6 - Sair do programa')

def menu(usuario, id_usuario, senha):
    traco()
    titulo()
    traco()
    print(f'Usuario logado no momento: {usuario}')
    traco()
    opcoes()
    traco()
    id_jogador = int(id_usuario)
    senhacomparar = senha
    usuario = usuario
    id_usuario = id_usuario
    senha = senha
    escolha(id_jogador,senhacomparar,usuario,id_usuario,senha)


def escolha(id_jogador, senhacomparar, usuario, id_usuario, senha):
    escolhe = str(input('O que gostaria de fazer?: ')).lower().strip()
    if(escolhe == '1' or escolhe == 'cadastrar' or escolhe == 'cadastrarjogo' or escolhe =='cadastrarjogos'):
        prog.addJogo()
        menu(usuario,id_usuario,senha)
    elif(escolhe == '2' or escolhe == 'ver' or escolhe == 'verjogo' or escolhe == 'verjogos'):
        prog.verJogo()
        menu(usuario, id_usuario, senha)
    elif(escolhe == '3' or escolhe == 'alterar' or escolhe == 'alterarjogo' or escolhe == 'alterarjogos'):
        traco()
        print('1 - Nome\n2 - Horas Jogadas\n3 - Conquistas\n4 - Finalizado')
        traco()
        while True:
            alterar = str(input('O que gostaria de alterar em Jogo?: ')).lower().strip()
            if(alterar == '1' or alterar == 'nome'):
                prog.trocarNomeJogo()
                menu(usuario, id_usuario, senha)
                break
            elif(alterar == '2' or alterar == 'horas' or alterar == 'horasjogadas'):
                prog.trocarTempojogadoJogo()
                menu(usuario, id_usuario, senha)
                break
            elif(alterar == '3' or alterar == 'conquistas' or alterar == 'conquista'):
                prog.trocarConquistasJogo()
                menu(usuario, id_usuario, senha)
                break
            elif(alterar == '4' or alterar == 'finalizado'):
                prog.trocarFinalizadoJogo()
                menu(usuario, id_usuario, senha)
                break
            else:
                print('Opção inválida! Por favor, escolha uma opção válida! Opções Válidas [//1 - Nome//2 - Horas Jogadas//3 - Conquistas//4 - Finalizado//]')
    elif(escolhe == '4' or escolhe == 'excluir' or escolhe == 'excluirjogo'):
        prog.excluirJogo()
        menu(usuario, id_usuario, senha)
    elif(escolhe == '5' or escolhe == 'opcoes' or escolhe == 'opcoesdeusuario' or escolhe == 'opcoesusuario' or escolhe == 'opções' or escolhe == 'opçõesdeusuario' or escolhe == 'opçõesusuario' or escolhe == 'opcoesusuário' or escolhe == 'opcoesdeusuário' or escolhe == 'opçõesdeusuário' or escolhe == 'opçõesusuário'):
        traco()
        print('1 - Alterar nome de usuario\n2 - Alterar senha\n3 - EXCLUIR USUARIO')
        traco()
        opcao = str(input('O que gostaria de fazer?: ')).lower().strip()
        if(opcao == '1' or opcao == 'alterarnome'):
            validar = True
            while validar:
                while True:
                    novousuario = str(input('Digite seu nome de usuario: ')).strip()
                    if not novousuario:
                        print('ERRO! O nome de usuario não pode estar vazio!')
                    else:
                        break
                for dado in bd.exibirJogador():                
                    usercompar = str(dado[1])
                    if(usercompar == novousuario):
                        print('Este nome de usuario já está sendo utilizado! Por favor, digite um novo nome de usuario!')                    
                        validar = True
                        break
                    else:                    
                        validar = False
            t = 3
            for i in range(3):
                t = t-1
                senha = str(input('Digite sua senha para confirmar a operação: '))
                if(senha == senhacomparar):
                    bd.atualizarUsuarioJogador(novousuario, id_jogador)
                    break
                else:                    
                    if(t > 0):
                        print(f'Senha incorreta! Mais {t} Tentativas!')
                    elif(t == 0):
                        print('Numero de tentativas excedido! Cancelando operação...')
                        exit()
        elif(opcao == '2' or opcao == 'alterarsenha'):
            while True:
                novasenha = str(input('Digite sua nova senha de 8 a 12 caracteres: ')).strip()
                if(len(novasenha > 12)):
                    print('Sua senha pode ter no máximo 12 caracteres!')
                elif(len(novasenha) < 8):
                    print('Sua senha deve ter no mínimo 8 caracteres!')
                elif not novasenha:
                    print('Sua senha não pode estar em branco!')
                else:
                    break
            t = 3
            for i in range(3):
                t = t-1
                senha = str(input('Digite sua senha para confirmar a operação: '))
                if(senha == senhacomparar):
                    bd.atualizarSenhaJogador(novasenha, id_jogador)
                    break
                else:
                    if(t > 0):
                        print(f'Senha incorreta! Mais {t} Tentativas!')
                    elif(t == 0):
                        print('Numero de tentativas excedido! Cancelando operação...')
                        exit()
        elif(opcao == '3' or opcao == 'excluir' or opcao == 'excluirusuario'):
            print('ESTA OPÇÃO DELETARÁ SEU USUARIO PARA SEMPRA! ISSO NÃO PODERÁ SER DESFEITO!')
            confirma = str(input('Digite "CONFIRMA" para prosseguir: ')).strip()
            if(confirma == 'CONFIRMA'):
                t = 3
                for i in range(3):
                    t = t-1
                    senha = str(input('Digite sua senha para confirmar a operação: '))
                    if(senha == senhacomparar):
                        bd.excluirJogador(id_jogador)
                        break
                    else:
                        if(t > 0):
                            print(f'Senha incorreta! Mais {t} Tentativas!')
                        elif(t == 0):
                            print('Numero de tentativas excedido! Cancelando operação...')
                            exit()
            else:
                print('Cancelando operação...')
                exit()
    elif(escolhe == '6' or escolhe == 'sair' or escolhe == 'sairdoprograma' or escolhe == 'sairprograma'):
        print('Saindo...')
        exit()
    else:
        print('Opção inválida! Por favor, digite uma opção válida! Opções válidas: [//1 - Cadastrar Jogo//2 - Ver Jogos//3 - Alterar Jogo//4 - Deletar Jogo//5 - Opções de Usuario//6 - Sair do programa//]')
        exit()
