from processadores import *
from dados import *
from helpers import *


# --- Main | Menu interativo --------
def main():
    cadastro = carregar_dados()

    while True:
        print('\n=== Gestão Acadêmica ===')
        print('[1] - Registrar aluno')
        print('[2] - Buscar aluno')
        print('[3] - Listar todos')
        print('[4] - Sair...')
        print('=========================\n')

        opcao = input('Escolha uma opção: ').strip()

        if opcao == '1':
            nome = ler_nome('Nome: ')

            if nome.strip() in carregar_dados():
                print(f'\nAluno {nome.title()} já registrado nos Dados dos alunos, informe um nome diferente.')
                continue

            qtd_notas = ler_quantidade_nota('Quantas notas quer informar: ')
            notas = ler_nota('Nota: ', qtd_notas)

            try:
                registrar_aluno(cadastro, nome, notas)

            except ValueError as error:
                print(error)
                continue

            print(f'Aluno {nome} registrado')

        elif opcao == '2':
            aluno = ler_nome('Informe o nome do Aluno: ')
            try:
                resultado =buscar_aluno(cadastro, aluno)

            except ValueError as error:
                print(error)
                continue

            print(f'\nAluno: {resultado["nome"]}')
            print(f'Notas: {resultado["notas"]}')

        elif opcao == '3':
            try:
               listagem = listar_alunos(cadastro)

            except ValueError as error:
                print(error)
                continue

            for aluno in listagem:
                print(f'\nAluno: {aluno["nome"]}')
                print(f'Media: {aluno["media"]}')
                print(f'Situacao: {aluno["situacao"]}\n')

        elif opcao == '4':
            salvar_dados(cadastro)
            print('\nFinalizado...')

            break

        else:
            print('Opcao invalida. Tente novamente.')

if __name__ == '__main__':
    main()
