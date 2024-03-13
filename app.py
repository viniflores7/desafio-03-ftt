from time import sleep
import webbrowser #Biblioteca para abrir uma imagem no navegador
import requests #Interagir com a API
import json #Interagir com os arquivos JSON
from funcoes import *


def main(): #Função principal para rodar o programa
    while True:
        menu(True, opcoes_menuprincipal(), str="GERENCIADOR DE PERSONAGENS")
        op = str(input('\033[1mOpção =--> \033[m')).strip()
        if op == '1':
            new_character()
        elif op == '2':
            see_character(n=True)
        elif op == '3':
            delete_character()
        elif op == '4':
            see_image_character()
        elif op == '5':
            sobre()
        elif op == '6':
            sair()
        else:
            error(op)


def new_character():
    linha(32,55)
    temp = dict()
    temp["Nome"] = str(input('Digite o nome do personagem: ')).strip().capitalize()
    temp["Descrição"] = str(input('\nDigite a descrição do seu personagem: ')).strip().capitalize()
    print('\n\033[1mOBS: Copie e cole o link da imagem, quando ir na opção "Vizualizar todos os personagens cadastrados" caso o link esteja inválido, ele abrirá no seu navegador padrão e irá mostrar uma mensagem de erro.')
    print('Como pegar o link? Clique com o botão direito do mouse em "Copiar o endereço da imagem" e cole na opção abaixo.')
    temp["Link"] = str(input('Digite o link para imagem: \033[m')).strip()
    temp["Programa"] = str(input('\nPrograma: ')).strip().capitalize()
    temp["Animador"] = (input('\nAnimador: ')).strip().capitalize()
    while True: # Entrando no meu de confirmação de dados
        linha(32,55)
        sleep(0.3)
        print('As informações cadastradas foram:')
        for n, i in temp.items():
            print(f'\033[1m{n}\033[m: {i}')
        menu(False, opcoes_newcharacter(), 32)
        op = str(input('\033[1mOpção =--> \033[m')).strip()
        if op == '1': #Confirmar todos os dados
            response = requests.post(url, json=temp.copy()) #json=variável a ser adicionada na API
            sleep(0.2)
            if response.status_code != 200: #Lidando com os erros da API
                print(f'Ocorreu um erro ao adicionar o personagem. Código de status: {response.status_code}')
                backToMenu(main)
            else:
                temp.clear() #Limpando o dicionário temporário para as próximas adições
                print(f'O personagem foi adicionado com sucesso!')
                print('\033[1mTodos os dados foram adicionados com \033[1;32mSUCESSO\033[m')
                sleep(0.4)
                backToMenu(main)
        elif op == '2': #Alteração de informações
            inf = str(input('Qual o nome da informação que você deseja alterar: ')).capitalize().strip()
            if inf != 'Nome' and inf != 'Descrição' and inf != 'Link' and inf != 'Programa' and inf != 'Animador':
                error(inf)
            else:
                temp[f"{inf}"] = str(input(f'{inf}: ')).strip().capitalize()
        elif op == '3': # Cancelar
            backToMenu(main)
        else:
            error(op)


def see_character(n=False): #Ver os personagens e a imagem cadastrada
        if verify_json('./api/characters.json'): #Se não tiver nenhum personagem cadastrado
            linha(34, 50)
            print('Ainda não existe nenhum personagem cadastrado!')
            linha(34, 50)
            sleep(0.7)
            backToMenu(main)
        else:  #Caso já tenha personagens cadastrados
            response = requests.get(url)
            if response.status_code == 200:
                linha(34, 50)
                characters = response.json()
                if characters and isinstance(characters, list):  # Verifica se characters é uma lista não vazia
                    linha(34, 50)
                    for character in characters:
                        if isinstance(character, dict):  # Verifica se cada item da lista é um dicionário
                            print(f"Nome: {character.get('Nome')}")
                            print(f"Descrição: {character.get('Descrição')}")
                            print(f"Link para imagem: {(character.get('Link'))[0:20]}...") # Deixando o Link menor
                            print(f"Programa: {character.get('Programa')}")
                            print(f"Animador: {character.get('Animador')}")
                            linha(34, 50)
                        else:
                            print("Um item na lista não é um dicionário válido de personagem.")
                else:
                    print('Ainda não existe nenhum personagem cadastrado!')
                    linha(34, 50)
                    backToMenu(main)
                if n: #Se n=True ele vai voltar para o menu principal
                    op = str(input('Aperte "Enter" para voltar para o menu principal: '))
                    op = 2
                    if op == 2:
                        backToMenu(main)
            else:
                print(f'Ocorreu um erro ao adicionar o personagem. Código de status: {response.status_code}')
                backToMenu(main)


def delete_character():
    while True:
        see_character(n=False)
        menu(False, opcoes_deletecharacter(), 30)
        op = str(input('\033[1mOpção =--> \033[m')).strip()
        if op == '1':        
            nome = str(input('Digite o nome do personagem que você quer deletar: ')).capitalize().strip()
            conf = str(input(f'Você confirma o nome digitado? [S/N] \033[1m{nome}\033[m ')).strip().upper()
            if conf != 'S':
                backToMenu(main)
            else:
                response = requests.get(f'{url}/{nome}') #Vendo se o personagem existe
                if response.status_code == 200:
                    response = requests.delete(f'{url}/{nome}') #Deletando o personagem
                    if response.status_code == 200:
                        print(f'\033[1;31mPersonagem "{nome}" deletado com sucesso.\033[m')
                        backToMenu(main)
                    else:
                        print(f'Ocorreu um erro ao deletar o personagem. Código de status: {response.status_code}')
                        backToMenu(main)
                else:
                    print(f'O personagem "{nome}" não existe.')
        elif op == '2':
            backToMenu(main)
        else:
            error(op)


def see_image_character(): #Ver o link do personagem
    while True:
        see_character(n=False)
        menu(False, opcoes_seeimagecharacter(), 37)
        op = str(input('\033[1mOpção =--> \033[m')).strip()
        if op == '1':        
            nome = str(input('Digite o nome do personagem que você quer ver a imagem: ')).capitalize().strip()
            conf = str(input(f'Você confirma o nome digitado? [S/N] \033[1m{nome}\033[m ')).strip().upper()
            if conf != 'S':
                backToMenu(main)
            else:
                response = requests.get(f'{url}/{nome}') #Vendo se o personagem existe
                if response.status_code == 200:
                    response = requests.get(f'{url}/{nome}')
                    if response.status_code == 200:
                        url_imagem = response.json() #Pegando a URL do personagem
                        see_image(url_imagem)
                        backToMenu(main)
                    else:
                        print(f'Ocorreu um erro ao adicionar o personagem. Código de status: {response.status_code}')
                        backToMenu(main)
                else:
                    print(f'O personagem "{nome}" não existe.')
        elif op == '2':
            backToMenu(main)
        else:
            error(op)


def sobre(): #Sobre do programa
    linha(33, 52)
    print('''\033[1mEste é um Gerenciador de Personagem onde:\n
1 - Você pode cadastrar seu personagem, editar as informações antes de confirma-lo
2 - Você pode abrir o link da imagem que anexar e ela irá abrir em seu navegador padrão (Todas as orientações estão no cadastro). Caso o link para a imagem do personagem for inválido, ele não irá abrir.
3 - É importante que você esteja rodando o arquivo da API, caso contrário as interações com ela não irão funcionar, consequentemente, o programa irá dar erro.
\nDono do projeto e programador: Vinícius Flores Ribeiro
Versão: 1.8 BETA''')
    linha(33, 52)
    con = str(input('Aperte "Enter" para voltar para o Menu Principal: '))
    con = 2
    if con == 2:
        backToMenu(main)


def sair(): #Sair do programa
    linha(33, 52)
    print('Muito obrigado por usar o Gerenciador de Personagens')
    sleep(0.8)
    print('Encerrando o programa', end='')
    for c in range(0,3):
        print('.', end='', flush=True)
        sleep(0.5)
    print('\n\033[1;32m[PROGRAMA ENCERRADO COM SUCESSO]\033[m')
    exit()


#Programa principal
url = "http://localhost:5000/characters"
print(f'\033[1mATENÇÃO: É IMPORTANTE QUE VOCÊ ESTEJA COM O CÓDIGO DA API EM EXECUÇÃO PARA QUE TODAS AS INTERAÇÕES SEJAM FEITAS COM \033[1;32mSUCESSO!\033[m')
confirm = input('Digite "Enter" para começar o programa: ')
confirm = 2
if confirm == 2:
    print('\n\n\n\n\n\n\n\n\n')
    main()
