friend = "Jason"

user_name = input("Enter your name: ")
if user_name == friend:
     print("Hello frined!")
else:
    print("Hello there")
print("------")


if 5:
    print("it's 5")
    
friends_list = ["Peter", "Bob", "Jason"]
friends_set = {"Peter", "Bob", "Jason"}
friends_tuple = ("Peter", "Bob", "Jason")

my_best_friend = "Bob"

if my_best_friend in friends_list:
    print(f"My best friend {my_best_friend} in list")

if my_best_friend in friends_set:
    print(f"My best friend {my_best_friend} in set")
    
if my_best_friend in friends_tuple:
    print(f"My best friend {my_best_friend} in tuple")
  
    
name = "Bob"

friends = ["Jason", "Peter"]
family = ["Carl", "Bob"]

if name in friends:
    print(f" {user_name} is my friend")
elif name in family:
    print(f" {user_name} is part of my family")
else:
    print(f" I don't know you {user_name}")