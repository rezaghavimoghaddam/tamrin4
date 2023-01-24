n = int(input("enter your number: "))

fibo = [1,2]

for i in range(2,n):
    fiboformul = fibo[i-1] + fibo[i-2]
    fibo.append(fiboformul)

print(fibo)