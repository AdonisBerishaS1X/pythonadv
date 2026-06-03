from abc import abstractclassmethod


class Animal:
    @abstractclassmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def mak_sound(self):
        print("ham ham ")


dog1=Dog()
dog1.make_sound()