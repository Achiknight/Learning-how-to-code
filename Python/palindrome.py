        
def ispal(x):
    check = 0
    temp = x
    k = len(str(x)) -1 
    while x >0:
        dig = x%10
        check = check + (dig)*(10**k)
        
        x = x//10
        k -= 1
        print(x)
        print("check is ",check)
    if temp == check:
        
        return True
    else:
        return False


pal = ispal(121)
print(pal)