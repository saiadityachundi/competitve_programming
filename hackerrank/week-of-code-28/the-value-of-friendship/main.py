#!/usr/bin/python2

n=0
m=0
nn={}
en={}
e={}

def mt():
    v={}
    for i in xrange(m):
        v[i+1]=0
    ne=[]
    mtot=0
    sm=0
    el=[]
    for i in xrange(m):
        el.append(i+1)
    while(len(el)!=0):
        if(len(ne)==0):
            mtot+=sm
            sm=0
            nin=2
            ein=1
            ed=el.pop(0)
            cnl=[e[ed][0],e[ed][1]]
            for i in en[e[ed][0]]:
                if(i in el and (not i in ne)):
                    ne.append(i)
            for i in en[e[ed][1]]:
                if(i in el and (not i in ne)):
                    ne.append(i)
            sm+=2
            mtot+=sm
        else:
            ed=ne.pop(0)
            el.remove(ed)
            for i in en[e[ed][0]]:
                if(i in el and (not i in ne)):
                    ne.append(i)
            for i in en[e[ed][1]]:
                if(i in el and (not i in ne)):
                    ne.append(i)
            x=e[ed][0]
            y=e[ed][1]
            if (not x in cnl):
                cnl.append(x)
                nin+=1
            if(not y in cnl):
                cnl.append(y)
                nin+=1
            ein+=1
            if(ein<=nin-1):
                sm+=2*(nin-1)
            mtot+=sm
    return mtot

q=int(raw_input())

for i in xrange(q):
    s=map(int, raw_input().split())
    n=s[0]
    m=s[1]
    e={}
    nn={}
    en={}
    for i in xrange(m):
        s=map(int, raw_input().split())
        x=s[0]
        y=s[1]
        e[i+1]=(x,y)
        if(not nn.has_key(x)):
            nn[x]=[]
        nn[x].append(y)
        if(not nn.has_key(y)):
            nn[y]=[]
        nn[y].append(x)
        if(not en.has_key(x)):
            en[x]=[]
        en[x].append(i+1)
        if(not en.has_key(y)):
            en[y]=[]
        en[y].append(i+1)
    print mt()
