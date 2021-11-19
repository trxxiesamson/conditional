# Program 2 : Find the lowest number
# Conditional Statements
# Create a program that will ask 3 numbers
# Find the lowest number using only if-else statement
# Display the lowest number among the three

print("LOWEST NUMBER GENERATOR")
print("below you can find the lowest number among three numbers that you're allowed to input")

user_first_num = float(input("First Number: "))
user_second_num = float(input("Second Number: "))
user_third_num = float(input("Third Number: "))

if user_first_num < user_second_num and user_first_num < user_third_num:
    lowest_number = user_first_num

elif user_second_num < user_first_num and user_second_num < user_third_num:
    lowest_number = user_second_num

elif user_third_num < user_first_num and user_third_num< user_second_num:
    lowest_number = user_third_num

print("The lowest number is", lowest_number)