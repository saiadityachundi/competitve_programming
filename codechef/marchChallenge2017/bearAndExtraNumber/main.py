#!/usr/bin/python2

t=input()
for i in xrange(t):
    n=input()
    x=map(int, raw_input().split())
#    mn1=mn2=float("inf")
#    mx1=mx2=-float("inf")
    if(x[0]<x[1]):
        mn1=x[0]
        mn2=x[1]
        mx1=x[1]
        mx2=x[0]
    else: 
        mn2=x[0]
        mn1=x[1]
        mx2=x[1]
        mx1=x[0]

    j=2
    while(j<n):
        if(x[j]<=mn1):
            mn2=mn1
            mn1=x[j]
        elif(x[j]<=mn2):
            mn2=x[j]
        if(x[j]>=mx1):
            mx2=mx1
            mx1=x[j]
        elif(x[j]>=mx2):
            mx2=x[j]
        j+=1
#    print mn1,mn2,mx1,mx2
    if(mx1-mn1+1!=n-1):
#        print "I am here!!"
        if (mx1-mn2+1==n-1):
            print mn1
        else:
            print mx1
    else:
        vst={}
#        print "I am in else!!"
        for j in xrange(n):
            if not(x[j]<=mx1 and x[j]>=mn1):
                print x[j]
                break
            else:
                if(vst.has_key(x[j])):
                    print x[j]
                    break
                else:
                    vst[x[j]]=1
