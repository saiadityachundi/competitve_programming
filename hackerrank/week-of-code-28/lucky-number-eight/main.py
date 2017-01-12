#!/usr/bin/python2

n=int(raw_input())

m=raw_input()

i=-1

ctr=0

while (i<n):
    j=i
    while (j<n):
        k=j
        while (k<n):
            #print i,j,k
            st=''
            if(i!=-1):
                if ((i!=j) and (i!=k) and (j!=k)):
                    st+=m[i]
                    st+=m[j]
                    st+=m[k]
                    if(int(st)%8==0):
                        ctr+=(2**(i))
                    #print st, ctr
            elif (j!=-1):
                if ((i!=j) and (i!=k) and (j!=k)):
                    st+=m[j]
                    st+=m[k]
                    if(int(st)%8==0):
                        ctr+=1
                    #print st, ctr
            elif (k!=-1):
                if ((i!=k) and (j!=k)):
                    if(int(m[k])%8==0):
                        ctr+=1
                    #print st, ctr
            k+=1
        j+=1
    i+=1

print ctr
#print n
#print m
#for i in xrange(len(m)):
#    print m[i]
