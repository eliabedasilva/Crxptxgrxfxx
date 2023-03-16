from archive_funcs import *

#windows-1252

characters_order = ['A', 'Á', 'À', 'Ã', 'Â', 'B', 'C', 'Ç', 'D', 'E', 'É', 'È', 'Ê', 'F', 'G', 'H', 'I', 'Í', 'Ì', 'J',
                   'K', 'L', 'M', 'N', 'O', 'Ó', 'Ò', 'Õ', 'Ô', 'P', 'Q', 'R', 'S', 'T', 'U', 'Ú', 'Ù', 'Û', 'V', 'W',
                   'X', 'Y', 'Z', 'a', 'á', 'à', 'ã', 'â', 'b', 'c', 'ç', 'd', 'e', 'é', 'è', 'ê', 'f', 'g', 'h', 'i',
                   'í', 'ì', 'j', 'k', 'l', 'm', 'n', 'o', 'ó', 'ò', 'õ', 'ô', 'p', 'q', 'r', 's', 't', 'u', 'ú', 'ù',
                   'û', 'v', 'w', 'x', 'y', 'z', '.', '-', ',', ':', '+', '\'', '!', '?', '0', '1', '2', '3', '4', '5',
                   '6', '7', '8', '9', '(', ')', '/', '_', '=', '\\', '[', ']', '*', '"', '<', '>', ';', ' ']
menu_list_1 = ['Tratar pasta', 'Tratar arquivo']
menu_list_2 = ['Encriptar', 'Descriptar', 'Visualizar']
while True:

    titulo('Bem vindo ao encriptador 3000!!!')
    opcao = menu(menu_list_1)

    if opcao == 1:
        pasta = input('Digite o caminho da pasta: ')
        key = input('Digite a chave: ')
        opcao_2 = menu(menu_list_2)
        archives = load_achives(pasta)
        if opcao_2 == 1:
            archives = generate_new_texts_encrypted(archives, key, characters_order)
            show_archives(archives)
            opcao_3 = input('Deseja salvar alterações [S/N]: ')
            if opcao_3.upper() == 'S':
                set_archives(archives, pasta)

        elif opcao_2 == 2:
            archives = generate_new_texts_unencrypted(archives, key, characters_order)
            show_archives(archives)
            opcao_3 = input('Deseja salvar alterações [S/N]: ')
            if opcao_3.upper() == 'S':
                set_archives(archives, pasta)

        elif opcao_2 == 3:
            archives = generate_new_texts_unencrypted(archives, key, characters_order)
            show_archives(archives)

        else:
            print('Opção inválida')

    elif opcao == 2:
        path = input('Digite o caminho do arquivo: ')
        archive = load_archive(path)
        opcao_2 = menu(menu_list_2)
        key = input('Digite a chave: ')

        if opcao_2 == 1:
            archive = generate_new_text_encrypted(archive, key, characters_order)
            show_archives([archive])
            opcao_3 = input('Deseja salvar alterações [S/N]: ')
            if opcao_3.upper() == 'S':
                set_archive(archive, path)

        elif opcao_2 == 2:
            archive = generate_new_text_unencrypted(archive, key, characters_order)
            show_archives([archive])
            opcao_3 = input('Deseja salvar alterações [S/N]: ')
            if opcao_3.upper() == 'S':
                set_archive(archive, path)

        elif opcao_2 == 3:
            archive = generate_new_text_unencrypted(archive, key, characters_order)
            show_archives([archive])

        else:
            print('Opção inválida')
    else:
        print('Opção inválida!')

    respost = str(input('Deseja continuar [S/N]: ')).upper()
    if respost == 'N':
        titulo('Esse é o fim obrigado e volte sempre!')
        break
