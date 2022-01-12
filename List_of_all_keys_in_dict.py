dis={"a":[1,2,3,4,5,6],"b":2,"c":3,"d":4,"e":5}

print(dis.values()) #method 1

x=[*dis]        #method 2
print(x)

*x, = dis        #method 2
print(x)
