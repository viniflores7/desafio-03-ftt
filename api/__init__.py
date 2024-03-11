from flask import Flask, jsonify, request #Flask = Servidor | Jsoinfy = Retornar em um formato json | Request = Acessar os dados
from tinydb import TinyDB, Query


app = Flask(__name__) #Criando um app com o nome do arquivo atual
db = TinyDB('./api/characters.json', indent = 4) #Criando o banco de dados caso não exista na pasta API


# Consultar (todos os dados)
@app.route('/characters',methods=['GET'])  #methods = Aceitar apenas o método "GET"
def API_see_AllCharacters():
    characters = db.all()
    return jsonify(characters) #Retorna todos os personagens em formato JSON


# Criar um novo personagem
@app.route('/characters',methods=['POST']) #methods - Aceitar apenas o método "POST"
def API_new_character():
    new = request.get_json()
    db.insert(new)
    return jsonify({'Mensagem': 'Personagem adicionado com sucesso!'})


# Excluir um personagem já cadastrado por nome
@app.route('/characters/<string:name>',methods=['DELETE'])
def API_delete_character(name):
    Character = Query() #Realizar consultas nos dados armazenados no banco de dados.
    db.remove(Character.Nome == name)
    characters = db.all()
    return jsonify(characters)


#Pegar a URL da imagem de um personagem por nome
@app.route('/characters/<string:name>', methods=['GET'])
def API_seeimage_character(name):
    Character = Query()
    character = db.get(Character.Nome == name)
    if character:
        image_url = character.get('Link')
        return jsonify(image_url)
    else:
        return jsonify({'Mensagem': 'Personagem não encontrado'}), 404


app.run(port='5000',host='localhost',debug=True) #Inicializando o servidor
