#!/usr/bin/python2

n,kl = map(int, raw_input().split())
al=[]
wt=[]

for i in xrange(n):
    a,w = map(int, raw_input().split())
    al.append(a)
    wt.append(w)

wsm=[]
wsm.append(wt[0])
i=1
while(i<n):
    wsm.append(wsm[i-1]+wt[i])
    i+=1

mcs=[]
mcs.append(0)
i=1
while(i<n):
    mcs.append(mcs[i-1]+wt[i]*(al[i]-al[0]))
    i+=1

def msc(i,j):               # j>i. move ind_j to ind_i
    return (mcs[j]-((al[i]-al[0])*(wsm[j]-wsm[i]))-mcs[i])

#pr=[]
#pr.append(0)

mp={}

#------------------------------------

mc = {}
mc[(n-1,1)] = 0


i = n-2
while(i>-1):
    mc[(i,1)] = msc(i,n-1)
    j = 2
    while(j<=n-i):
        mc[(i,j)] = float("inf")
        k = i+1
        while(k<=n-j+1):
            mc[(i,j)] = min(mc[(i,j)],mc[(k,j-1)]+msc(i,k-1))
            k+=1
        j+=1
    i-=1

#------------------------------------

    '''
def mc(ind, k):
    if(mp.has_key((ind,k))):
        return mp[(ind,k)]
    if(ind+1<k):
        mp[(ind,k)]=(ind,float("inf"))
        return mp[(ind,k)]
    if(ind+1 == k):
        mp[(ind,k)]=(ind,0)
        return mp[(ind,k)]
    if(k==1):
        if(ind>-1):
            mp[(ind,k)]=(0,0)
            return mp[(ind,k)]
        else:
            mp[(ind,k)]=(0,float("inf"))
            return mp[(ind,k)]
    '''

    '''
    if(ind==n-1):
        if(k==1):
            mp[(ind,k)]=(n-1,0)
            return mp[(ind,k)]
        else:
            mp[(ind,k)]=(n,float("inf"))
            return mp[(ind,k)]
    '''

    '''
    if(ind==0):
        if(k==1):
            mp[(ind,k)]=(0,0)
            return mp[(ind,k)]

    ns1,m1 = mc(ind-1,k-1)
    ns2,m2 = mc(ind-1,k)
    m3 = m1+msc(ns1,ind-1)
    m4 = m2+msc(ns2,ind)
    if(m3<m4):
        mp[(ind,k)]=(ind,m3)
    else:
        mp[(ind,k)]=(ns2,m2)
    return mp[(ind,k)]
    '''

    '''
    prt=pr[0]
    pr[0]=ind
    ns1,m1=mc(ind+1,k-1)
    pr[0]=prt
    ns2,m2=mc(ind+1,k)
    m3=m1+msc(pr[0],ind-1)+msc(ind,ns1-1)
    m4=m2+msc(pr[0],ns2-1)

    if(m3<m4):
        mp[(ind,k)]=(ind,m1+msc(ind,ns1-1))
        return mp[(ind,k)]
    else:
        mp[(ind,k)]=(ns2,m2)
        return mp[(ind,k)]
    '''

'''
for i in xrange(n):
    print "i,j:",i,i,msc(i,i)
'''

#x,y = mc(n-1,k)
#print y+msc(x,n-1)

#for i in xrange(n):
#    print msc(0,i)

print mc[(0,kl)]
