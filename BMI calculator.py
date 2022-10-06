print("Prosty kalkulator BMI")

#Michał Wysocki

import matplotlib.pyplot as plt

class dane: #KLASA1
    def wprowadz():
        while True:
            try:
                imie=str(input("Podaj imię: "))
                a=imie
                waga = float(input('Wprowadź wagę w [kg]: '))
                wzrost = float(input('Wprowadź wzrost w [cm]: '))
                if 40 < waga < 150 and 150 < wzrost < 200:
                    return imie, waga, wzrost
            except ValueError:
                print('Wprowadź poprawne dane!')
                continue
class BMI: #KLASA2
    def __init__(self, imie, waga, wzrost):
        self.imie = imie
        self.waga = waga
        self.wzrost = wzrost
    def bmi(self):
        return round(self.waga/((self.wzrost*0.01)**2),2)
    def skala(self):
        if 18.5 > self.bmi():
            return 'Niedowaga'
        if 18.5 < self.bmi() < 25:
            return 'Norma'
        elif 25 < self.bmi() < 30:
            return 'Nadwaga'
        else:
            return 'Otyłość'
    def wynik(self):
        print(self.imie, 'Twoje BMI to:',(self.bmi()))
        print('Wynik BMI to:',(self.skala()))


#obiekt1
a = dane.wprowadz()
print(a)

#obiekt 2
b=BMI(a[0],a[1], a[2])
b.wynik()

class wykres: #KLASA2
    def rysuj():
        x1=[150,200]
        y1=[40,73]
        y2=[56,100]
        y3=[67,120]
        y4=[150,150]
        plt.plot(x1, y1)
        plt.plot(x1, y2)
        plt.plot(x1, y3, color="red")
        plt.plot(a[2], a[1], 'o')
        plt.fill_between(x1, y1, y2, alpha=0.2, color="green")
        plt.fill_between(x1, y2, y3, alpha=0.2, color="orange")
        plt.fill_between(x1, y3, y4, alpha=0.2, color="red")
        plt.fill_between(x1, y1, y2=0, alpha=0.2, color="skyblue")
        plt.text(173, 25, 'NIEDOWAGA', fontsize=15, alpha=0.5)
        plt.text(174, 65, 'NORMA', fontsize=12, alpha=0.4)
        plt.text(173.7, 85, 'NADWAGA', fontsize=12, alpha=0.4)
        plt.text(173.5, 120, 'OTYŁOŚĆ', fontsize=15, alpha=0.5)
        plt.text(a[2]-0.7, a[1]+1.5, a[0], fontsize=10, alpha=1)
        plt.tight_layout()
        plt.title('Porównanie BMI', fontsize=18)
        plt.xlabel('WZROST', fontsize=15)
        plt.ylabel('WAGA', fontsize=15)
        plt.show()
#obiekt 3
c=wykres.rysuj()

input('Koniec..')
