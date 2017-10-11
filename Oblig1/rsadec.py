# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 12:38:34 2017

@author: preben
"""
def asciii(tallting):
    if tallting == 99:
        return ' '
    else:
        return chr(65+tallting)



msg = [3041999, 4179908, 10100499, 11041306, 4991908, 11990920, 11999999]
streng = ''
streng1 = ''
listen = ''
for tallq in msg:
    streng = streng + str(tallq) + ' '
streng = streng[:-1]
sliste = streng.split(' ')
for bok1 in sliste:
    while len(bok1) < 8:
        bok1 = '0' + bok1
    streng1 = streng1 + bok1

tallet = 0
for enkel in streng1:
    if tallet%2 == 0 and tallet != 0:
        listen += ' '
    listen+=enkel
    tallet+=1
tab = listen.split(' ')
ut = ''
for bok in tab:
    ut += asciii(int(bok))
print(ut)