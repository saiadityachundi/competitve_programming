#!/usr/bin/python2

def fui(a,b,st,en,l):
    z=(st+en)/2
    if(z==0):
        if(a[z]!=b[z]):
            return z
    if(z==l-1):
        if(a[z]!=b[z]):
            return z
        else:
            return -1
    else:
        if(a[z]!=b[z]):
            if(a[z-1]==b[z-1]):
                return z
            else:
                return fui(a,b,st,z,l)
        elif(a[z]==b[z]):
            return fui(a,b,z+1,en,l)

def cmp(a,b):
    if(len(a)!=len(b)):
        if(len(a)>len(b)):
            return 1
        if(len(a)<len(b)):
            return -1
    z=fui(a,b,0,len(a)-1,len(a))
#    print "z: ",z
    if(z==-1):
        return 0
#    print "In cmp, the digits are: ",a[z],b[z]
#    print "(a[z])>(b[z]): ", int(a[z])>int(b[z])
#    print "(a[z])<(b[z]): ", int(a[z])<int(b[z])
    if(int(a[z])>int(b[z])):
        return 1
    if(int(a[z])<int(b[z])):
        return -1

def msort(a,st,en):
#    print "st: ",st
#    print "en: ",en
#    print "slice: ",a[st:en+1]
    ln=en-st+1
    z=(st+en)/2
#    print "ln: ",ln
#    print "z: ",z
    if(ln==1):
#        print "b: ",a[st:en+1]
        return a[st:en+1]
    elif(ln==2):
        if(cmp(a[st],a[en])==-1):
#            print "b: ", a[st:en+1]
            return a[st:en+1]
        else:
#            print "b: ", [a[en],a[st]]
            return [a[en],a[st]]
    l=a[st:z+1]
    r=a[z+1:en+1]
#    print "l: ",l
#    print "r: ",r
    nl=msort(a,st,z)
    nr=msort(a,z+1,en)
#    print "nl: ",nl
#    print "nr: ",nr
#    print
    nm=[]
    i=0
    j=0
    ll=len(nl)
    rl=len(nr)
    while(i<ll or j<rl):
        if(i==ll):
            nm.append(nr[j])
            j+=1
        elif(j==rl):
            nm.append(nl[i])
            i+=1
        else:
            if(cmp(nl[i],nr[j])==-1):
                nm.append(nl[i])
                i+=1
            else:
                nm.append(nr[j])
                j+=1
    return nm

n=int(raw_input())
a=[]
for i in xrange(n):
    s=raw_input()
    a.append(s)

b=msort(a,0,n-1)

for i in b:
    print i

#for i in xrange(n):
#    s=raw_input().split()
#    print s[0]
#    print s[1]
#    if(len(s[0])==len(s[1])):
#        f=fui(s[0],s[1],0,len(s[0])-1,len(s[0]))
#        print "f: ",f
#        print "The digits are: ",s[0][f],s[1][f]
#    print "cmp: ",cmp(s[0],s[1])
