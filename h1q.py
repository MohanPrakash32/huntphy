k=int(input())
l=input().split()
m=[]
n=''
for i in l:
    if l.count(i)>1 and i not in m:
        m.append(i)
if len(m)>0:
    for i in range(len(m)-1):
        d+=m[i]+" "
    print(d+m[-1])
else:
    print("unique")
