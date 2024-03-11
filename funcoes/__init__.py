from time import sleep
import webbrowser #Biblioteca para abrir uma imagem no navegador
import requests #Interagir com a API
import json #Interagir com os arquivos JSON


def menu(tit = True, op='',  cor=36, str=''): #Menu principal | Tit = True = Vai ter título | op = Opções | Cor padrão = azul | str= Nome do título | 
    if tit:
        print(f'\033[{cor}m-='*25, end='')
        print('-\033[m')
        print(f'\033[1m{f"{str}":^50}\033[m')
        print(f'\033[{cor}m-='*25, end='')
        print('-\033[m')
        print(op)
        print(f'\033[{cor}m-='*25, end='')
        print('-\033[m')
    else:
        print(f'\033[{cor}m-='*25, end='')
        print('-\033[m')
        print(op)
        print(f'\033[{cor}m-='*25, end='')
        print('-\033[m')


def opcoes_menuprincipal(): #Se o n=True vai retornar com negrito
    return'''\033[1m1 - Cadastrar um novo personagem
2 - Vizualizar todos os personagens cadastrados na API
3 - Deletar algum personagem
4 - Ver a imagem de algum personagem
5 - Sobre
6 - Sair do programa\033[m'''


def opcoes_newcharacter():
    return'''\033[1m1 - Confirmar todos os dados
2 - Editar algum dado
3 - Cancelar\033[m'''


def opcoes_deletecharacter():
    return'''\033[1m1 - Deletar um personagem
2 - Cancelar\033[m'''

def opcoes_seeimagecharacter():
    return'''\033[1m1 - Ver a imagem do personagem
2 - Cancelar\033[m'''



def linha(cor, num): #Criar uma linha onde o primeiro parâmetro é o código da cor, e a segunda é a quantidade
    print(f'\033[1;0{cor}m-\033[m'*num)


def error(var):
    print(f'\033[1;31mERRO: "{var}" não é uma opção válida\033[m')
    print('\n\n')


def backToMenu(function):
    sleep(0.6)
    print('Voltando para o \033[36mMenu Principal\033[m')
    sleep(0.6)
    print('\n\n\n\n\n\n\n')
    function()


def see_image(link_imagem): # Abra o navegador padrão com o URL da imagem
    webbrowser.open(link_imagem, new=2)


def verify_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return not bool(data)  # Retorna True se o arquivo estiver vazio, False caso contrário
    except (FileNotFoundError, json.JSONDecodeError):
        # Lida com a situação em que o arquivo não existe ou não é um JSON válido
        return True
