# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------
NOME..: file_search_rename.py
LANG..: Python3
7TITULO: Modulo envio de dados
DATA..: 10/11/2023
VERSÃO: 0.1.00
HOST..: diversos
LOCAL.: diversos
OBS...: colocar nas linhas abaixo informações importantes sobre o programa
Programa em Python para procurar e renomear arquivos em todas as pastas a partir de uma pasta inicial.

Este programa recebe como entrada o caminho inicial, o nome do arquivo a ser procurado e o nome
do arquivo que será atribuído após a renomeação.
GERADO PELO CHATGPT
DEPEND: (informar nas linhas abaixo os recursos necessários para utilização)
-
-------------------------------------------------------------------------
Copyright (c) 2022 - Vya.Digital - Yves Marinho
This script is licensed under MIT version 3.0 or above
-------------------------------------------------------------------------
Modifications.....:
 Date          Rev    Author            Description
 06/10/2023    0      Yves Marinho      Elaboração
-------------------------------------------------------------------------
ATUALIZAÇÕES NECESSÁRIAS:
# TODO - PRECISA DE TRAMANETO EM CASO DE WILDCARDS

PARÂMETROS (informar os parâmetros necessários no exemplo de utilização):
    - path_inicial (str): Caminho inicial para iniciar a busca.
    - file_to_search (str): Nome do arquivo a ser procurado, pode conter caracteres coringa.
    - file_to_rename (str): Nome do arquivo após a renomeação, pode conter caracteres coringa.

EXEMPLO DE USO:
    # search_and_rename_files("c:\\user\\teste\\documents\\", "requirements.txt", "*.bak")
    Arquivo renomeado em: c:\\user\\teste\\documents\\pasta1
    Arquivo renomeado em: c:\\user\\teste\\documents\\pasta2

RESULTADO ESPERADO:
    Pastas onde foram encontrados os arquivos serão exibidas.


"""

import os
import glob
import shutil
import sys

def generate_file_name(file_path, file_to_rename):
    """
    Gera o novo nome do arquivo com base nos wildcards fornecidos.

    Args:
        file_path (str): Caminho completo do arquivo original.
        file_to_rename (str): Nome do arquivo após a renomeação, pode conter caracteres coringa.

    Returns:
        str: Novo nome do arquivo.

    Raises:
        ValueError: Se os parâmetros fornecidos não são válidos.
    """
    try:

        print("=== Função: %s ===" % (sys._getframe().f_code.co_name))
        # Obter partes do nome original do arquivo
        file_name, file_extension = os.path.splitext(os.path.basename(file_path))
        wildcard_parts = file_to_rename.split('.')
        print("=== Parâmetros recebidos ===")
        print(f"file_path type {type(file_path)}, content {file_path}")
        print(f"file_to_rename type {type(file_to_rename)}, content {file_to_rename}")
        print(f"file_name type {type(file_name)}, content {file_name}")
        print(f"file_extension type {type(file_extension)}, content {file_extension}")
        print(f"wildcard_parts type {type(wildcard_parts)}, content {wildcard_parts}")

        # Substituir wildcards pelos partes correspondentes do nome original do arquivo
        new_file_name = wildcard_parts[0].join(file_name.split(wildcard_parts[0]))
        # new_file_extension = wildcard_parts[1].join(file_extension.split(wildcard_parts[1]))
        new_file_extension = file_name + '.' + wildcard_parts[1]
        print(f"new_file_name type {type(new_file_name)}, content {new_file_name}")
        print(f"new_file_extension type {type(new_file_extension)}, content {new_file_extension}")

        # Montar o novo nome completo do arquivo
        new_file_name_full = os.path.join(os.path.dirname(file_path), f"{new_file_name}{new_file_extension}")
        print(f"new_file_name_full type {type(new_file_name_full)}, content {new_file_name_full}")


        print("=== Termino Função: %s ===" % (sys._getframe().f_code.co_name))
        return new_file_name_full

    except ValueError as ve:
        raise ValueError(f'Erro ao gerar o novo nome do arquivo: {ve}')

def search_and_rename_files(path_inicial, file_to_search, file_to_rename):
    """
    Procura e renomeia arquivos em todas as pastas a partir de uma pasta inicial.

    Args:
        path_inicial (str): Caminho inicial para iniciar a busca.
        file_to_search (str): Nome do arquivo a ser procurado, pode conter caracteres coringa.
        file_to_rename (str): Nome do arquivo após a renomeação, pode conter caracteres coringa.

    Returns:
        None: A função apenas exibe as pastas onde os arquivos foram encontrados.

    Raises:
        ValueError: Se os parâmetros fornecidos não são válidos.
        FileNotFoundError: Se o caminho inicial não existe.
    """
    print("=== Função: %s ===" % (sys._getframe().f_code.co_name))
    print("=== Parâmetros recebidos ===")
    print(f"path_inicial type {type(path_inicial)}, content {path_inicial}")
    print(f"file_to_search type {type(file_to_search)}, content {file_to_search}")
    print(f"file_to_rename type {type(file_to_rename)}, content {file_to_rename}")
    try:
        # Validar os parâmetros recebidos
        if not os.path.exists(path_inicial):
            raise FileNotFoundError(f'O caminho "{path_inicial}" não existe.')

        # Listar todos os arquivos correspondentes ao padrão em todas as pastas
        files_to_rename = glob.glob(os.path.join(path_inicial, '**', file_to_search), recursive=True)

        # Renomear os arquivos
        for file_path in files_to_rename:
            new_file_path = generate_file_name(file_path, file_to_rename)
            shutil.move(file_path, new_file_path)

            # Exibir as pastas onde os arquivos foram encontrados
            print(f'Arquivo renomeado em: {os.path.dirname(new_file_path)}')

    except ValueError as ve:
        print(f'Erro: {ve}')
    except FileNotFoundError as fe:
        print(f'Erro: {fe}')
    print("=== Termino Função: %s ===" % (sys._getframe().f_code.co_name))


# Exemplo de Uso
if __name__ == "__main__":
    path_inicial = "C:\\Users\\info\\Documents\\Projetos sysdev\\scripts"
    file_to_search = "requirements.txt"
    file_to_rename = "*.bak"
    search_and_rename_files(path_inicial, file_to_search, file_to_rename)
