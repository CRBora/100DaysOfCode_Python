#!/usr/bin/python3

print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ") # What is your name?
name2 = input("What is their name? ") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combined_names = name1 + name2
lower_names = combined_names.lower()

t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
total_t = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
total_l = l + o + v + e

love_score = int(str(total_t) + str(total_l))

if love_score < 10 or love_score > 90:
  print("Your score is {}, you go together like coke and mentos.".format(love_score))
elif love_score >=40 and love_score <=50:
  print("Your score is {}, you are alright together.".format(love_score))
else:
  print("Your score is {}.".format(love_score))
