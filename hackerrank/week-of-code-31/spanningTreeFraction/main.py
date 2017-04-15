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
    j+=1

#print "ed:",ed
#print "enb:",enb
#print "----------"
#print

uvst = {}
for i in xrange(n-1):
    uvst[i+1] = 1

q = {}
for i in enb[0]:
    q[i] = 1

#print "uvst:",uvst
#print "q:",q
#print "enb[0]:",enb[0]
#print "----------"
#print

def fn(uvst,q,nm,dm):
    if(len(uvst)==0):
        #print "uvst:",uvst
        #print "q:",q
        #print "returning (nm,dm):", (nm,dm)
        #print
        return (nm,dm)
    mnm = nm
    mdm = dm
    fr = -float("inf")
    for i in q.keys():
        tuvst = {}
        for j in uvst.keys():
            tuvst[j] = 1
        tq = {}
        for j in q.keys():
            tq[j] = 1
        if(uvst.has_key(ed[i][0])):
            for j in enb[ed[i][0]]:
                if (tuvst.has_key(ed[j][0])) or (tuvst.has_key(ed[j][1])):
                    tq[j] = 1
            tuvst.pop(ed[i][0],None)
            tq.pop(i,None)
            tnm, tdm = fn(tuvst, tq, nm+ed[i][2], dm+ed[i][3])
            if(float(tnm)/(tdm)>fr):
                mnm = tnm
                mdm = tdm
                fr = float(mnm)/mdm

        elif(uvst.has_key(ed[i][1])):
            for j in enb[ed[i][1]]:
                if (tuvst.has_key(ed[j][0])) or (tuvst.has_key(ed[j][1])):
                    tq[j] = 1
            tuvst.pop(ed[i][1],None)
            tq.pop(i,None)
            tnm, tdm = fn(tuvst, tq, nm+ed[i][2], dm+ed[i][3])
            if(float(tnm)/(tdm)>fr):
                mnm = tnm
                mdm = tdm
                fr = float(mnm)/mdm
    #print "uvst:",uvst
    #print "q:", q
    #print "nm,dm:",nm,dm
    #print "mnm,mdm:",mnm,mdm
    #print
    return (mnm,mdm)

nm,dm = fn(uvst,q,0,0)
print str(nm)+"/"+str(dm)
