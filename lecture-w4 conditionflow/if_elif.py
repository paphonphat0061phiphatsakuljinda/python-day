num_employees = int(input("Enter the number of employees: "))

if num_employees < 50:
    print("You are a small company.")
elif num_employees < 250:
    print("You are a medium-size company.")
elif num_employees >= 250:
    print("You are a large company.")