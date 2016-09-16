#!/usr/bin/python2

import math

def chk(s, j):
    l = j
    isBreak = False
    for i in xrange(j):
        if(s[i]!=s[j+i]):
            isBreak = True
            break
    if(isBreak):
        return False
    else:
        return True

def div(n):
    l = []
    for i in xrange(int(math.sqrt(n))):
        if(n%(i+1)==0):
            l.append(i+1)
            if(i+1!=math.sqrt(n)):
                l.append(n/(i+1))
    l.sort()
    return l

def func(s, m):
    l = len(s)
    d = div(l)
    for i in d:
        if(i<=(l/2)):
           ind = i
           if(chk(s,i)):
               break
    rl = i
    return int(m/rl)

s=raw_input()
n=int(raw_input())
print func(s,n)
