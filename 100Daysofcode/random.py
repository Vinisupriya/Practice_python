import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
choice= len(names)
names1= random.randint(0,choice-1)
p= names[names1]
print(p + " is ggoing to buy the meal today!")
