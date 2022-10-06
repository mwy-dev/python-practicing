# Michał Wysocki
import math

wartosci=[1.5, 1.8, 0.5, 0.7, 1.2, 0.6, 1.0]
print("Wartości xi: %s" % wartosci)
ilosci=[25003, 30012, 23005, 20007, 62015, 22022]
print("Ile razy dana wartość pojawiła się w próbie: %s" % ilosci)
a = ''
while a.isdigit() == False:
    a = input('Wprowadź ilość pojawień w próbie dla wartości 1.0: ')
    if a.isdigit() == True:
        print("Wprowadzono liczbę: %s" % a)
        ilosci.append(int(a))
    else:
        print("Wprowadzona liczba nie jest liczbą naturalną!")

#Średnia
proba=[]
for i in (range(len(ilosci))):
    v=ilosci[i]+len(proba)
    while len(proba) < v:
        proba.append(wartosci[i])

s=round(sum(proba)/len(proba), 2)
print("Średnia z próby: %s" % s)

#Mediana
psort=[]
for i in sorted(proba):
    psort.append((i))

if len(psort) % 2 == 0:
    me=(psort[int(len(psort)/2)]+psort[int((len(psort)/2+1))])/2
else:
    me=psort[int((len(psort)+1)/2)]

print("Mediana z próby: %s" % me)

#Odchylenie
licznik=[]
for i in proba:
    k=float(proba[int(i)])
    licznik.append((k-s)**2)
o=round(math.sqrt(sum(licznik))/(len(proba)-1), 5)
print("Odchylenie standardowe z próby: %s" % o)

uchwyt = open('wynik.txt', 'w')
uchwyt.write("Wartość podana przez użytkownika: %s" % a)
uchwyt.write("\n")
uchwyt.write("Średnia z próby: %s" % s)
uchwyt.write("\n")
uchwyt.write("Mediana z próby: %s" % me)
uchwyt.write("\n")
uchwyt.write("Odchylenie standardowe z próby: %s" % o)
uchwyt.close()

input('Zamknij...')
input('Koniec..')