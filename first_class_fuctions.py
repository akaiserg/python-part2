def greet():
    print("hello")

hello = greet

hello()



#avg = lambda seq : sum(seq) / len(seq)
#total = lambda seq: sum(seq)
#top = lambda seq: max(seq)


students = [
    {"name": "Jason", "grades": (60,70,50)},
    {"name": "Peter", "grades": (30,40,60)}
]

operations = {
    "avg": lambda seq : sum(seq) / len(seq),
    "total": lambda seq: sum(seq),
    "top": lambda seq: max(seq) 
}

for student in students:
    name = student["name"]
    grades = student["grades"]
    print(f"Student:{name}")    
    operation = input("Enter 'avg', 'total', 'top':  ")
    operation_function = operations[operation]
    print(operation_function(grades))
    