m = int(input())
a = list(map(int,input().split()))
b = []
count = 0
for i in a:
    if i not in b and a.count(i)>1:
        b.append(i)
    if(a.count(i)==1):
        b.append(i)
print(*b)