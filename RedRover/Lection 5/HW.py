# 5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
#     - как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получания значений этого атрибута
#     нужно использовать методы get и set

# class Dog:
#     def __init__(self, name, color, age):
#         self.__name = name
#         self.color = color
#         self.age = age
# 
# 
# dog1 = Dog('Zak', 'black', 5)
# print(getattr(dog1, '__name'))


class Cat:
    def __init__(self, name, age):
        self._name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name


cat1 = Cat('Bars', 1)
#print(cat1.name, ' ', cat1.get_age())
cat1.set_age(2)
cat1._Cat__age = 3
print(cat1.get_name(), ' ', cat1.get_age())

