#!/usr/bin/python2

n,k = map(int, raw_input().split())
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

def msc(i,j):
    return (mcs[j]-((al[i]-al[0])*(wsm[j]-wsm[i]))-mcs[i])

pr=[]
pr.append(0)

mpp={}

def mc(i,k):
    #if(mpp.has_key((i,k))):
    #    return mpp[(i,k)]
    if(i==n-1):
        if(k==1):
            #mpp[(i,k)]=(n-1,0)
            return (n-1,0)
        else:
            #mpp[(i,k)]=(n-1,float("inf"))
            return (n-1,float("inf"))
    if(k==0):
        #mpp[(i,k)]=(n,0)
        return (n,0)
    if(i==0):
        #mpp[(i,k)]=y+msc(0,x-1)
        x,y = mc(1,k-1)
        return (0,y+msc(0,x-1))
    if(i+k>n):
        #mpp[(i,k)]=(n,float("inf"))
        return (n,float("inf"))
    prt = pr[0]
    pr[0] = i
    ns1,m1 = mc(i+1, k-1)
    pr[0] = prt
    ns2,m2 = mc(i+1, k)
    m3 = m1+msc(i,ns1-1)+msc(i-1,pr[0])
    m4 = m2+msc(pr[0],ns2-1)
    if(m3<m4):
        #print "i,k: ",i,k,(i,m1+msc(i,ns1-1))
        #mpp[(i,k)]=(i,m1+msc(i,ns1-1))
        return (i,m1+msc(i,ns1-1))
    else:
        #print "i,k: ",i,k,(ns2,m2)
        #mpp[(i,k)]=(ns2,m2)
        return (ns2,m2)

'''
for i in xrange(n):
    print "i,j:",i,i,msc(i,i)
'''
x,y = mc(0,k)
print y
