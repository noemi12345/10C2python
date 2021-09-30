# kerekítés round(mit, tizedesek száma)
print(round(3.1415, 3))
print(round(3.1415, 2))
# hatványozás
print(pow(2, 8)) #pow(alap, kitevő) 
#abszolútérték abs(mit)
print(abs(-12))
print(abs(12))
print(min(12,7,9,45,3))
print(max(12,7,9,45,3))
#pi
'''
import math
a=math.pi
print(a)
'''
from math import * #program elején helyezzük el
a=pi
print(a)
#négyzetgyök -sqrt
print(sqrt(16)) #math.sqrt()
#felfelé kerekítés - ceil(mit kerekítek)
print(ceil(3.16))
#lefelé kerekítés math.floor(mit)
print(floor(3.56))

#1. négyzet kerülete, területe
a = input("Add meg a négyzet oldalát!")
a=float(input("Kérem a négyzet oldalát! a="))
k=4*a
t=pow(a,2)
print("a(z)",a, "egység oldalú négyzet kerülete", k, "területe", t)
print("A négyzet kerülete", k)
print("A négyzet területe", t)

#2. téglalap kerülete, területe


#3. kör kerülete (2*r*PI) területe (r^2*PI)


#4. kocka térfogata (V=a^3), felszíne (A=6*a^2)


#5. derékszögű háromszög 2 befogóját kérd be, add meg az átogót!
# c=négyzetgyök(a^2+b^2)