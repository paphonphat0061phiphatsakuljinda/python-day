test1 = float(input("Enter the score for test 1:"))
test2 = float(input("Enter the score for test 2:"))
tes3 = float(input("Enter the score for test 3:"))
average = (test1 + test2 + tes3) / 3
if average >= 95:
    print("That is a great average:", average)
else:
    print("The average score is:", average)