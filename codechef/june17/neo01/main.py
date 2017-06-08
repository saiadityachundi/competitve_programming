#!/usr/bin/python2

t = int(raw_input())
for i in xrange(t):
    n = int(raw_input())
    a = map(int, raw_input().split())
    nn = []
    ng = []
    for i in a:
        if(i>=0):
            nn.append(i)
        else:
            ng.append(i)
    ng.sort(reverse=True)
    nb = len(nn)
    s = 0
    for i in nn:
        s+=i
    s2 = 0
    for i in ng:
        if(s>nb*(-i)):
            nb+=1
            s+=i
        else:
            s2+=i
    print nb*s+s2
