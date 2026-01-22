from abc import abstractmethod

class Animal:
    def __init__(self, nome, idade, peso, raca, patas):
        self.nome = nome 
        self.idade = idade
        self.peso = peso
        self.raca = raca
        self.patas = patas


        @abstractmethod
        def saudar(self):
            pass

class Cachorro(Animal):
    def __init__(self, nome, idade, peso, raca, patas):
        super().__init__(nome, idade, peso, raca, patas)

    def saudar(self):
        print("Au Au")

class Gato(Animal):
    def __init__(self, nome, idade, peso, raca, patas):
        super().__init__(nome, idade, peso, raca, patas)

    def saudar(self):
        print("Miau Miau")


Cachorro1 = Cachorro("Rex", 5, 20, "Labrador", 4)
Gato1 = Gato("Mimi", 3, 5, "Siamês", 4)

Cachorro1.saudar()
Gato1.saudar()