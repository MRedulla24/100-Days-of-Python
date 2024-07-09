#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Mail Merge
# By Marco Redulla
# Day 24 (09/07/2024)

FILEPATH = r"C:\Users\Intel NUC\Documents\GitHub\100-Days-of-Python\100 Days of Python\Intermediate (Days 15 - 31)\Day 24 - Files, Directories, and Paths\Mail Merge\Input\Letters\starting_letter.txt"
NAME_LIST = r"C:\Users\Intel NUC\Documents\GitHub\100-Days-of-Python\100 Days of Python\Intermediate (Days 15 - 31)\Day 24 - Files, Directories, and Paths\Mail Merge\Input\Names\invited_names.txt"
OUTPUT = r"C:\Users\Intel NUC\Documents\GitHub\100-Days-of-Python\100 Days of Python\Intermediate (Days 15 - 31)\Day 24 - Files, Directories, and Paths\Mail Merge\Output\ReadyToSend"

PLACEHOLDER = "[name]"
# get list of names
with open(NAME_LIST, "r") as file:
    name_list = file.read().split("\n")

# get overall message
with open(FILEPATH, "r") as file:
    message = file.read()

#code to write messages
for name in name_list:
    with open(f"{OUTPUT}\{name}.txt", "w") as file:
        file.write(message.replace(PLACEHOLDER, name))