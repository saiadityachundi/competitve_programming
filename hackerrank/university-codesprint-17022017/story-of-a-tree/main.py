#!/usr/bin/python2

from fractions import gcd

t=int(raw_input())
for t0 in xrange(t):
    tr={}
    p={}
    c={}
    n=int(raw_input())
    for t1 in xrange(n-1):
        s=map(int, raw_input().split())
        if not(tr.has_key(s[0])):
            tr[s[0]]=[]
        if not(tr.has_key(s[1])):
            tr[s[1]]=[]
        tr[s[0]].append(s[1])
        tr[s[1]].append(s[0])
    q=[1]
    vst={}
    while(len(q)!=0):
        nd=q.pop(0)
        vst[nd]=1
        for nb in tr[nd]:
            if not(vst.has_key(nb)):
                q.append(nb)
                p[nb]=nd

    s=map(int, raw_input().split())
    g=s[0]
    k=s[1]
    gu={}
    for t2 in xrange(g):
        s=map(int, raw_input().split())
        if(gu.has_key((s[1],s[0]))):
            k-=1
            del gu[(s[1],s[0])]
        else:
            gu[(s[0],s[1])]=1

    cnd={}

    cnd[1]=0

    for ge in gu.keys():
        x,y=ge
        if(y!=1):
            if(p[y]==x):
                cnd[1]+=1

    q=[1]
    vst={}
    while(len(q)!=0):
        nd=q.pop(0)
        vst[nd]=1
        if(nd!=1):
            if(gu.has_key((p[nd],nd))):
                cnd[nd]=cnd[p[nd]]-1
            elif(gu.has_key((nd,p[nd]))):
                cnd[nd]=cnd[p[nd]]+1
            else:
                cnd[nd]=cnd[p[nd]]
 
        for nb in tr[nd]:
            if not(vst.has_key(nb)):
                q.append(nb)

    cnt=0
    for i in xrange(n):
        if(cnd[i+1]>=k):
            cnt+=1

    gc=gcd(cnt,n)
    cnt/=gc
    n/=gc
    print str(cnt)+"/"+str(n)
