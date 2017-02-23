#!/usr/bin/python2

import math

x1=x2=x3=x4=y1=y2=y3=y4=xs=ys=xc=yc=r=h=w=m1=m2=m3=m4=c1=c2=c3=c4=k1=k2=k3=k4=0

def insideSquare(x,y):
    if(x1==x2 and y1==y2):
        if(x==x1 and y==y1):
            return True
        else:
            return False
    if(m1==0):
        if ((ys-c1)*(y-c1)>=0) and ((xs-k2)*(x-k2)>=0) and ((ys-c3)*(y-c3)>=0) and ((xs-k4)*(x-k4)>=0):
            return True
        else:
            return False
    if(m2==0):
        if ((xs-k1)*(x-k1)>=0) and ((ys-c2)*(y-c2)>=0) and ((xs-k3)*(x-k3)>=0) and ((ys-c4)*(y-c4)>=0):
            return True
        else:
            return False
    if ( (ys-(m1*xs)-c1)*(y-(m1*x)-c1)>=0 ) and ( (ys-(m2*xs)-c2)*(y-(m2*x)-c2)>=0 ) and ( (ys-(m3*xs)-c3)*(y-(m3*x)-c3)>=0 ) and ( (ys-(m4*xs)-c4)*(y-(m4*x)-c4)>=0 ):
        return True
    else:
        return False

def insideCircle(x,y):
    if(math.sqrt(((x-xc)**2)+((y-yc)**2))<=r):
        return True
    else:
        return False

s=raw_input().split()
w=float(s[0])
h=float(s[1])
s=raw_input().split()
xc=float(s[0])
yc=float(s[1])
r=float(s[2])
s=raw_input().split()
x1=float(s[0])
y1=float(s[1])
x3=float(s[2])
y3=float(s[3])

xs=(x1+x3)/2
ys=(y1+y3)/2

if(x1!=x3):
    m=(y1-y3)/(x1-x3)
    t1=math.sqrt((((y1-ys)**2)+((x1-xs)**2))/((m**2)+1))
    t2=m*t1
else:
    t1=0
    t2=math.sqrt(((y1-ys)**2)+((x1-xs)**2))

x2=xs-t2
y2=ys+t1

x4=xs+t2
y4=ys-t1

#print "vertices of square are: ",(x1,y1),(x2,y2),(x3,y3),(x4,y4)
#print "centre of the square is: ", (xs,ys)

if(x1==x2):
    k1=x1
    m1=float("inf")
else:
    m1=(y2-y1)/(x2-x1)
    c1=(y2-m1*x2)
if(x2==x3):
    k2=x2
    m2=float("inf")
else:
    m2=(y3-y2)/(x3-x2)
    c2=(y3-m2*x3)
if(x3==x4):
    k3=x3
    m3=float("inf")
else:
    m3=(y4-y3)/(x4-x3)
    c3=(y4-m3*x4)
if(x1==x4):
    k4=x4
    m4=float("inf")
else:
    m4=(y1-y4)/(x1-x4)
    c4=(y1-m4*x1)

#print "slopes are: ", m1, m2, m3, m4
#print "k's are: ", k1,k2,k3,k4
#print "c's are: ", c1,c2,c3,c4

for y in xrange(int(h)):
    s=""
    for x in xrange(int(w)):
        if(insideSquare(x,y)):
#            print (x,y),"is inside square"
            s+="#"
        elif(insideCircle(x,y)):
#            print (x,y),"is inside circle"
            s+="#"
        else:
#            print (x,y),"is neither inside square nor insdie circle"
            s+="."
    print s
