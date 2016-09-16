#!/usr/bin/python2

import math

p={}
c={}
an={}
can={}
di={}

n=int(raw_input())
s=raw_input().split(' ')

an[1]=[1]
ch=0

for i in xrange(n):
    c[i+1]=[]

for i in xrange(n-1):
    ch=int(s[i])
    p[i+2]=ch
    c[ch].append(i+2)

qu=[1]

while(len(qu)!=0):
    cur=qu.pop(0)
    if(len(c[cur])!=0):
        qu.extend(c[cur])
    if(cur==1):
        an[cur]=[1]
    else:
        an[cur]=[]
        an[cur].append(cur)
        an[cur].extend(an[p[cur]])

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
        elif(m in an[n]):
            can[m][n]=m
            can[n][m]=m
        elif(n in an[m]):
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
