#!/usr/bin/python2

n=int(raw_input())
a=0
x=map(int, raw_input().split())
for i in xrange(n):
    a+=(x[n-i-1]*(2**i))

b=0
x=map(int, raw_input().split())
for i in xrange(n):
    b+=(x[n-i-1]*(2**i))

xr=a^b

vr={}
vr[0]=(1+(2**(n-1))+(2**(n-2)))
vr[1]=(3+(2**(n-1)))
vr[2]=(7)
i=3
while(i<n):
    vr[i]=vr[i-1]*2
    i+=1

ck={}

def chk(ind, num):
    if(ck.has_key(ind)):
        if(ck[ind].has_key(num)):
            return ck[ind][num]
    else:
        ck[ind]={}
    if(num==0):
        ck[ind][num]=0
        return 0
    if(ind==n-1):
        if(num==vr[n-1]):
            ck[ind][num]=1
            return 1;
        else:
            ck[ind][num]=float("inf")
            return float("inf")
    m1=1+chk(ind+1, num^vr[ind])
    m2=chk(ind+1, num)
    if(m1<m2):
        ck[ind][num]=m1
        return m1
    else:
        ck[ind][num]=m2
        return m2

ans=chk(0,xr)
if(ans==float("inf")):
    print "impossible"
else:
    print ans
