my_list = [3, 4, 5, 6, 9 , 755]
count = 0
for i in range(len(my_list)):
    if my_list[i] > 3:
        count = count + 1
        i = i +1
    else:
        i = i +1

print(count)
    
