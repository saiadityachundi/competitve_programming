#!/usr/bin/python2

def red2root(w):
    d={}
    for i in w:
        if not d.has_key(i):
            d[i]=1
    r=d.keys()
    r.sort()
    return r

n=int(raw_input())
w=raw_input().split()
rts=[]
for i in xrange(n):
    rt=red2root(w[i])
    b=True
    for j in rts:
        if j==rt:
            b=False
    if b:
        rts.append(rt)

#print rts

#ct=0
#i=0
#n=len(rts)
#while(i<n):
#    j=i+1
#    while(j<n):
#        if rts[i]!=rts[j]:
#            ct+=1
#        j+=1
#    i+=1
#
#print ct+1

print len(rts)
