#importando bibliotecas necessarias para o funcionamento do codigo  
from flask.wrappers import Request 
from models.pokemon import Pokemon
from flask import Flask, render_template, request 
import requests 
import json

#criando uma instância da classe 'Flask' 
app=Flask(__name__, static_folder='static') 

#define a URL raiz e direciona ela ao template 'index.html' 
@app.route("/")
def index():
    return render_template("index.html") 

#define a URL /buscar, que é executada. Recebendo o nome do pokemon e instancia um objeto 'Pokemon'  
@app.route("/buscar", methods=["GET", "POST"]) 
def buscar():
    pokemon = Pokemon(request.form["nome"].lower(), "","","","")  
    #tentando fazer uma requisição a API do pokemon apartir do nome digitado pelo usuario  
    try:
        res = json.loads(requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon.nome}").text)   
        #sendo os dados encontrados, serão extraídos e atríbudos ao objeto Pokemon 
        result = res['sprites'] 
        result = result['front_default'] 
        pokemon.foto = result 
        pokemon.golpes = res["moves"][0]["move"]["name"] 
        pokemon.peso = res["weight"] 
        pokemon.altura = res["height"] 
        if len(res["types"]) == 2:
            pokemon.tipo1 = res["types"][0]["type"]["name"] + " | " + res["types"][1]["type"]["name"] 
        else:
            pokemon.tipo1 = res["types"][0]["type"]["name"] 
    #caso não seja encontrado na API, será retornado o template 'nao_enc.html' 
    except:
        return render_template("nao_enc.html")  
    #renderiza o template e passando os atributos do 'Pokemon' para serem exibidos 
    return render_template("index2.html",
    nome = pokemon.nome,
    foto = pokemon.foto,
    tipo1 = pokemon.tipo1,
    golpes = pokemon.golpes,
    peso = pokemon.peso,
    altura = pokemon.altura
    ) 

#caracteristica do Flask que possibilita mensagens de erro detalhadas, caso isso ocorra 
if __name__ == '__main__':
    app.run(debug=True) 