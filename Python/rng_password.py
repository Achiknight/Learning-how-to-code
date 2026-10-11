import random

charN=0



caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small = caps.lower()
char = "!@#$%^&*_+!@#$%^&*_+"

All = caps+small+char
password = ""
print(len(All),flush=True)

for i in range(12):
    k = random.randint(0,71)
    password = password + All[k]
    
print(password)
    