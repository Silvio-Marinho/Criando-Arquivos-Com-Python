'''
    Criando e lendo arquivos com python
'''


# Criando as função para criar, escrever e ler os arquivos

def criar_arquivo():
    while True:
        print('\nCriando arquivo!')
        arquivo = input('Digite o nome e extensão do arquivo: ')
        if len(arquivo) > 4:
            try:
                open(arquivo, 'w', encoding='utf-8')
                print(f'Arquivo "{arquivo}", criado com sucesso!')
                break
            except BaseException as erro:
                print(erro)
        else:
            print('\nO nome do arquivo com sua extensão deve conter no mínimo 5 caracteres')

def escrevendo_arquivo():
    try:
        print('\nEscrevendo no arquivo!')
        arquivo = input('Digite o nome e extensão do arquivo: ')
        while True:
            texto = input('Escreva o que será salvo no arquivo [sair=/]: ')
            if texto == '/':
                break
            with open(f'{arquivo}', 'a+', encoding='utf8') as arq:
                arq.write(f'{texto}\n')
    except BaseException as erro:
        print(erro)

def ler_arquivo():
    try:
        print('\nLendo o conteúdo do arquivo!')
        arquivo = input('Digite o nome e extensão do arquivo: ')
        with open(f'{arquivo}', 'r', encoding='utf8') as arq:
            print()
            for linha in arq:
                print(linha[0:-1])
    except BaseException as erro:
        print(erro)

