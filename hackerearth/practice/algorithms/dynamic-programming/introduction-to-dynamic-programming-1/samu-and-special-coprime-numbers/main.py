g={}

def gcd(a, b):
    if(g.has_key(a)):
        if(g[a].has_key(b)):
            return g[a][b]
    else:
        g[a]={}
    if(not g.has_key(b)):
        g[b]={}
    mn=min(a,b)
    mx=max(a,b)
    if(mn==0):
        g[a][b]=g[b][a]=mx
        return g[a][b]
    else:
        g[a][b]=g[b][a]=gcd(mn, mx%mn)
        return g[a][b]

def chk(n):
    su=0
    sqsu=0
    while(n/10!=0):
        su+=(n%10)
        sqsu+=((n%10)**2)
        n/=10

    su+=(n)
    sqsu+=(n**2)

    if(gcd(su,sqsu)==1):
        return True
    else:
        return False

d={}

def spc(n):
    if(d.has_key(n)):
        return d[n]
    else:
        if(n==1):
            d[n]=1
        elif(chk(n)):
            d[n]=spc(n-1)+1
        else:
            d[n]=spc(n-1)
        return d[n]

t=int(raw_input())
l=[]
for i in xrange(t):
    s=map(int, raw_input().split())
    l.append((s[0],s[1]))

for i in l:
    x,y=i
    if(x==1):
        print spc(y)
    else:
        print spc(y)-spc(x-1)
