#Program 1
#Conditional Statements
#Create a program that will ask for grade percentage. Display the equivalent Grade/Mark and Description
#Ask for the grade
#Compute grade for the equivalent mark and description
#Print the mark and description

import math
print("PUP Grade Generator")
grade = float(input("Enter your grade:"))

Grade=math.ceil(grade)

if grade <= 65:
    print("You've got an ' Incomple / Withdrawn / Dropped ' mark.")
    print("Withdrawn")
    print("Please Try to Study Harder")

elif grade >= 65 and grade <= 74:
    print("You've got a ' 5.0 ' mark.")
    print("Failed")
    print("Please Try to Study Harder")

elif grade <= 75:
    print("You've  got a ' 3.0 ' mark.")
    print("Passed")
    print("Try to Study Harder")
    
elif grade >= 76 and grade <= 78:
    print("You've got a ' 2.75 ' mark.")
    print("Satisfactory! ★")

elif grade >= 79 and grade <= 81:
    print("You've got a ' 2.5 ' mark.")
    print("Satisfactory! ★") 

elif grade >= 82 and grade <= 84:
    print("You've got a ' 2.25 ' mark.")
    print("That's Good!★")

elif grade >= 85 and grade <= 87:
    print("You've got a ' 2.0 ' mark.")
    print("That's Good! ★")

elif grade >= 88 and grade <= 90:
    print("You've got a ' 1.75 ' mark.")
    print("That's Very Good! ★ ★ ★")
    
elif grade >= 91 and grade <= 93:
    print("You've got a ' 1.5 ' mark.")
    print("That's Very Good! ★ ★ ★")

elif grade >= 94 and grade <= 96:
    print("You've got a ' 1.25 ' mark.")
    print("That's Excellent! ★ ★ ★")

elif grade >= 97 and grade <= 99:
    print("You've got ' 1.0 ' mark.")
    print("That's Excellent! ★ ★ ★")

else: 
    print("★ Celebrate your Success! ★")