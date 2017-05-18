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

while(len(nd)!=0):
    cn = nd.pop(0)
    #vst[cn] = 1
    j = r[cn]#rcr(cn)
    i = 1
    while(i<=j):
        nb = cn+i
        nb%=n
        if not(ds.has_key(nb)):
            ds[nb] = ds[cn] + 1
            nd.append(nb)
        nb = cn-i
        nb%=n
        if not(ds.has_key(nb)):
            ds[nb] = ds[cn] + 1
            nd.append(nb)
        i+=1

if ds.has_key(t):
    print ds[t]
else:
    print -1
