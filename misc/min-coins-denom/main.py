d=map(int, raw_input().split())
ln=len(d)
mmn={}

amm=int(raw_input())

def mc(am):
    if(mmn.has_key(am)):
        return mmn[am]
    if(am==0):
        mmn[am] = (0,[])
        return mmn[am]
    if(am in d):
        mmn[am] = (1,[am])
        return mmn[am]
    if(am<0):
        mmn[am] = (float("inf"),[])
        return mmn[am]

    a=[]
    b=[]

    mn=float("inf")

    for i in xrange(ln):
        x,y=mc(am-d[i])
        a.append(x+1)
        b.append([])
        for j in y:
            b[i].append(j)
        b[i].append(d[i])
        if(a[i]<mn):
            mn=a[i]

    for i in xrange(ln):
        if(a[i]==mn):
            mmn[am]=(a[i], b[i])
            return mmn[am]

x,y=mc(amm)
y.sort(reverse=True)
if(x==float("inf")):
    print -1
else:
    for j in y:
        print j,
