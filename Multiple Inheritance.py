class Animal:
    def speak(self):
        return "Animal Speaks"
class Bird:
    def fly(self):
        return "Bird Flies"
class parrot(Animal,Bird):
    def __init__(self,name):
        self.name = name
    def info(self):
        return f"{self.name} is a parrot"
parrot = parrot("Parry")
print(parrot.info())
print(parrot.speak())
print(parrot.fly())