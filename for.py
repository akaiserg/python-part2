friends = ["Peter", "Bob", "Jason"]
for friend in friends:
    print(friend+"\n")
    
for index in range(5):
    print(f"{index}")
print("\n")
for index in range(2,5):
    print(f"{index}")
print("\n")    
for index in range(10,20, 2):
    print(f"{index}")
    
    
students = [
    {"name": "Bob", "grade": 23},
    {"name": "Jason", "grade": 93},
    {"name": "Peter", "grade": 56},
]

for student in students:
    print(student["name"], student["grade"])
    
# destructuring tuple

currencies = 0.8, 1.2
usd, eur = currencies
friends = [("Bob", 12), ("Peter", 24)]
for name, age in friends:
    print(f"{name}, {age}")
    
# iterating 

friends_info = {"Peter":23, "Bob":24, "Jason":56}
for age in friends_info.values():# .keys() or .items()
    print(age)
    
    
cars = ["ok","ok","ok","faulty","ok","ok"]

for status in cars:
    if status == "faulty":
        print("stopping")
        break
    print(f"car's status {status}")
    
for status in cars:
    if status == "faulty":
        print("found faulty car skipping..")
        continue
    print(f"car's status {status}")
    
    
cars = ["ok","ok","ok","ok","ok","ok"]    
for status in cars:
    if status == "faulty":
        print("stopping")
        break
    print(f"car's status {status}")
else:
    print("all the cars ok")
