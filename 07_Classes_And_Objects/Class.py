class Person:
    def __init__(self, name, age):  #Constructor
        self.name = name
        self.age = age

    def greet(self):  # متد (تابع داخل کلاس)
        print(f"My Name is {self.name} Old {self.age}")

p = Person("Ali",20)
p.greet()
#Get Attributes Class Person
print(p.name)
print(p.age)

# More objects
p2 = Person("Sara", 19)
p3 = Person("Reza", 25)
p2.greet()
p3.greet()

#More Method in Faction 
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        self.speed = 0

    def accelerate(self):
        self.speed += 10
        print(f"{self.brand} is now going {self.speed} km/h")

    def brake(self):
        self.speed -= 10
        print(f"{self.brand} slowed down to {self.speed} km/h")

my_car = Car("Saina S", 2025)
my_car.accelerate()
my_car.brake()


#Inheritance

class Animal:
    def speak(self):
        print("An animal makes a sound")
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def speak(self):
        print("Woof!")

dog = Dog()
dog.eat()
dog.speak()

# Super()
class Person:
    def __init__(self,name):
        self.name = name
    def sayhello(self):
        print(F"hello {self.name}")

class Student(Person):
    def __init__(self,name,id):
       super().__init__(name)
       self.id  = id
    def introduce(self):
        print(F"Im am {self.name} and My Id is {self.id}")

s = Student("Ali hajian",3232)
s.sayhello()
s.introduce()


# Polymorphism
class Cat:
    def speak(self):
        return "Meow"

class Dog:
    def speak(self):
        return "Woof"

# هر دو کلاس متد speak دارن، ولی خروجی‌شون فرق می‌کنه
animals = [Cat(), Dog()]

for animal in animals:
    print(animal.speak())

class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"


def make_it_speak(animal):
    print(animal.speak())


dog = Dog()
cat = Cat()

make_it_speak(dog)
make_it_speak(cat)


from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass  


class Dog(Animal):
    def speak(self):
        return "Woof!"  

class Cat(Animal):
    def speak(self):
        return "Meow!"  


 
