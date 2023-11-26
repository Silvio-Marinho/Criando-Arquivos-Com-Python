from arquivo.criar_escrever_ler_arquivos import *
menu = ['Criar', 'Escrever', 'Ler', 'Exit']

while True:
    print('\nSelecione uma das opções!\n')
    contador = 1
    for op_menu in menu:
        print(f'[{contador}] - {op_menu}')
        contador += 1
    opcao = input('\nOpção: ')
    if opcao.isnumeric():
        opcao = int(opcao)
        if opcao == 1:
            criar_arquivo()
        elif opcao == 2:
            escrevendo_arquivo()
        elif opcao == 3:
            ler_arquivo()
        elif opcao == 4:
            break
    else:
        print('\nOpção inválida!')
