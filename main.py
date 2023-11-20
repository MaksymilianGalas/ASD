def fibbonacci(x):
    if(x==0):
        return 0
    elif(x==1):
        return 1
    else:
        return fibbonacci(x-1) + fibbonacci(x-2)

for i in range(10):
    print(fibbonacci(i))