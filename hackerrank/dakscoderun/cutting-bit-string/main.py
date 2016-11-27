s=raw_input()
ln=len(s)

n={}

gmn=float("inf")

def nm(i,j):
    if(n.has_key(i)):
        if(n[i].has_key(j)):
            return n[i][j]

    else:
        n[i]={}

    if(i==j):
        n[i][j]=int(s[i])

    else:
        n[i][j]=2*nm(i,j-1)+int(s[j])

    return n[i][j]

def chk(n):
    brk=False
    if n==0:
        return False
    elif n==1:
        return True
    else:
        while(n!=1):
            if(n%5!=0):
                return False
            n/=5
        return True
def mn(i):
    if(i<ln and s[i]=='0'):
        return float("inf")
    if(i==ln-1 and s[i]=='1'):
        return 1
    elif(i==ln):
        return 0
    lmn=float("inf")
    j=i
    while(j<ln):
        if(chk(nm(i,j))):
            m=1+mn(j+1)
            if(m<lmn):
                lmn=m
        j+=1
    return lmn

ans=mn(0)
if(ans==float("inf")):
    print -1
else:
    print ans
