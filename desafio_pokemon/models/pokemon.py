#criando classe com os atributos dos pokemons trabalhados na pasta 'pokedex.py'
class Pokemon:
    def __init__(self, nome, foto, tipo1, tipo2, golpes):  
        self.nome = nome 
        self.foto = foto
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.golpes = golpes
