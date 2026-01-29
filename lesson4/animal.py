"""
Напишите класс Animal, представляющий животное, имеющий следующие методы:

- __init__(self, name): конструктор, принимающий имя животного;
- speak(self): метод, который выводит звук, издаваемый животным.

Напишите класс Dog, наследующийся от класса Animal, представляющий собаку, имеющий следующие методы:

- speak(self): метод, который выводит звук, издаваемый собакой.

Напишите класс Cat, наследующийся от класса Animal, представляющий кошку, имеющий следующие методы:

- speak(self): метод, который выводит звук, издаваемый кошкой.
"""


class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self, voice="?"):
        return voice



class Dog(Animal):

    def speak(self, voice="Woof!"):
        return voice

class Cat(Animal):

    def speak(self, voice="Meow!"):
        return voice


if __name__ == "__main__":
    # код для проверки
    animal = Animal("Animal")
    print(animal.speak())  # ?

    dog = Dog("Dog")
    print(dog.speak())  # Woof!

    cat = Cat("Cat")
    print(cat.speak())  # Meow!
