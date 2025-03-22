a=['lista', 'list']
a_tuple=(1,2,3,3,3)

print(a_tuple)
 ##rozpakowywanie krotki

warzywa = ('pomidor', 'ogor', 'kapucha')

(multicolor,*zolty)=warzywa

print(zolty)

krotka1=(1,23)
krotka2=(2,230)
(krotka1, krotka2)=krotka2, krotka1

print(krotka1,krotka2)