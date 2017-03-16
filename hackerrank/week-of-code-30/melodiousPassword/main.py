#!/usr/bin/python2

n = int(raw_input())
s=""

def ppass(c, n, s):            # c is the 1st letter of the password(whether a vowel or a consonant). n is the # of letters.
    if(n==0):
        print s
    else:
        st=s
        if(c=='v'):
            for i in ['a','e','i','o','u']:
                st+=i
                ppass('c', n-1, st)
                st=s
        elif(c=='c'):
            for i in "bcdfghjklmnpqrstvwxz":
                st+=i
                ppass('v', n-1, st)
                st=s

ppass('v', n, s)
ppass('c', n, s)
