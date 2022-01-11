l1=[1,2,3,4,5,6,7,8,9]
l2=[1,2,90,45,52,68,73,88,9]

def common_elem(l1,l2):
    common=[]
    count = 0
    for i in l1:
        for j in l2:
            if(i!=j):
                common.append(i)
                count = count +1
    print("Common Elemts in both the list are :", common)


common_elem(l1,l2)
