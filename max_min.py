"""arr = [12,34,56,78,90,1,2,3,46,7,8,9,898]
arr.sort()
print(arr)
print(arr[0])
print(arr[len(arr)-1]

def maximum(arr):
    max=arr[0]  ###find max with loop
    size=len(arr)
    for i in range(size):
        if(arr[i]>max):
            max=arr[i]
    return max
print(maximum(arr))"""

arr = [12,34,56,78,90,1,2,3,46,7,8,9,898]
arr.sort()
"""print(arr)
print(arr[0])
print(arr[len(arr)-1])"""

def min(arr):   #find min with loop
    min=arr[0]
    size=len(arr)
    for i in range(size):
        if(arr[i]<min):
            min=arr[i]
    return min
print(min(arr))
