#!/bin/python2

from fractions import gcd

import sys

tr={}
gu=[]
p={}
c={}
cnd={}

def cndd(nd):
    if(cnd.has_key(nd)):
        return cnd[nd]
    if(gu.has_key((p[nd],nd))):
        cnd[nd]=cndd(p[nd])-1
    elif(gu.has_key((nd,p[n]))):
        cnd[nd]=cndd(p[nd])+1
    else:
        cnd[nd]=cndd(p[nd])
    return cnd[nd]

q = int(raw_input().strip())
for a0 in xrange(q):
        n = int(raw_input().strip())
        tr={}
        p={}
        c={}
        cnd={}
        for a1 in xrange(n-1):
                u,v = raw_input().strip().split(' ')
                u,v = [int(u),int(v)]
                if not (tr.has_key(u)):
                        tr[u]=[]
                tr[u].append(v)
                if not (tr.has_key(v)):
                        tr[v]=[]
                tr[v].append(u)
        q=[1]
        vst={}
        vst[1]=1
        while len(q)!=0:
            nd=q.pop(0)
            vst[nd]=1
            if(not c.has_key(nd)):
                c[nd]=[]
            for i in tr[nd]:
                if(not vst.has_key(i)):
                    c[nd].append(i)
                    p[i]=nd
                    q.append(i)

        g,k = raw_input().strip().split(' ')
        g,k = [int(g),int(k)]
        gu={}
        for a1 in xrange(g):
                u,v=raw_input().split(' ')
                u,v=[int(u),int(v)]
                gu[(u,v)]=1

        cnt=0

        cnd[1]=0
        for i in gu.keys():
            x,y=i
            if(y!=1 and x==p[y]):
                cnd[1]+=1

        if(cnd[1]>=k):
            cnt+=1

        i=2
        while(i<=n):
            if(cndd(i)>=k):
                cnt+=1
            i+=1

        gc=gcd(cnt,n)
        cnt/=gc
        n/=gc
        print str(cnt)+"/"+str(n)

#        print "xxxxxx"
#        print p
#        print c
#        print cnd
#        print "xxxxxx"
