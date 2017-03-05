#!/usr/bin/python2

n=0

def knum(k):
    if(1+k>n):
        return n*n
    else:
        d=n-(1+k)
        return (n*n-((d)*(d+1)))


t=input()
for i in xrange(t):
    cnt=0
    n=input()
    r={}
    for j in xrange(n):
        r[j]=map(int, raw_input().split())
    #kmx=-float("inf")
    #for j in xrange(n):
    #    kinf=0
    #    while(kinf<n/2 and r[j][kinf]==0):
    #        kinf+=1
    #    df=j-kinf
    #    if df<0:
    #        df=-df
    #    if(kinf==n/2):
    #        df=0
    #    kinb=n-1
    #    while(kinb>n/2-1 and r[j][kinb]==0):
    #        kinb-=1
    #    db=j-kinb
    #    if db<0:
    #        db=-db
    #    if(kinb==n/2-1):
    #        db=0
    #    if(df>db):
    #        k=df
    #    else:
    #        k=db
    #    if(k>kmx):
    #        kmx=k
    #print kmx
    for j in xrange(n):
        for k in xrange(n):
            if(r[j][k]!=0):
                cnt+=1

    k=0
    while(1):
        if(cnt<=knum(k)):
            print k
            break
        k+=1
