class Dog:
    def __init__(self):
        self.age = 0
        self.name = 0

    def bark(self):
        print("Woof")


def main():
    my_dog = Dog(10, "Fluffy")
    print(my_dog.name)


class Animal:
    pass

class Dog(Animal):
    def __init__(self, age, name):
        self.age = age
        self.name = name




