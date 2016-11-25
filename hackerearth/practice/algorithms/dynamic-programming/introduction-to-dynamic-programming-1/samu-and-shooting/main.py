x=y=n=w=p1=p2=0
d={}

def pmax(s, i):
    if(d.has_key(s)):
        if(d[s].has_key(i)):
            return d[s][i]
    else:
        d[s]={}
    if(s<=0):
        d[s][i]=1
        return d[s][i]
    elif(i==n):
        if(s<=mn):
            d[s][i]=max(p1, p2)
            return d[s][i]
        elif(s<=mx):
            d[s][i]=p
            return d[s][i]
        else:
            d[s][i]=0
            return d[s][i]
    else:
        d[s][i]=max((p1*pmax(s-x,i+1)+(1-p1)*(pmax(s,i+1))),(p2*pmax(s-y,i+1)+(1-p2)*(pmax(s,i+1))))
        return d[s][i]

t=float(raw_input())
for i in xrange(int(t)):
    s=map(float, raw_input().split())
    x=s[0]
    y=s[1]
    n=s[2]
    w=s[3]
    p1=s[4]
    p2=s[5]
    p1=p1/100
    p2=p2/100
    mx=max(x, y)
    mn=min(x, y)
    if(x==mx):
        p=p1
    else:
        p=p2
    d={}
    ans=pmax(w,1)
    ans*=100
    print ("%0.6f"%ans)
