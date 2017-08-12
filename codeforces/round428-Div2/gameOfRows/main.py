#!/usr/bin/python2

n,k = map(int, raw_input().split())

a = map(int, raw_input().split())

fg = n
tg = 2*n
og = 0

#print fg,tg

br = False

for i in xrange(k):
    if(fg<=0 and tg<=0):
        print 'NO'
        br = True
        break
    else:
        if(fg<=0):
            r = a[i]%2
            q = (a[i]-r)/2
            if(r==1):
                q+=1
            if(q<=tg):
                tg-=q
            else:
                print 'NO'
                br = True
                break
        elif(tg<=0):
            r = a[i]%4
            q = (a[i]-r)/4
            if(r>0):
                q+=1
            if(q<=fg):
                fg-=q
            else:
                print 'NO'
                br = True
                break
        else:
            r = a[i]%4
            q = (a[i]-r)/4
            #print "r,q:",r,q
            #print "fg,tg:",fg,tg
            #print "--------"
            if(q<=fg):
                #print "I am in if"
                fg-=q
            else:
                #print "I am in else"
                #print "fg,tg:",fg,tg
                q-=fg
                fg=0
                q*=2
                if(q<=tg):
                    #print "I am in 2if"
                    tg-=q
                else:
                    #print "I am in 2else"
                    print 'NO'
                    br = True
                    break
            if(r!=0):
                if(fg<=0 and tg<=0):
                    print 'NO'
                    br = True
                    break
                elif(fg<=0):
                    #q = r
                    #r = a[i]%2
                    if(r==0):
                        r = 0
                    elif(r<=2):
                        r = 1
                    else:
                        r = 2
                    if(r<=tg):
                        tg-=r
                    else:
                        print "NO"
                        br = True
                        break
                elif(tg<=0):
                    if(r==0):
                        r = 0
                    else:
                        r = 1
                    fg-=r
                else:
                    if(r==0):
                        pass
                    elif(r<=2):
                        tg-=1
                    else:
                        fg-=1
    #print fg,tg

#print fg,tg
if(not br):
    print 'YES'

