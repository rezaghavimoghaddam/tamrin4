import random

n = int(input("how many numbers you need? "))
nrrn = []

for i in range(n):
    nrrn_number = random.randint(0, 100)
    nrrn.append(nrrn_number)

nrrn = set(nrrn)
   
print(nrrn)