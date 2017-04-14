#!/usr/bin/python2

n,m = map(int, raw_input().split())
ed={}
enb={}
j = 1
for i in xrange(m):
    x,y,a,b = map(int, raw_input().split())
    if(x!=y):
        ed[j] = (x,y,a,b)
        if(not enb.has_key(x)):
            enb[x]=[]
        enb[x].append(j)
        if(not enb.has_key(y)):
            enb[y]=[]
        enb[y].append(j)

vst={}
vst[0]=1
q = {}
for i in xrange(n):
    q[i] = 1
el={}
for i in enb[0]:
    el.append(i)
nm = 0
dm = 0
while(len(q)!=0):
    mst = -float("inf")
    nd = -1
    for i in el.keys():
        t = float(nm+(ed[i][3]))/(dm+(ed[i][4]))
        if(t>mst):
            if(not vst.has_key(ed[i][0])):
                mst = t
                nd = ed[i][0]
                ce = i
            if(not vst.has_key(ed[i][1])):
                mst = t
                nd = ed[i][1]
                ce = i
    vst[nd] = 1
    nm+=(ed[ce][2])
    dm+=(ed[ce][3])

    for i in enb[nd]:
        if(not el.has_key(i)):
            el[i] = 1

    el.pop(i,None)
    q.pop(nd,None)

print str(nm)+"/"+str(dm)
