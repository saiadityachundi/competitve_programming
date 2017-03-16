#!/usr/bin/python2

n,k = map(int, raw_input().split())
al=[]
wt=[]

for i in xrange(n):
    a,w = map(int, raw_input().split())
    al.append(a)
    wt.append(w)

al.reverse()
wt.reverse()

def mc(pr, cu, k):
    if(k==0):
        if(cu<n):
            return float("inf")
        else:
        #print "I am returning zero"
            return 0
    if(cu==n):
        #print "I am returning inf"
        return float("inf")
    m1 = mc(pr, cu+1, k)
    i=pr
    cs=0
    while(i<=cu):
        cs+=wt[i]*(al[i]-al[cu])
        i+=1
    m2 = mc(cu+1, cu+1, k-1)+cs
    #print "n:",n
    #print "pr:", pr
    #print "cu:", cu
    #print "k:", k
    #print "m1:",m1
    #print "cs:",cs
    #print "m2:",m2
    #print
    #print
    if(m1<m2):
        #print "I am returning m1"
        return m1
    else:
        #print "I am returning m2"
        return m2

print mc(0, 0, k)
