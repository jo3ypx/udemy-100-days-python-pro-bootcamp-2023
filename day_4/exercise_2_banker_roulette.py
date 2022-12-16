import random

names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(", ")
person = random.randint(0, len(names))
print(names[person] + " is going to buy the meal today!")
