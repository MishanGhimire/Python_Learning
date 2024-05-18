#Ask user for their name
#name = input("What's your name?")

#Remove white space from str
#name = name.strip()

#Capitalize user's first name
#name = name.capitalize()
##name = name.title()

#Remove whitespace from str and capitalize user's name both first and last name
#name = name.strip().title()

#Now making it more eaisier by making it onto fewer lines of code
name = input("What's your name? ").strip().title()

#Split user's name into first name and last name
first, last = name.split(" ")

#Say hello to user
print(f"hello, {name}")
