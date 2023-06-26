# 5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
#     - как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получания значений этого атрибута
#     нужно использовать методы get и set
class Dog:
    def __init__(self, name, weight, color):
        self.name = name
        self.weight = weight
        self.color = color

    def run(self):
        return 'I can run'

    def get_name(self):
        return f'My name is {self.name}'


# dog1 = Dog('Zak', 15, 'Black')
# print(dog1.get_name())
# print(dog1.color)

dog2 = Dog('Yard', 5, 'Brown')

print(dog2.run())


class Metis(Dog):
    def __init__(self, name, weight, color):
        super().__init__(name, weight, color)

    def run(self):
        return 'I can run fast'


dog3 = Metis('Yard', 5, 'Brown')
print(dog3.run())