#!/usr/bin/python3
target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
sum_of_even = 0

for number in range (0, target + 1, 2):
    sum_of_even += number
print(sum_of_even)