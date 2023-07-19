def greet():
    name = input("Enter your name: ")
    print(f"Hello, {name}")

greet()


def greet(name):    
    print(f"Hello, {name}")

friends = ["Peter","Jason"]
greet(friends[0])


def return_nothing():
    return None

print(return_nothing)


def add(x,y=1): # a name argument y=1
    return x+y

print(add(12))

print(add(x=12,y=12))