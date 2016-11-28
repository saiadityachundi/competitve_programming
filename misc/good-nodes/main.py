n=int(raw_input())
pt={}
for i in xrange(n):
    s=int(raw_input())
    pt[i+1]=s

def des(i):
    l=[i]
    i=pt[i]
    while(i!=1 and not(i in l)):
        l.append(i)
        i=pt[i]
    return i

cnt=0

i=2
while(i<=n):
    di=des(i)
    if(di!=1):
        pt[di]=1
        cnt+=1
    i+=1

print cnt
