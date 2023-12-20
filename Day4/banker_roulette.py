#!/usr/bin/python3
names_string = input("What are your names?")
names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random
num_names = len(names)
name_to_print = random.randint(0, num_names -1)
name_to_pay = names[name_to_print]
print("{} is going to buy the meal today!".format(name_to_pay))
