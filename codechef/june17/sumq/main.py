#!/usr/bin/python2
md = 1000000007

def ind(st,en,a,x):
    if(en==st):
        if(st==0):
            if(a[st]<=x):
                return 0
            else:
                return -1
        else:
            return st
    if(en==st+1):
        if(a[st]>x):
            return st-1
        elif(a[en]<=x):
            return en
        else:
            return st
    md = (st+en)/2
    if a[md]>x:
        return ind(st,md-1,a,x)
    else:
        return ind(md,en,a,x)

t = int(raw_input())
for i in xrange(t):
    sm=0
    p,q,r = map(int, raw_input().split())
    a = map(int,raw_input().split())
    b = map(int,raw_input().split())
    c = map(int,raw_input().split())
    a.sort()
    b.sort()
    c.sort()
    sa = [a[0]]
    i = 1
    while(i<p):
        sa.append(sa[i-1]+a[i])
        i+=1
    sc = [c[0]]
    k = 1
    while(k<r):
        sc.append(sc[k-1]+c[k])
        k+=1
    for j in xrange(q):
        i = ind(0,p-1,a,b[j])
        k = ind(0,r-1,c,b[j])
        if not(i==-1 or k==-1):
            #sm+=(((b[j]**2)*(i+1)*(k+1))%md +((b[j])*((sa[i]*(k+1))+(sc[k]*(i+1))))%md +(sa[i]*sc[k])%md)%md
            sm+=(b[j]*(i+1)+sa[i])*(b[j]*(k+1)+sc[k])
    print sm%md
