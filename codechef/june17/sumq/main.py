#!/usr/bin/python2

md = 1000000007

t = int(raw_input())

for i in xrange(t):
    p,q,r = map(int, raw_input().split())
    a = map(int, raw_input().split())
    b = map(int, raw_input().split())
    c = map(int, raw_input().split())
    a.sort()
    b.sort()
    c.sort()
    i = j = k = 0
    sm = 0
    while(j<q):
        i = 0
        while(i<p and a[i]<=b[j]):
            k=0
            while(k<r and c[k]<=b[j]):
                #print "i,j,k:",i,j,k
                #print "a[i],b[j],c[k]:",a[i],b[j],c[k]
                #print "sm before:",sm
                sm+=(a[i]+b[j])*(b[j]+c[k])
                sm%=md
                #print "sm after:",sm
                #print
                #print
                k+=1
            i+=1
        j+=1
    print sm
