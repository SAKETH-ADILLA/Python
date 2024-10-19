class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Nmae:  {self.name}, Age: {self.age}")

person1 = person("Raju",18)
person2 = person("Sai",19)

person1.display_info()
person2.display_info()