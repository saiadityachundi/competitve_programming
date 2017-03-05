#!/usr/bin/python2

t=input()

for i in xrange(t):
    e1=e2=o1=o2=0
    n=input()
    x=map(int, raw_input().split())
    for j in xrange(n):
        if((j+1)%2==0):
            o1+=x[j]
        else:
            e1+=x[j]
    x=map(int, raw_input().split())
    for j in xrange(n):
        if((j+1)%2==0):
            o2+=x[j]
        else:
            e2+=x[j]

    if(e1+o2<e2+o1):
        print e1+o2
    else:
        print e2+o1
