import os

characters_order = ['A', 'Á', 'À', 'Ã', 'Â', 'B', 'C', 'Ç', 'D', 'E', 'É', 'È', 'Ê', 'F', 'G', 'H', 'I', 'Í', 'Ì', 'J',
                   'K', 'L', 'M', 'N', 'O', 'Ó', 'Ò', 'Õ', 'Ô', 'P', 'Q', 'R', 'S', 'T', 'U', 'Ú', 'Ù', 'Û', 'V', 'W',
                   'X', 'Y', 'Z', 'a', 'á', 'à', 'ã', 'â', 'b', 'c', 'ç', 'd', 'e', 'é', 'è', 'ê', 'f', 'g', 'h', 'i',
                   'í', 'ì', 'j', 'k', 'l', 'm', 'n', 'o', 'ó', 'ò', 'õ', 'ô', 'p', 'q', 'r', 's', 't', 'u', 'ú', 'ù',
                   'û', 'v', 'w', 'x', 'y', 'z', '.', '-', ',', ':', '+', '\'', '!', '?', '0', '1', '2', '3', '4', '5',
                   '6', '7', '8', '9', '(', ')', '/', '_', '=', '\\', '[', ']', '*', '"', '<', '>', ';', ' ']


def load_archive(path):
    archive = open(path, 'r')
    lines_archive = archive.readlines()
    archive.close()
    for line in range(len(lines_archive)):
        lines_archive[line] = lines_archive[line].replace('\n', '')
    return lines_archive


def load_achives(pasta):
    listas = []
    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            listas.append(load_archive(pasta+'/'+arquivo))
    return listas


def generate_new_text_encrypted(lines_archive, key, characters_order):
    new_lines_archive = []
    counter_key = 0
    for line in lines_archive:
        new_line_archive = ''
        for character_text in line:
            for character_counter in range(len(characters_order)):
                if character_text == characters_order[character_counter]:
                    if character_counter + int(key[counter_key]) < len(characters_order) - 1:
                        new_character_pos = character_counter + int(key[counter_key])
                    else:
                        new_character_pos = ((character_counter + int(key[counter_key])) - (len(characters_order) - 1)) - 1
                    new_line_archive += characters_order[new_character_pos]
                    counter_key += 1
                    if counter_key > len(key) - 1:
                        counter_key = 0
        new_lines_archive.append(new_line_archive)

    return new_lines_archive


def generate_new_texts_encrypted(archives, key, characters_order):
    new_archives = []
    for archive in archives:
        new_archives.append(generate_new_text_encrypted(archive, key, characters_order))

    return new_archives


def generate_new_texts_unencrypted(archives, key, characters_order):
    new_archives = []
    for archive in archives:
        new_archives.append(generate_new_text_unencrypted(archive, key, characters_order))

    return new_archives


def generate_new_text_unencrypted(lines_archive, key, characters_order):
    new_lines_archive = []
    counter_key = 0
    for line in lines_archive:
        new_line_archive = ''
        for character_text in line:
            for character_counter in range(len(characters_order)):
                if character_text == characters_order[character_counter]:
                    new_character_pos = character_counter - int(key[counter_key])
                    new_line_archive += characters_order[new_character_pos]
                    counter_key += 1
                    if counter_key > len(key) - 1:
                        counter_key = 0
        new_lines_archive.append(new_line_archive)

    return new_lines_archive


def set_archive(lines_archive, path):
    arq = open(path, 'w+')
    for line in lines_archive:
        arq.write(line + '\n')
    arq.close()


def set_archives(archives, pasta):
    for diretorio, subpastas, arquivos in os.walk(pasta):
        contador = 0
        for arquivo in arquivos:
            set_archive(archives[contador], pasta+'/'+arquivo)
            contador += 1


def show_archives(archives):
    for archive in archives:
        print('='*100)
        for line in archive:
            print(line)
        print('='*100)


def titulo(frase):
    print('=' * 50)
    print(frase.center(50))
    print('=' * 50)


def menu(menu_list):
    contador = 1
    print('=' * 50)
    for item in menu_list:
        print(f'{contador} - {item}')
        contador += 1
    print('=' * 50)
    return int(input('Opção: '))

