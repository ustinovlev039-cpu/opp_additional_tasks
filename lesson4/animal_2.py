"""
Допишите код под условия в цикле так, чтобы вывод был корректным
"""


class Animal:

    def __init__(self, name):
        self.name = name

    def walk(self, voice=""):
        return voice


class Dog(Animal):

    def bark(self):
        return 'Bark!'


class Cat(Animal):

    def meow(self):
        return 'Meow!'



animals = [Dog('Dog1'), Dog('Dog2'), Cat('Cat1'), Dog('Dog3')]


if __name__ == "__main__":
    for animal in animals:
    # Должно выводиться Bark или Meow в зависимости от того какой класс
        if isinstance(animal, Dog):
            print(animal.bark())
        elif isinstance(animal, Cat):
            print(animal.meow())

