#!/usr/bin/python2

a = int(raw_input())
b = int(raw_input())

xr = -float("inf")

i = a
while(i<b):
        j = i+1
        while(j<=b):
                if i^j > xr:
                        xr = i^j
                j+=1
        i+=1
        
print xr
