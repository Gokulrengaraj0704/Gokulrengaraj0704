class Animal:
    def run():
        print("I can run")

class Cheetah(Animal):
    def run():
        print("Using Method Overriding:  I am the fastest Animal")


animal = Animal
animal.run()

Cheetah = Cheetah
Cheetah.run()