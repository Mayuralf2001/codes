def recurfib(n):
    if(n<=1):
        return n
    else:
        return(recurfib(n-1)+recurfib(n-2))
n1 = 10

if(n1<=0):
    print("Enter a positive number")
else:
    print("Fibonacci series using recursive method:")
    for i in range(n1):
        print(recurfib(i))

#Time Complexity  = T(2^n) exponential
#Space Complexity = O(N)