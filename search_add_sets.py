numbers={23,23,24,25,26,27,28,29,30}


numbers.add(31)
print(numbers)  # Add a new data

"""-------------------------------------"""

srch_num=int(input(print("Enter the number")))

for var in numbers:
    if var==srch_num:
        print("Number found")
        break
    print("Number not found")
    break
