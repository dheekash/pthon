month = "February"

months_31_days = ("January", "March", "May", "July", 
					"August", "October", "December")

months_30_days = ("April", "June", "September", "November")

if month in months_31_days:
    print("The month ", month, "has 31 days")

elif month in months_30_days:
    print("The month ", month, "has 30 days")

else:
    print("The month ", month, "has 28 days")
    

