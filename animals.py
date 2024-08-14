"""
Crie uma classe chamada Animal e outra chamada Zoologico.
Na classe Animal, inclua os atributos name, especie, e age.
Na classe Zoologico, crie uma lista para armazenar os animais e implemente os sseguintes métodos
adicionar_animal, remover_animal, listar_animais, buscar_animal, e contar_animais.

"""


class Animal:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        
    def __str__(self) -> str:
        return f' Nome do animal: {self.name}\n raça: {self.breed}\n idade: {self.age}'

class Zoo:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.animals = []
        
    def __str__(self) -> str:
        return f' Zoologico {self.name} {self.address}'

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, name):
        for animal in self.animals:
            if animal.name == name:
                self.animals.remove(animal)
                return f'{name} removido da lista'
        return f'{name} não foi encontrado'

    def list_animals(self):
        for animal in self.animals:
            print(f"Nome: {animal.name}, Raça: {animal.breed}, Idade: {animal.age}")

    def search_animal(self, name):
        for animal in self.animals:
            if animal.name == name:
                print('animal encontrado')
                return animal
        return f" O animal '{name}' não existe nessa lista"

    def count_animals(self):
        return len(self.animals)

cao = Animal('spike', 'pastor alemão', 3)
gato = Animal('bernado', 'sphynx', 2)
rato = Animal('rato', 'camundongo', 1)

zoo = Zoo('Parque Natural', 'Av. campo sales - 2258 porto velho - RO')
print(zoo)

zoo.add_animal(cao)
zoo.add_animal(gato)
zoo.add_animal(rato)
zoo.list_animals()

print('-' * 50)
print(zoo.search_animal('spike'))

print(zoo.remove_animal('rato'))

print(zoo.count_animals())


