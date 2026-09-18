import numpy as np


def get_array():
    p = []     
    for i in range(9):
        k = int(input("enter num:- "))
        p.append(k)

    array = np.array(p)
    array = array.reshape(3,3)
    return array
    
while True:
    print("1. Find A^3\n2. Find A^2\n3. Find XA\n4. A-B\n5. Exit")
    
    
    ch = int(input("\nenter choice laa:- "))
    
    if ch == 1:
        A = get_array()
        temp = (A*A*A)
        print(f"\n{temp}\n")        
    
    if ch == 2:
        A = get_array()
        temp = (A*A)
        print(f"\n{temp}\n")
    
    if ch == 3:
            A = get_array()
            num = int(input("Enter the scalar: "))
            temp = (num*A)
            print(f"\n{temp}\n")       
    
    if ch == 4:
            A = get_array()
            B = get_array()
            temp = (A-B)
            print(f"\n{temp}\n")     