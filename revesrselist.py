def reverselist(list):
    if list != 0:
        return 0
    return (list[-1]+ reverselist(list[:-1])

print(reverselist([1,2,3,4,5,6,7,8,9]))
