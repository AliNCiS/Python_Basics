# This repository was created by Ali Hajian as part of university coursework.

# functions

def Fun1():
    print("Hi")

Fun1()

def Fun1(x):
    print(F"print: {x}")

Fun1(85)

def Fun1(x,y):
    return x+y

print(Fun1(2,10))

def Fun1(name ="Ali"):
    print(name)

Fun1()
Fun1("Ali Hajian")

def Fun1(*Arga):
    total = 0
    for x in Arga:
        total += x
    return total

print(Fun1(1,2,3,4,5))


def Fun1(**key):
    for key,value in key.items():
        print(f"key: {key} is: {value}")
    
Fun1(name = "Ali",age = "20",myCar = "Saina S")


def Fun1():
    x = lambda x,y:x+y
    print(x(1,1))

Fun1()


def Fun1(n):
    return len(n)

a = list(map(Fun1,('Ablfz','Amir','Ali')))
print(a)
# or
Li = [1,2,4,5,6,7]
squared = list(map(lambda x:x**2,Li))
print(squared)

fI = [1,2,4,5,6,7]
squared = list(filter(lambda x:x%2==0,Li))
print(squared)
# بر اساس سم مرتب میکنه
students = [("Ali", 22), ("Amir", 19), ("Ablfz", 24)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)





    