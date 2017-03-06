#!/usr/bin/python2

from fractions import gcd

def nsq(r,c):
    if(r>c):
        t=c
        c=r
        r=t
    return (((r-1)*r*c)+((r*(r-1)*(2*r-1))/6)-(((r+c)*(r)*(r-1))/2))

t=input()

for i in xrange(t):
    cnt=0
    s=map(int, raw_input().split())
    r=s[0]
    c=s[1]
    #if(r>c):
    #    t=c
    #    c=r
    #    r=t
#    cnt+=nsq(r,c)
#    #print "first cnt:",cnt
#    i=2
#    while(i<=r):
#        j=2
#        while(j<=c):
#            l=i-1
#            m=j-1
#            g=gcd(l,m)
#            x=g+1
#            l=(r-i)/((j-1)/g)
#            m=(c-j)/((i-1)/g)
#            l+=1
#            m+=1
#            if(l<m):
#                y=l
#            else:
#                y=m
#            s=nsq(x,y)
#            cnt+=s
#            #print "i,j:",i,j
#            #print "g:",g
#            #print "l,m:",l,m
#            #print "x,y:",x,y
#            #print "s:",s
#            #print "cnt: ",cnt
#            j+=1
#        i+=1
    for l in xrange(c):
        for d in xrange(r):
            if not(l==0 or d==0):
                #print "l,d:",l,d
                x=0
                y=0
                if(r-(l+d)>=0):
                    y=r-(l+d)
                if(c-d>=l+1):
                    x=c-d-l
                cnt+=x*y
                #print "cnt:",cnt

    cnt+=nsq(r,c)
    
    print "Case #"+str(i+1)+": "+str(cnt%((10**9)+7))
