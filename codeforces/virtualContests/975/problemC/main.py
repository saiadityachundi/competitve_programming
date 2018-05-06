#!/usr/bin/python2

n,q=map(int,raw_input().split())
a=map(int,raw_input().split())
k=map(int,raw_input().split())

s=0
for i in a:
    s+=i

ac=a[:]
sc=s
for i in xrange(q):
    kc=k[i]
    if kc>=sc:
        ac=a[:]
        sc=s
        print n
    else:
        for j in xrange(n):
            if ac[j]-kc<0:
                kc-=ac[j]
                sc-=ac[j]
                ac[j]=0
                if j==n-1:
                    print n
                    ac=a[:]
                    sc=s
            else:
                ac[j]-=kc
                sc-=kc
                kc=0
                if ac[j]==0:
                    print n-j-1
                    break
                else:
                    print n-j
                    break
        #print "i:",i
        #print ac
        #print "sc:",sc
        #print "kc:",kc
        #sm=0
        #for j in xrange(n):
        #    if ac[j]>0:
        #        sm+=1
        #if sm==0:
        #    ac=a[:]
        #    sc=n
        #    sm=n
        #print sm
