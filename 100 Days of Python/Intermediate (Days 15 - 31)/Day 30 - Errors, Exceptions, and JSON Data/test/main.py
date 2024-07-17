# Test Code
# By Marco Redulla
# Day 30 (17/07/2024)

# try:
#     FILEPATH = r"100 Days of Python\Intermediate (Days 15 - 31)\Day 30 - Errors, Exceptions, and JSON Data\test\a_file.txt"
#     file = open(FILEPATH, "r")
# except FileNotFoundError:
#     file = open(FILEPATH, "w")
#     file.write("Hello World!")
# except: # default catch statement
#     print("Error: An unknown error has occured.")
# else: # runs if no error has occured.
#     content = file.read()
#     print(content)
# finally: # runs regardless of situation
#     file.close()
#     print("file has been closed.")

height = float(input("Height (meters): "))
weight = int(input("Weight (kilograms): "))

if height > 3:
    raise ValueError("Human height should NOT be over 3 meters.")

bmi = weight / height ** 2
print(f"Your BMI is {bmi}.")