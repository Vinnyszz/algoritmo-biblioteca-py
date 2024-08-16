
# Declaração da lista de livros e id_global para índice de livros
lista_livro = []
id_global = 0


# Função para cadastrar livros
def cadastrar_livro(id):
    print('-' * 60)
    print('-' * 10, 'MENU CADASTRA LIVRO', '-' * 18)
    print(f'ID do livro: {id} ')
    nome = str(input('Digite o nome do livro: '))
    autor = str(input('Digite o autor do livro: ')).lower()
    editora = str(input('Digite a editora do livro: '))
    livro = {'ID': id, 'Nome': nome, 'Autor': autor, 'Editora': editora}
    lista_livro.append(livro.copy())  # Copiamos o dicionário para dentro da lista
    print('-' * 60)
    print('\n')


# Função para consultar livros
def consultar_livro():
    while True:
        print('-' * 60)
        print('-' * 10, 'MENU CONSULTAR LIVRO', '-' * 18)
        opcao_consulta = int(input('Escolha a opção deseja:\n'
                          '1 - Consultar Todos os Livros\n'
                          '2 - Consultar Livro por id\n'
                          '3 - Consultar Livro(s) por autor\n'
                          '4 - Retornar ao menu\n'
                          '>>'))
        if opcao_consulta == 1:
            print('-' * 60)
            for livro in lista_livro:  # Vamos fazer a verificação para cada livro (dicionário) contido dentro da lista
                for item, valor in livro.items():  # Dentro de cada livro, vamos imprimir o par de dado e seu valor
                    print(f'{item} : {valor}')
                print('\n')
            continue

        elif opcao_consulta == 2:
            id_livro = int(input('Digite o id do livro: '))
            print('-' * 60)
            # Irá exibir o item e se respectivo valor do livro que possui o índice que o usuário escolheu
            # o -1 serve para compensar o fato do indice da lista comecar em 0
            for item, valor in lista_livro[id_livro - 1].items():
                print(f'{item} : {valor}')
            print('\n')
            continue

        elif opcao_consulta == 3:
            nome_autor = str(input('Digite o autor do(s) livro(s): ')).lower()

            # Aqui será iterado todos os livros da lista_livro. Se o valor da key for igual ao nome_autor será retornado
            # todas as informações cadastrada do livro em questão
            for livro in lista_livro:
                if livro['Autor'] == nome_autor:
                    for item, valor in livro.items():
                        print(f'{item} : {valor}')
                    print('\n')
            continue
        elif opcao_consulta == 4:
            break
        else:
            print('Opção inválida')
            continue

# Função para remover livros
def remover_livro():
    print('-' * 60)
    print('-' * 10, 'MENU REMOVER LIVRO', '-' * 18)
    while True:
        id_remover = int(input('Digite o ID do livro que deseja remover: '))
        if (id_remover <= 0) or (id_remover > len(lista_livro)):
            print('Id inválido\n')
            continue
        else:
            # Aqui temos que subtrair -1 pois a nossa lista começa a contagem de itens em 0. Porém, para o usuário a
            # contagem se inicia em 1. Então para compensar a entrada do usuário é subtraido 1 para selecionar o ID certo.
            del lista_livro[id_remover - 1]
            print('Livro removido com sucesso !')
            break


# Aqui é o nosso escopo principal (main)
print('Bem vindo a Livraria do Vinícius Prudente')
print('-'*60)
while True:
    print('-' * 15, 'MENU PRINCIPAL', '-' * 20)
    opcao = int(input('Escolha a opção desejada:\n'
                      '1 - Cadastrar livro\n'
                      '2 - Consultar Livro(s)\n'
                      '3 - Remover Livro\n'
                      '4 - Encerrar programa\n'
                      '>>'))
    if opcao == 1:
        id_global += 1
        cadastrar_livro(id_global)
        continue
    elif opcao == 2:
        consultar_livro()
        continue
    elif opcao == 3:
        remover_livro()
        continue
    elif opcao == 4:
        break
    else:
        print('Opção Inválida')
        continue
