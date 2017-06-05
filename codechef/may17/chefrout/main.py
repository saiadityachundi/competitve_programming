#!/usr/bin/python2

def chk(s):
    if(len(s)==1):
        return True
    else:
        i = 0
        l = len(s)
        br = False
        while(i<l-1):
            if(s[i]==s[i+1]):
                i+=1
            else:
                if (s[i]=='E' and s[i+1]=='C') or (s[i]=='S' and s[i+1]=='C') or (s[i]=='S' and s[i+1]=='E'):
                    br = True
                    break
                else:
                    i+=1
        if br:
            return False
        else:
            return True

t = int(raw_input())
for i in xrange(t):
    s = raw_input()
    if(chk(s)):
        print "yes"
    else:
        print "no"
