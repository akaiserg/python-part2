friends = ["Jason", "Jhon", "Arthur", "Peter"]

print(friends[1:4])
print(friends[:4])
print(friends[:]) # is a new list

print(friends[-2:])
print(friends[:-1])
print(friends[-3:-1])


numbers = [0,1,2,3,4,5,6]


double_number= [number * 2 for number in range(6)]

print(double_number)

double_number= [2 * 2 for _ in range(6)]

ages = [22,34,45,55,34]

odds = [age for age in ages if age %2 == 1]


friends2 = ["Jason", "Peter", "Robert"]

for counter, friend in enumerate(friends2):
    print(counter, friend)
    
print(list(enumerate(friends2)))

print(list(zip([0,1,2], friends2)))