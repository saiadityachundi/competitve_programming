
def func(a, n):
    memd={}         # memd reverses the order of be and id memd[be][id]

    def mins(ids, be):
        if(memd.has_key(be)):
            if(memd[be].has_key(ids)):
                return memd[be][ids]
        else:
            memd[be]={}
    
        if(ids==1): # id-1 is shirt. It says the box before current 'be' is shirt
            if(be==n):
                memd[be][ids]=min(a[be][2],a[be][3])
            else:
                memd[be][ids]=min(a[be][2]+mins(2, be+1), a[be][3]+mins(3, be+1))
    
        elif(ids==2): # id-2 is pant. It says the box before current 'be' is pant
            if(be==n):
                memd[be][ids]=min(a[be][1], a[be][3])
            else:
                memd[be][ids]=min(a[be][1]+mins(1, be+1), a[be][3]+mins(3, be+1))
    
        elif(ids==3): # id-1 is shoe. It says the box before current 'be' is shoe
            if(be==n):
                memd[be][ids]=min(a[be][1], a[be][2])
            else:
                memd[be][ids]=min(a[be][1]+mins(1, be+1), a[be][2]+mins(2, be+1))
        return memd[be][ids]

    return min(a[1][1]+mins(1, 2),a[1][2]+mins(2, 2),a[1][3]+mins(3, 2))

t=int(raw_input())
for i in xrange(t):
    a={}
    n=int(raw_input())
    for j in xrange(n):
        a[j+1]={}
        s=raw_input().split(' ')
        for k in xrange(3):
            a[j+1][k+1]=int(s[k])
    print func(a,n)
