dic1 = {'1':"Dheeraj",'2':"kashyap",'3':"Esha",'4':"Kashyap"}

dic1['5']="Rohan" #add new data 

-----------------------------------------
for dic in dic1:
    print(dic1[dic]) #print the values

-----------------------------------------

name = input(print("Enter the CX name"))

for dic in dic1:
    if dic == name:
        print(dic1[dic])  # Take customer ID as input to search
        break

-----------------------------------------

print(dic1)
