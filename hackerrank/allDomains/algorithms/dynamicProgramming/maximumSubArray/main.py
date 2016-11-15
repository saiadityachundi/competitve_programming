def func(a):
    mx=a[0]
    smx=0
    smn=0
    smnl=0
    pos=0
    cas=0
    nas=0
    s=0
    l=len(a)
    for i in xrange(l):
        if(a[i]>mx):
            mx=a[i]
        if(a[i]>0):
            pos+=1
        s+=a[i]
        if(s>smx):
            smx=s
            smnl=smn
        if(s<smn):
            smn=s
        if(a[i]>0):
            nas+=a[i]
    cas=smx-smnl
    if(pos==0):
        nas=mx
        cas=mx
    print cas, nas

t=int(raw_input())
for i in xrange(t):
    n=int(raw_input())
    s=raw_input().split(' ')
    a=[]
    for j in xrange(n):
        a.append(int(s[j]))
    func(a)

