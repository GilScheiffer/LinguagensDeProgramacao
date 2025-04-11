class Animal:
    def fazer_som(self):
        print("O animal faz um som.")

class Cachorro(Animal):
    def fazer_som(self):
        print("O cachorro late: Au Au!")

class Gato(Animal):
    def fazer_som(self):
        print("O gato mia: Miau!")

# Programa principal
animal = Animal()
cachorro = Cachorro()
gato = Gato()

animal.fazer_som()
cachorro.fazer_som()
gato.fazer_som()
