#!/usr/bin/python

def isSet(a, su):
    l=len(a)
    for i in xrange(l):
        if(a[i]==su):
            return True
        if(isSet(a[:i]+a[i+1:],su-a[i])):
            return True
    return False

t=int(raw_input())

for i in xrange(t):
    a=map(int, raw_input().split())
    if(isSet(a,0)):
        print 'Yes'
    else:
        print 'No'
    print
