#!/usr/bin/python2

import sys
sys.setrecursionlimit(1000)

mod=1000000007

f={}
f[1]=1
f[2]=2

def func(n):
    if(f.has_key(n)):
        return f[n]
    else:
        f[n]=((func(n-1)%mod)+((n-1)%mod)*(func(n-2)%mod))%mod
        return func(n)

t=long(raw_input())
for i in xrange(t):
    n=long(raw_input())
    print func(n)
