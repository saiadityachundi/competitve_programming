#!/usr/bin/python2

r = {}
ds = {}
#vst = {}

n,s,t = map(int, raw_input().split())
r[0],g,sd,p = map(int, raw_input().split())

i = 1
while(i<n):
    r[i] = (r[i-1]*g+sd)%p
    i+=1

#def rcr(i):
#    if not(r.has_key(i)):
#        r[i] = (rcr(i-1)*g+sd)%p
#    return r[i]

nd = [s]
ds[s] = 0

#while(len(nd)!=0):
#    cn = nd.pop(0)
#    #vst[cn] = 1
#    j = r[cn]#rcr(cn)
#    i = 1
#    while(i<=j):
#        nb = cn+i
#        nb%=n
#        if not(ds.has_key(nb)):
#            ds[nb] = ds[cn] + 1
#            nd.append(nb)
#        nb = cn-i
#        nb%=n
#        if not(ds.has_key(nb)):
#            ds[nb] = ds[cn] + 1
#            nd.append(nb)
#        i+=1

i = 1
while(i<n):
    ds[i] = float("inf")
    i+=1

ly = 0
ll = lr = rl = rr = s
nll = nlr = nrl = nrr = s
j = 0
br = False
while(True):
    #print "layer ly:",ly
    #print "ll,lr:",ll,lr
    #print "rl,rr:",rl,rr
    nlr = (ll-1)
    nll = ll
    nrl = (rr+1)
    nrr = rr
    i = ll
    while(i<=lr):
        ds[i] = ly
        if ((i+r[i]) >nrr):
            nrr = (i+r[i])
        if ((i-r[i]) <nll):
            nll = (i-r[i])
        j+=1
        if(j==n):
            br = True
            break
        i+=1
    if br:
        break

    i = rl
    while(i<=rr):
        ds[i] = ly
        if ((i+r[i]) >nrr):
            nrr = (i+r[i])
        if ((i-r[i]) <nll):
            nll = (i-r[i])
        j+=1
        if(j==n):
            br = True
            break
        i+=1
    if br:
        break

    #print "nll,nlr:",nll,nlr
    #print "nrl,nrr:",nrl,nrr
    #print
    #print
    nll%=n
    nlr%=n
    nrl%=n
    nrr%=n
    if (nll == ll) and (nrr == rr):
        break

    ll = nll
    lr = nlr
    rl = nrl
    rr = nrr

    ly+=1

#print ds

if ds.has_key(t):
    print ds[t]
else:
    print -1
