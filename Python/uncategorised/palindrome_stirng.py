String = input("enter a string:- ")
temp = ""
for val in String:
    temp = val + temp
    
print (temp)
if temp == String:
    print("True")
    
else: print("False")