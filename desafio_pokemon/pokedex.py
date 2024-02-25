from flask.wrappers import Request 
from models.pokemon import Pokemon
from flask import Flask, render_template, request 
import requests 
import json


app=Flask(__name__, static_folder='static') 

@app.route("/")
def index():
    return render_template("index.html") 

@app.route("/buscar", methods=["GET", "POST"]) 
def buscar():
    pokemon = Pokemon(request.form["nome"].lower(), "","","","")   
    try:
        res = json.loads(requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon.nome}").text)   
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
    except:
        return render_template("nao_enc.html")  
    return render_template("index2.html",
    nome = pokemon.nome,
    foto = pokemon.foto,
    tipo1 = pokemon.tipo1,
    golpes = pokemon.golpes,
    peso = pokemon.peso,
    altura = pokemon.altura
    ) 

if __name__ == '__main__':
    app.run(debug=True) 