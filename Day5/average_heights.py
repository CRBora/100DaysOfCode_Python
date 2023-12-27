#!/usr/bin/python3
# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇

student_num = len(student_heights)
total_height = 0
for n in student_heights:
  total_height += n

avg_height = round(total_height/student_num)

print("total height = {}".format(total_height))
print("number of students = {}".format(student_num))
print("average height = {}".format(avg_height))
