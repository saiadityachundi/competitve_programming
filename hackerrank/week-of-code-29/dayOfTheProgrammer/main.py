#!/bin/python2

import sys

def isJulian(n):
        if(n<1918):
                return True
        else:
                return False
        
def isGregorian(n):
        if(n>1918):
                return True
        else:
                return False
        
def isLeap(n):
        if(isGregorian):
                if(n%400==0):
                        return True
                if(n%4==0 and n%100!=0):
                        return True
                return False
        if(isJulian):
                if(n%4==0):
                        return True
                else:
                        return False

y = int(raw_input().strip())
if(isGregorian(y)):
        if(isLeap(y)):
                d=str(12)
        else:
                d=str(13)
elif(isJulian(y)):
        if(isLeap(y)):
                d=str(12)
        else:
                d=str(13)
else:
        d=str(29)
        
print d+'.09.'+str(y)
