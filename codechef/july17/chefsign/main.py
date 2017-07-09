#!/usr/bin/python2

t = int(raw_input())
for i in xrange(t):
    s = raw_input()
    n = len(s)
    a = []
    i = 0
    l = g = e = 0
    while(i<n):
        if(l):
            if(s[i]=='<'):
                l+=1
            elif(s[i]=='>'):
                a.append(l)
                l = 0
                g = -1
        elif(g):
            if(s[i]=='>'):
                g-=1
            elif(s[i]=='<'):
                a.append(g)
                g = 0
                l = 1
        elif(e):
            pass
        else:
            if(s[i]=='<'):
                l = 1
            elif(s[i]=='>'):
                g = -1
        if(i==n-1):
            if(l):
                a.append(l)
            elif(g):
                a.append(g)
            elif(len(a)==0):
                a.append(0)
        i+=1
    

    mn = mx = cu = 0
    for i in a:
        if(i>0):
            if(cu+i>mx):
                cu+=i
                mx=cu
            else:
                cu=mx
        elif(i<0):
            if(cu+i<mn):
                cu+=i
                mn=cu
            else:
                cu=mn
        #print "cu,mx,mn:",cu,mx,mn

    #print a
    print mx-mn+1
