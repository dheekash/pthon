my_list = [1, 2, 3, 4]

def find_sum(s):
    if len(s) == 0:
        return 0
    else:
        return s[0] + find_sum(s[1:]) 

print(find_sum(my_list))
