import os

restaurantes = [{'nome': 'Picanha Mania', 'categoria': 'Almoço', 'ativo': True},    
                {'nome': 'Bobs', 'categoria': 'Lanche', 'ativo': False},
                {'nome': 'Cafe Delicia', 'categoria': 'Cafe', 'ativo': True},
                ]

def main():
    # Função que controla o programa / Menu
    os.system('cls')
    exibirMenu()
    escolherOpcao()

def exibirMenu():
    # Função que printa na tela as opções do programa
    print('Sabor express\n')
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alterar Status do Restaurante')
    print('4. Sair\n')

def voltarMenuPrincipal():
    # Função de apoio usada no final das outras funções para padronização 
    input('Digite qualquer tecla para voltar. ')
    main()

def subTitulo(mensagem):
    # Função que controla o sub-titulo de cada operação do programa. É chamda no inicio de cada função.
    # Recebe 'mensagem' (str) -> O nome da operação atual
    # Imprime a operação atual
    os.system('cls')
    print(f'{mensagem}\n')

def opcaoInvalida():
    print('Opção invalida!')
    voltarMenuPrincipal()

def cadastrarRestaurante():
    # Cadastro de restaurantes no banco de dados
    # Input: Nome do Restaurante (str) || Categoria do Restaurante (str)
    # Por padrão, todos os novos restaurantes cadastrados iniciam com o status 'false' == Desativado.
    # Output: Nome do Restaurante cadastrado 
    subTitulo('Cadastrando Restaurante...')
    nomeRestaurante = input('Digite o nome do restaurante: ')
    categoriaRestaurante = input(f'Digite a categoria do restaurante {nomeRestaurante}: ')
    dadosRestaurante = {'nome': nomeRestaurante, 'categoria': categoriaRestaurante, 'ativo': False}
    restaurantes.append(dadosRestaurante)
    print(f'Parabéns!! \nO restaurante {nomeRestaurante} foi cadastrado com sucesso!! \n')
    voltarMenuPrincipal()

def listarRestaurante():
    # Listagem dos Restaurantes cadastrados na base de dados
    # Printa na tela o Nome do Restaurante, Categoria, e o status (ativado ou desativado)
    subTitulo('Listando restaurantes cadastrados...')
    
    for i, restaurante in enumerate(restaurantes):
        nomeRestaurante = restaurante['nome']
        categoriaRestaurante = restaurante['categoria']
        statusRestaurante = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'id : {i} - Nome: {nomeRestaurante} || Categoria: {categoriaRestaurante} || Status: {statusRestaurante}\n')
    
    voltarMenuPrincipal()

def alterarStatus():
    # Alterando o status de um restaurante
    # Input: O usuario digita uma opção para realizar uma operação especifica (ativar ou desativar)
    # Output: Imprime os restaurantes de acordo com o status e a escolha do usuario
    # Input: Recebe o id (index) do restaurante que deseja alterar o status
    # Altera o status do restaurante
    # Output: Imprime que a alteração foi feita com sucesso
    subTitulo('Alternado o status do restaurante...')
    operacaoDesejada = int(input('Qual operação você deseja fazer?\n1 - Ativar restaurante\n2 - Desativar restaurante\n'))
    if operacaoDesejada == 1:
        for i, restaurante in enumerate(restaurantes):
            if not restaurante['ativo']:
                print(f'Id: {i} || Nome: {restaurante['nome']}')
        idRestaurante = int(input('Digite o id do restaurante que deseja ativar: '))
        restaurantes[idRestaurante]['ativo'] = True
        print(f'O restaurante {restaurantes[idRestaurante]['nome']} foi Ativado com sucesso!')

    else:
         for i, restaurante in enumerate(restaurantes):
            if restaurante['ativo']:
                print(f'Id: {i} || Nome: {restaurante['nome']}')
        
         idRestaurante = int(input('Digite o id do restaurante que deseja Desativar: '))
         restaurantes[idRestaurante]['ativo'] = False
         print(f'O restaurante {restaurantes[idRestaurante]['nome']} foi desativado com sucesso!')

    voltarMenuPrincipal()

def escolherOpcao():
    # Controlo as opções escolhidas e chamo as funções desejadas pelo usuario
    # Input: Opção que o usuario escolher (exibirMenu())
    # Output: Chamada de função
    # OBS: Se o usuario não digitar uma opcão valida, ele chama a função 'opcaoInvalida()' que chama a func 'exibirMenu()' novamente
    try:
        opcaoEscolhida = int(input('Digite uma opção: '))
        match opcaoEscolhida:
            case 1:
                cadastrarRestaurante()
            case 2:
                listarRestaurante()
            case 3:
                alterarStatus()
            case 4:
                print('Finalizando o programa...')
            case _:
                opcaoInvalida()
    except:
        opcaoInvalida()



if __name__ == '__main__':
    main()