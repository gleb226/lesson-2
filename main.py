class Cat:
    def __init__(self,name):
        self.name = name

    def play(self,person):
        print('I`m playing with', person.name)
        person.isHappy = True


class Person:
    isHappy = False
    def __init__(self, name, age):
        self.name = name
        self.age = age




my_cat = Cat("Barsik")
me = Person("Hlieb", 12)
friend = Person("Venya", 12)
print(me.isHappy)

my_cat.play(me)
print(me.isHappy)
my_cat.play(friend)
