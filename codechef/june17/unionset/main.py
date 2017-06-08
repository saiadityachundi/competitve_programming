#!/usr/bin/python2

t = int(raw_input())
for i in xrange(t):
    n,k = map(int, raw_input().split())
    s={}
    c={}
    for i in xrange(n):
        c[i+1] = {}
        for j in xrange(k):
            c[i+1][j+1]=1
        sl = map(int, raw_input().split())
        sl.pop(0)
        s[i+1]={}
        for j in sl:
            s[i+1][j]=1
            if c[i+1].has_key(j):
                del c[i+1][j]

    ct = 0
    i = 1
    while(i<=n):
        j=i+1
        while(j<=n):
            br =False
            for p in c[i].keys():
                if not(s[j].has_key(p)):
                    br = True
                    break
            if not br:
                ct+=1
            j+=1
        i+=1
    print ct
