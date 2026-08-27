first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

first_name = first_name.strip().title().capitalize().upper()
last_name = last_name.strip().title().capitalize().upper()

full_name = first_name + " " + last_name

print("Full name:", full_name)