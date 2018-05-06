#!/usr/bin/python2

global a
a=map(int,raw_input().split())

def mscore(i):
    global a
    #b=a
    b=a[:]
    n=b[i]
    b[i]=0
    q=n/14
    r=n%14
    for j in xrange(14):
        b[j]+=q
    for j in xrange(r):
        j+=1
        b[(i+j)%14]+=1
    sc=0
    for j in xrange(14):
        if b[j]%2==0:
            sc+=b[j]
    return sc

mx=-float('inf')
for i in xrange(14):
    #print a
    sc=mscore(i)
    if sc>mx:
        mx=sc

print mx
