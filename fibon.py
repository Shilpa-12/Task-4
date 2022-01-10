def fibon(n):
    if n<=1:
       return n
    else:
       return(fibon(n-1)+fibon(n-2))
num=13
print("Fibonacci sequence:")
for i in range(num):
    print(fibon(i))
        