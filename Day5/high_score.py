#!/usr/bin/python3
# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
  
highest_score = 0
# print(temp)

for next_score in student_scores:
   if next_score  > highest_score:
    highest_score = next_score

print("The highest score in the class is: {}".format(highest_score))