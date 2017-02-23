#!/usr/bin/python2

import math

s=raw_input().split()

f=int(s[0])
l=int(s[1])

'''
n=l

pr1={}
pr={}
i=1
while(i*i<=n):
    pr1[i]=True
    i+=1

del pr1[1]

i=2
while(i*i<=math.sqrt(n)):
    if(pr1.has_key(i)):
        j=i*i
        while(j<=math.sqrt(n)):
            if(pr1.has_key(j)):
                del pr1[j]
            j+=i
    i+=1

#print pr1

i=f
while(i<=l):
    pr[i]=True
    i+=1

#print pr

i=2
while(i*i<=n):
#    print "i:",i
    if(pr1.has_key(i)):
        r=f%i
        if(r==0):
            j=f
        else:
            j=f+i-r
        while(j<=n):
#            print "j:",j
            if(pr.has_key(j) and j>=i*i):
#                print "del",j
                del pr[j]
            j+=i
    i+=1

#print pr

'''

def nxt(a):
    a=str(a)
    a=list(a)
    l=len(a)
    i=l-1
    #print "a: ",a
    while(i>=0 and a[i]=='7'):
        i-=1
    #print "i: ",i
    if(i!=-1):
        if(a[i]=='2'):
            a[i]='3'
        elif(a[i]=='3'):
            a[i]='5'
        elif(a[i]=='5'):
            a[i]='7'
    #    print "a[i]:",a[i]
        i+=1
    #    print "i:",i
        while(i<l):
            a[i]='2'
            i+=1
    else:
        a=[]
        for i in xrange(l+1):
            a.append('2')
    l=len(a)
    if(l!=1 and a[l-1]=='2'):
        a[l-1]='3'
    if(l!=1 and a[l-1]=='5'):
        a[l-1]='7'

    return int(''.join(a))

def nxtd(a):
    a=list(str(a))
    l=len(a)
    i=0
    s=''
    while (a[i]=='2') or (a[i]=='3') or (a[i]=='5') or (a[i]=='7'):
        i+=1
    #print "i:",i
    #print "s:",s
    if(a[i]<'2'):
        #print "I am in 2"
        a[i]='2'
        s+=''.join(a[:i+1])
        i+=1
    elif(a[i]<'3'):
        #print "I am in 3"
        a[i]='3'
        s+=''.join(a[:i+1])
        i+=1
    elif(a[i]<'5'):
        #print "I am in 5"
        a[i]='5'
        s+=''.join(a[:i+1])
        i+=1
    elif(a[i]<'7'):
        #print "I am in 7"
        a[i]='7'
        s+=''.join(a[:i+1])
        i+=1
    else:
        #print "I am in else"
        if(len(a[:i])!=0):
            s=str(nxt(int(''.join(a[:i]))))
        else:
            s=str(nxtd(0))
        s+='2'
        i+=1
    while(i<l):
        s+='2'
        i+=1
    return int(s)

def chk(n):
    if(n<10):
        if(n==2 or n==3 or n==5 or n==7):
            return True
        else:
            return False
    else:
        r=n%10
        if(r==2 or r==3 or r==5 or r==7):
            return chk(n/10)
        else:
            return False

def chkp(n):
    cnt=2
    i=2
    while(i*i<n):
        if(n%i==0):
            cnt+=2
        i+=1
    if((int(math.sqrt(n))**2)==n):
        cnt+=1
    if(cnt!=2):
        return False
    else:
        return True

#seive()
cnt=0

'''
for i in pr.keys():
    if(i>=f and chk(i)):
        cnt+=1
'''
#print cnt

#n=int(raw_input())
#for i in xrange(n):
#    s=int(raw_input())
#    if(chkp(s)):
#        print "Prime"
#    else:
#        print "NotPrime"
#        print nxt(s)
#    else:
#        print nxtd(s)

if(chk(f)):
    i=f
else:
    i=nxtd(f)

while(i<=l):
    if(chkp(i)):
        cnt+=1
    i=nxt(i)

print cnt
