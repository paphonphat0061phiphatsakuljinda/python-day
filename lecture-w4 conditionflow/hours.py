hour=int(input("Enter the hour:"))
rate=float(input("Enter the rate:"))

if hour <= 40:
    pay=hour*rate
    print("The gross pay is:", pay)
else:
    pay=(40*rate)+(hour-40)*rate*1.5
    print("The gross pay is $:", pay)