"""
Напишите класс Car, представляющий машину, имеющий следующие свойства:

- бренд
- модель
- год выпуска

Так как данный класс используется в большом каталоге, его необходимо оптимизировать и создать класс, который использует коллекции slots

Сравните скорость работы двух классов: с коллекциями slots и без них. Для этого каждому классу напишите метод get_set_del, 
в котором происходи получение, присваивание и удаление значения.
"""


class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_set_del(self):
        self.brand = self.brand
        self.model = self.model
        self.year = self.year
        del self.year

class CarSlots:
    __slots__ = ("brand", "model", "year")

    def __init__(self, model, brand, year):
        self.model = model
        self.brand = brand
        self.year = year


    def get_set_del(self):
        self.brand = self.brand
        self.model = self.model
        self.year = self.year
        del self.year



if __name__ == "__main__":

    import timeit

    t1 = timeit.timeit(lambda: Car('Toyota', 'Corolla', 2022).get_set_del(), number = 10_000)
    t2 = timeit.timeit(lambda: Car('Toyota', 'Crown', 1990).get_set_del(), number = 10_000)

    print((t1-t2)/t1*100)
