#!/usr/bin/python2

n = int(raw_input())

ls = []
for i in xrange(n):
    lt = map(int, raw_input().split())
    ls.append((lt[0],lt[1]))

ls.sort()

i = 0

while(i<=len(ls)-2):
    if(ls[i][0]==ls[i+1][0]):
        ls.pop(i)
    else:
        i+=1

i = n-1
mx = -float("inf")
while(i>-1):
    if(ls[i][1]>mx):
        mx = ls[i][1]
    else:
        ls.pop(i)
    i-=1

n = len(ls)

'''

def mc(ind):
    if(mp.has_key(ind)):
        return mp[ind]
    if(ind == n-1):
        mp[ind] = ls[ind][0]*ls[ind][1]
        return mp[ind]
    i = ind+1
    mn = float("inf")
    while(i<n):
        tm = (max(ls[ind][0],ls[i-1][0])*max(ls[ind][1],ls[i-1][1]))+mc(i)
        if tm <= mn:
            mn = tm
        i+=1
    mp[ind] = mn
    return mn

'''

def insxn(m1,c1,m2,c2):
    x = float(c2-c1)/(m1-m2)
    y = m1*x + c1
    return (x,y)


cs={}
cs[n] = 0
#cs[n-1] = ls[n-1][0]*ls[n-1][1]
i = n-1
e = []
e = [(ls[n-1][0], cs[n], -float("inf"), float("inf"))]

def rmne(st,en,x):
    if(st==en):
        return e[md][0]*x + e[md][1]
    elif(en==st+1):
        if(x<=e[st][3]):
            return e[st][0]*x + e[st][1]
        elif(x>=e[en][2]):
            return e[en][0]*x + e[en][1]
    md = (st + en)/2
    if(e[md][2]<=x and x<=e[md][3]):
        return e[md][0]*x + e[md][1]
    elif(x>e[md][3]):
        return rmne(md,en,x)
    elif(x<e[md][2]):
        return rmne(st,md,x)

def mne(x):
    if(len(e)==1):
        return e[0][0]*x + e[0][1]
    else:
        return rmne(0,len(e)-1,x)

def ade(m,c):
    l = len(e)
    if(l==1):
        e.append((m,c,insxn(e[0][0],e[0][1],m,c)[0], float("inf")))
        m1,c1,x,y = e[0]
        e[0] = (m1,c1,-float("inf"),e[1][2])
    elif(insxn(m,c,e[l-1][0],e[l-1][1])[0] <= e[l-1][2] ):
        e.pop(l-1)
        ade(m,c)
    else:
        inx = insxn(m,c,e[l-1][0],e[l-1][1])
        #e[l-1][3] = inx[0]
        m1,c1,x,y = e[l-1]
        e[l-1] = (m1,c1,x,inx[0])
        e.append((m,c,inx[0], float("inf")))


while(i>-1):
    #print "e:",e
    cs[i] = float("inf")                # c = c[j+1]; m = ls[j][0]  j>i  ln[j] > ln[i]  w[i] > w[j]

    cs[i] = mne(ls[i][1])

    if(i!=0):
        ade(ls[i-1][0], cs[i])

    '''
    j = i
    while(j<n):
        cs[i] = min(cs[i], cs[j+1] + ls[j][0]*ls[i][1])
        j+=1
    '''

    i-=1

print cs[0]
#print cs
#print ls
