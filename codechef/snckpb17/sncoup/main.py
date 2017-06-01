#!/usr/bin/python2

g = {}
g[1] = {}
g[2] = {}

def fn(g):
    ct = 0
    ht = False
    vta1 = False
    vta2 = False
    fl = False
    #vta = False
    l = len(g[1])
    for i in xrange(l):
        if (vta1 and g[1][i+1]==1) or (vta2 and g[2][i+1]==1):
            ct+=1
            fl = True
            if(g[1][i+1]==1):
                vta1 = True
            else:
                vta1 = False
            if(g[2][i+1]==1):
                vta2 = True
            else:
                vta2 = False
            if(g[1][i+1]==1 and g[2][i+1]==1 and not(ht)):
                ct+=1
                ht = True
        else:
            #print "I am here1"
            if not(g[1][i+1]==0 and g[2][i+1]==0):
                #print "I am here2"
                if(fl):
                    #print "I am here also"
                    if not(ht):
                        ct+=1
                        ht = True
                    if(g[1][i+1]==1):
                        vta1 = True
                    if(g[2][i+1]==1):
                        vta2 = True
                else:
                    #print "I am here3"
                    if(g[1][i+1]==1 and g[2][i+1]==1):
                        #print "I am here4"
                        ct+=1
                        ht = True
                    fl = True
                    if(g[1][i+1]==1):
                        #print "I am here5"
                        vta1 = True
                    if(g[2][i+1]==1):
                        #print "I am here6"
                        vta2 = True


    print ct


t = int(raw_input())
for i in xrange(t):
    c = int(raw_input())
    g[1].clear()
    g[2].clear()
    for q in xrange(2):
        s = raw_input()
        sl = len(s)
        for j in xrange(sl):
            if(s[j]=='*'):
                g[q+1][j+1]=1
            else:
                g[q+1][j+1]=0
    #for i in xrange(2):
    #    print g[i+1]
    fn(g)
