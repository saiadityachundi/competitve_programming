#!/usr/bin/python2

t = int(raw_input())
for i in xrange(t):
    n = int(raw_input())
    if(n==1):
        print 1
    elif(n==2):
        print 1,2
    else:
        d=[]
        for i in xrange(498):
            d.append(i+3)
        a = [1,2]
        i = 1
        while(i<=n-2):
            c = d.pop(0)
            br = False
            for p in a:
                for q in a:
                    if(p!=q):
                        if(c==p+q):
                            br = True
                            break
                if br:
                    break
            if not(br):
                a.append(c)
                i+=1
        for i in a:
            print i,
