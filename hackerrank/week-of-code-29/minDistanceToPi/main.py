#!/usr/bin/python2

import math

s=raw_input().split()

mn=int(s[0])
mx=int(s[1])

i=mn

mnn=float("inf")
nu=0
de=0

den=mn

while(den<=mx):
    nu1=math.floor(math.pi*den)
    nu2=math.ceil(math.pi*den)
    p1=nu1/den
    p2=nu2/den
    d1=math.pi-p1
    if d1<0:
        d1=-d1
    d2=math.pi-p2
    if d2<0:
        d2=-d2
    if d1<d2 and d1<mnn:
        mnn=d1
        nu=nu1
        de=den
    if d2<d1 and d2<mnn:
        mnn=d2
        nu=nu2
        de=den
#    print den,nu1,nu2,p1,p2,d1,d2
    den+=1

#print 
#print "xxxxxxxxxxxxxxxx"
print str(int(nu))+"/"+str(de)
