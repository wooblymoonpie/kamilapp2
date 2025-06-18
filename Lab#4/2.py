class Car:
  def move(self):
    print("Drive!")

class Boat:
  def move(self):
    print("Sail!")

class Plane:
  def move(self):
    print("Fly!")

'''
Each class has a method called move(), but:

Car's version of move() prints "Drive!"

Boat's version prints "Sail!"

Plane's version prints "Fly!"
'''

for x in (car1, boat1, plane1):
  x.move()

''' 
If x is a Car, it drives.

If x is a Boat, it sails.

If x is a Plane, it flies.
'''
# Inheritance + Polymorphism:
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  def move(self):
    print("Drive!")

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")


''' 
Vehicle is the parent class (base).

Car, Boat, Plane are child classes (subclasses).

Even though all of them have the same method name move(), they act differently depending on the class. 
'''