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

mc = {}
mc[(n-1,1)] = 0

'''
i = n-2
while(i>-1):
    mc[(i,1)] = msc(i,n-1)
    j = 2
    while(j<=n-i):
        mc[(i,j)] = float("inf")
        k = i+1
        while(k<=n-j+1):
            ck = mc[(k,j-1)] + mcs[k-1] -mcs[i]
            mk = wsm[i]-wsm[k-1]
            x = (al[i]-al[0])
            #mc[(i,j)] = min(mc[(i,j)],mc[(k,j-1)]+mcs[k-1]-(al[i]-al[0])*(wsm[k-1]-wsm[i])-mcs[i])
            mc[(i,j)] = min(mc[(i,j)], mk*x+ck)
            k+=1
        j+=1
    i-=1
'''

def insxn(m1,c1,m2,c2):
    return float(c2-c1)/(m1-m2)

def addl((m,c),e):              # slopes come in decreasing order
    if len(e) == 0:
        e.append((m,c,-float("inf"),float("inf")))
    elif len(e) == 1:
        m1,c1,x1,y1 = e[0]
        if(m1==m):
            if(c>c1):
                e[0] = (m,c,-float("inf"),float("inf"))
        else:
            x = insxn(m,c,me1,c1)
            e[0] = (m1,c1,-float("inf"),x)
            e.append(m,c,x,float("inf"))
    else:
        m1,c1,x1,y1 = e[-1]
        if(m1==m):
            if(c>c1):
                e.pop(-1)
                addl((m,c),e)
        else:
            x = insxn(m,c,m1,c1)
            if(x<=x1):
                e.pop(-1)
                addl((m,c),e)
            else:
                e[-1] = (m1,c1,x1,x)
                e.append(m,c,x,float("inf"))

def hval(x,e,st,en):
    if(en==st+1):
        if(x<=e[st][3]):
            return e[st][0]*x+e[st][1]
        else:
            return e[en][0]*x+e[en][1]
    md = (st+en)/2
    if e[md][2]<=x and x<=e[md][3]:
        return e[md][0]*x+e[md][1]
    elif(x<e[md][2]):
        return hval(x,e,st,md)
    elif(x>e[md][3]):
        return hval(x,e,md,en)

j = 1
i = n-1
while(i>-1):
    mc[(i,j)] = msc(i,n-1)
    print "mc[("+str(i)+","+str(j)+")]: "+str(mc[(i,j)])
    i-=1

j = 2
while(j<=kl):
    i = n-j
    e = []
    while(i>=0):
        k = i+1
        mk = wsm[i]-wsm[k-1]                            # slopes come in descending order
        ck = mc[(k,j-1)] + mcs[k-1] - mcs[i]
        x = (al[i]-al[0])
        addl((mk,ck),e)

        mc[(i,j)] = hval(x,e,0,len(e)-1)
        print "mc[("+str(i)+","+str(j)+")]: "+str(mc[(i,j)])

        # ---------------------------------------------------------------------------------------- #
        #mc[(i,j)] = float("inf")
        #k = i+1
        #while(k<=n-j+1):
        #    ck = mc[(k,j-1)] + mcs[k-1] -mcs[i]
        #    mk = wsm[i]-wsm[k-1]
        #    x = (al[i]-al[0])
        #    #mc[(i,j)] = min(mc[(i,j)],mc[(k,j-1)]+mcs[k-1]-(al[i]-al[0])*(wsm[k-1]-wsm[i])-mcs[i])
        #    mc[(i,j)] = min(mc[(i,j)], mk*x+ck)
        #    k+=1
        # ---------------------------------------------------------------------------------------- #

        i-=1
    j+=1

print mc[(0,kl)]
