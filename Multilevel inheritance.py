class Animal:
    def speak(self):
        return "Animal Speaks"
class Mammal(Animal):
    def Walk(self):
        return "Mammal Walks"
class Dog(Mammal):
    def bark(self):
        return "Dog Barks"
dog= Dog()
print(dog.speak())
print(dog.Walk())
print(dog.bark())