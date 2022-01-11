arr=[1,2,3,4,4,5,5,6,7,7,8,8,9,9,9,1,2,4,5,]

#arr2 = list(set(arr))
#print(arr2)

"""arr3=[]

for i in arr:
    if(i not in arr3):
        arr3.append(i)
print(arr3)"""


"""rem_dup = lambda arr : set(arr)

print(rem_dup(arr)) """


dict1={'car':["Ford", "Toyota", "Ford", "Toyota"],'brand':["Mustang","Ranz","Mustang","Ranz"]}

dict2 ={}

for key,value in dict1.items():
    dict2[key] = set(value)
print(dict2)
