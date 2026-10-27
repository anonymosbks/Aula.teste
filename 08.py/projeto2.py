import os

restaurantes = [{'nome': 'Bom Gosto', 'categoria': 'Hamburgueria', 'ativo': True}, {'nome': 'benatti', 'categoria': 'Pizarria', 'ativo':False}, {'nome':'Cantina', 'categoria':'lanchonete', 'ativo':True}
            ]

def exibir_nome_app():
    print("""𝕾𝕬𝕭𝕺𝕽_𝕰𝕾𝕻𝕽𝕰𝕾𝕾|\n""")

def exibir_opcao():  
    print('1. Cadastrar restaurante\n')
    print('2. Listar restaurantes\n')
    print('3. Ativar restaurante\n')
    print('4. Sair\n\n')

def cadastar_novo_restaurante():
    exibir_subititulo('Cadastro de novos restaurantes')

    print(f'{'Nome do Restaurante'.ljust(23)} | {'Categoria'.ljust(21)}| Status')
    for restaurante in restaurantes:
        nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
        categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}\n')
        dados_restaurante = {'nome': nome_do_restaurante,'categoria':categoria, 'ativo':False}
        restaurantes.append(dados_restaurante)
        print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subititulo('listando restaurantes cadastrados')
    for restaurante in restaurantes:
        nome_do_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f' - {nome_do_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()

def finalizar_app():
    exibir_subititulo('Finalizando o app...')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def opcao_invalida():
    print('Opção inválida\n')
    voltar_ao_menu_principal()

def exibir_subititulo(texto):
    os.system('cls')
    print(texto)
    print()

def alternar_estado_restaurante():
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o status: \n')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            menssagem = f'o restaurante {nome_restaurante} foi ativado com sucesso' if restaurante ['ativo'] else f'o restaurante{nome_restaurante} foi desativado com sucesso'
            print(menssagem)

    if not restaurante_encontrado:
        print('o restaurante não foi encontrado')
    voltar_ao_menu_principal

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        #Opção escolhida e testada com bloco de condição if

        if opcao_escolhida == 1:
            cadastar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
            escolher_opcao()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_app()
    exibir_opcao()
    escolher_opcao()

if __name__ == '__main__':
    main()