# -*- coding: utf-8 -*-
# Oskar Myhre Midbøe, Preben Haukebøe og Sindre Tornes Steinsvik
"""
Spyder Editor

This is a temporary script file.
"""
#Oppgave a
(n,e) = (216541799, 241)
t1 = 70408180
t2 = 1313
klar = (t1, t2)
svar1 = RSA_encrypt(n, e, klar)
#Output[132957703, 185758505]


#Oppgave b
"""
sqrt(n) må være input til eratosthenes.
vi finner først sqrt(n) og runder ned til nærmeste int
så tester man om n kan deles på noe i listen primtall vi får fra eratosthenes(sqrt(n))
hvis ja, er p lik dette tallet og q er lik n delt på p
"""





#Oppgave c
from math import sqrt
i = int(sqrt(n))
svar2 = eratosthenes(i)
for tal1 in svar2:
    if ((n/tal1)%1)==0:
        p = tal1
q=n/p
# p = 12743, q = 16993
     


#Oppgave d
svar3 = check_key(p,q,e)
# true


#Oppgave e

svar4 = mult_inverse(((p-1)*(q-1)), e)
d=svar4
# d = 114095569

#Oppgave f
svar5 = RSA_encrypt(n, int(d), svar1)
# Output: [70408180, 1313]

#Oppgave g
melding = [138938544, 167918735, 143648527, 162290725, 29951859, 205923221, 136395302]
svar6 = RSA_encrypt(n, int(d), melding)
#melding = det er ikke lenge til jul   


msg = [t1, t2]
streng = ''
for we in msg:
   streng += str(we) + ' '
if int(streng[:2])>26:
    streng = '0'+streng
stre = streng.split(' ')
for qw in stre:
    if len(qw)%2 != 0:
        qw +='0'
        

ut = asciii(2)

















