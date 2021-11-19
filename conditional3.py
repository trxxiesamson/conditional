# Program 3 : Life Stages
# Conditional Statements
# Create a program that will ask for an age of a person
# Display the life stage of the person
# Rules 
# 0 - 12 : KID
# 13 - 17 : TEEN
# 18 : YOUNG ADULT / DEBUT
# 19 and above : ADULT

print("LIFE STAGES OF A PERSON ☻ ")

age= int(input("Enter age:"))
if -1 < age <= 12:
    print('You are still a Kid ')
elif 13 >= age <= 17:
    print('Enjoy being a Teen ')
elif age == 18:
    print('You are a Debutant')
else:
    print('Welcome to Adult - hood!')