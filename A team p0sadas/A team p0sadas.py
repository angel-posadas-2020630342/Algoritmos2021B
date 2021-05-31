a =int(input())
r = list()
k=0
for i in range(0,a):
    r = list(map(int, input().split()))
    if(sum(r)>1):
        k +=1
print(k)