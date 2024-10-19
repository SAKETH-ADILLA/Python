class Animal:
    def __init__ (self,name):
        self.name= name
        print(f"{self.name} has been Created")

    def __del__(self):
        print(f"{self.name} has been destroyed")

d = Animal("Buddy")

del d