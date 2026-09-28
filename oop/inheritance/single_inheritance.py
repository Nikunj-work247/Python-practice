class Animal:
    def eat(self):
        print("This animal is eating.")


class Dog(Animal):
    def bark(self):
        print("The dog barks.")

my_dog = Dog()
my_dog.eat()   
my_dog.bark()  