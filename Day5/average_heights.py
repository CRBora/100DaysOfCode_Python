#!/usr/bin/python3
# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇

total_height = 0
for n in student_heights:
  total_height += n
print("total height = {}".format(total_height))

student_num = 0
for student in student_heights:
  student_num += 1
print("number of students = {}".format(student_num))

avg_height = round(total_height/student_num)

print("average height = {}".format(avg_height))

# My original code before correction acoording to instructions

#studen_num = len(student_heights)
#total_height = 0
# for n in student_heights:
#   total_height += n

# avg_height = round(total_height/student_num)

# print("total height = {}".format(total_height))
# print("number of students = {}".format(student_num))
# print("average height = {}".format(avg_height))