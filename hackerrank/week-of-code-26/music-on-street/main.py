n=int(raw_input())
s=map(int, raw_input().split())
a=[]
for i in s:
    a.append(i)
s=map(int, raw_input().split())
m=s[0]
hmn=s[1]
hmx=s[2]
df=hmx-hmn+1  # hmx = hmn+hmx-hmn

op={}

def opf(i,ms):
    if(op.has_key(i)):
        if(op[i].has_key(ms)):
            return op[i][ms]
    else:
        op[i]={}
    if(i==n-1):
        if(ms>=hmn and ms<=hmx):
            op[i][ms]=True
            return True
        else:
            op[i][ms]=False
            return op[i][ms]
    if(ms<hmn):
        op[i][ms]=False
        return op[i][ms]
    if(a[i+1]-a[i]>=hmn and a[i+1]-a[i]<=hmx):
        op[i][ms]=opf(i+1,ms-(a[i+1]-a[i]))
        return op[i][ms]
    else:
        op[i][ms]=False
        return op[i][ms]

def func(i,ms):
    if(i==n):
        return a[n-1]
    if(i==0):
        z=hmx
    else:
        z=min(hmx,a[i]-a[i-1])
    j=hmn
    while(j<=z):
        if(opf(i,ms-j)):
            return a[i]-j
        j+=1
    return func(i+1, ms)

print func(0,m)
