#!/usr/bin/python2

n,k = map(int, raw_input().split())

a = map(int, raw_input().split())

fg = n
tg = 2*n
og = 0

br = False

for i in xrange(k):
    if(a[i]>0 and fg>0):
        #print "H1"
        q = a[i]/4
        if(q<=fg):
            #print "H2"
            fg-=q
            a[i]-=q*4
        else:
            #print "H3"
            a[i]-=fg*4
            fg=0
    if(a[i]>0 and tg>0):
        #print "H4"
        q = a[i]/2
        if(q<=tg):
            #print "H5"
            tg-=q
            a[i]-=q*2
            #print "tg,a[i]:",tg,a[i]
        else:
            #print "H6"
            a[i]-=tg*2
            tg = 0
    if(a[i]>0 and og>0):
        #print "H7"
        q = a[i]
        if(q<=og):
            #print "H8"
            og-=q
            a[i]-=q
        else:
            #print "H9"
            a[i]-=og
            og = 0
    if(a[i]==0):
        continue
    if(a[i]==1):
        #print "H10"
        if(tg>0):
            #print "H11"
            tg-=1
        elif(fg>0):
            #print "H12"
            fg-=1
            tg+=1
        else:
            #print "H13"
            br = True
            break
    elif(a[i]==2):
        #print "H14"
        if(tg>0):
            #print "H15"
            tg-=1
        elif(fg>0):
            #print "H16"
            fg-=1
            og+=1
        else:
            #print "H17"
            br = True
            break
    elif(a[i]==3):
        #print "H18"
        if(fg>0):
            #print "H19"
            fg-=1
        else:
            #print "H20"
            br = True
            break

if(br):
    #print "H21"
    print 'NO'
else:
    #print "H22"
    print 'YES'
