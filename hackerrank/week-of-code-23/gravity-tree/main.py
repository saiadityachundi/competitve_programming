#!/usr/bin/python2

import math

p={}
c={}
can={}
di={}

n=int(raw_input())
s=raw_input().split(' ')

ch=0

for i in xrange(n):
    c[i+1]=[]

for i in xrange(n-1):
    ch=int(s[i])
    p[i+2]=ch
    c[ch].append(i+2)

def chan(m,n):                      # Check if m is an ancestor of n
    if(m==1):
        return True
    else:
        ct=n
        while(ct!=1):
            if(ct==m):
                return True
            ct=p[ct]
        return False

def anc(m,n): 
    if(can.has_key(m) and can[m].has_key(n)):
        return can[m][n]
    else:
        
        if(not can.has_key(m)):
            can[m]={}
        if(not can.has_key(n)):
            can[n]={}
 
        if(m==n):
            can[m][n]=m

        elif(chan(m,n)):
            can[m][n]=m
            can[n][m]=m
        
        elif(chan(n,m)):
            can[m][n]=n
            can[n][m]=n
 
        else:
            can[m][n]=anc(p[m],p[n])
            can[n][m]=can[m][n]
        return can[m][n]

def dis(m,n):
    if(di.has_key(m) and di[m].has_key(n)):
        return di[m][n]
    else:
        if(not di.has_key(m)):
            di[m]={}
        if(not di.has_key(n)):
            di[n]={}
        if(m==n):
            di[m][m]=0
        else:
            a=anc(m,n)
            if(m==a or n==a):
                if(m==a):
                    ct=n
                else:
                    ct=m
                cn=0
                while(ct!=a):
                    cn+=1
                    ct=p[ct]
                di[m][n]=cn
                di[n][m]=cn
            else:
                di[m][n]=dis(m,a)+dis(a,n)
                di[n][m]=di[m][n]
        return di[m][n]

at={}

def atr(u,v):
    if(at.has_key(u) and at[u].has_key(v)):
        return at[u][v]
    else:
        if(not at.has_key(u)):
            at[u]={}
        fo=0
        fo+=(dis(u,v)**2)
        for i in c[v]:
            fo+=atr(u,i)
        at[u][v]=fo
        return at[u][v]


q=int(raw_input())

for i in xrange(q):
    s=raw_input().split()
    u=int(s[0])
    v=int(s[1])
    print atr(u,v)
