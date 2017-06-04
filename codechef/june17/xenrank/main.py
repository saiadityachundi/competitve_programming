#!/usr/bin/python2

t = int(raw_input())
for i in xrange(t):
    u,v = map(int, raw_input().split())
    print (u+v)*(u+v+1)/2 + (u+1)
