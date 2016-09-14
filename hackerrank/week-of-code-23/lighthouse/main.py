#!/usr/bin/python2

import math

def ck(l,p,q,n,r):
    if(p>n or q>n or p<1 or q<1 or r<0):
        return -1
    elif(p+r>n or q+r>n or p-r<1 or q-r<1):
        return -1
    elif(r>(n/2)):
        return -1
    else:
        if(r==0):
            if(l[(p,q)]==0): return 0
            else:
                return -1
        
        i=p-r
        j=q
        while(i!=p+1):
            d=math.floor(math.sqrt((r**2)-((i-p)**2)))
            d=int(d)
            j=q+d
            if(i!=p and j!=q):
                if(l[(i,j)]==1):
                    return -1
                j=q-d
                if(l[(i,j)]==1):
                    return -1
                j=q+d
                if(l[(2*p-i,j)]==1):
                    return -1
                j=q-d
                if(l[(2*p-i,j)]==1):
                    return -1
            elif(i==p and j!=q):
                j=q+d
                if(l[(i,j)]==1):
                    return -1
                j=q-d
                if(l[(i,j)]==1):
                    return -1
            elif(i!=p and j==q):
                if(l[(i,j)]==1):
                    return -1
                if(l[(2*p-i,j)]==1):
                    return -1
            i+=1
        return r

n = int(raw_input())
l={}
z=[]
for i in xrange(n):
    s = raw_input()
    for j in xrange(n):
        if(s[j]=='*'):
            l[(i+1,j+1)]=1
        elif(s[j]=='.'):
            l[(i+1,j+1)]=0
            z.append((i+1,j+1))

m=-1

for k in z:
    x,y = k
    r=0
    while(ck(l,x,y,n,r)!=-1):
        r+=1
    r-=1
    if(r>m):
        m=r

print m 
