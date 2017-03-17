#!/usr/bin/python2

n,k = map(int, raw_input().split())
al=[]
wt=[]

for i in xrange(n):
    a,w = map(int, raw_input().split())
    al.append(a)
    wt.append(w)

'''
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
'''

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
'''
print al
print wt

i=0
while(i<n):
    j=i+1
    while(j<n):
        print "i:"+str(i)+" j:"+str(j)+" "+str(mcs[j]-((al[i]-al[0])*(wsm[j]-wsm[i]))-mcs[i])
        j+=1
    i+=1

for i in xrange(n):
    print wsm[i]
'''

mpp={}

def mc(ind, k):
    if(mpp.has_key((ind,k))):
        return mpp[(ind,k)]
    if(ind+k>n):
        mpp[(ind,k)]=float("inf")
        return float("inf")
    if(k==1):
        mpp[(ind,k)]=float("inf")
        return msc(ind, n-1)
    if(k==0):
        mpp[(ind,k)]=0
        return 0
    mcp={}
    i=ind+1
    #mn=float("inf")
    while(i<n):
        mcp[i]=mc(i,k-1)+msc(ind,i-1)
        i+=1
    mn=float("inf")
    ind1 = -1
    for j in mcp.keys():
        if(mcp[j]<mn):
            mn = mcp[j]
            ind1=j
    #print "ind1:"+str(ind1)+" k:"+str(k-1)+" mn:"+str(mn)
    mpp[(ind,k)]=mn
    return mn

print mc(0,k)
'''
print mc(0,2)
print msc(0,1)
print mc(2,1)
print msc(2,5)
'''
