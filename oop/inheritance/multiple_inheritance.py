class Swimmer:
    def swim(self):
        print("Swimming in water")

class Flyer:
    def fly(self):
        print("Flying on land")

class Duck(Swimmer, Flyer):
    pass
duck = Duck()
duck.swim()
duck.fly()