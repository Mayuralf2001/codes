print("Ficonacci Non-Recursive Series")

n=10
n1=0
n2=1

print(n1)
print(n2)
while(n-2):
    c = n1 + n2
    n1 = n2
    n2 = c
    print(c)
    n = n - 1
#Time Complexity  = T(N) -> Linear
#Space Complexity = O(1)