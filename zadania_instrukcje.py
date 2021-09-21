#Zadanie 1
'''
a = int(input('Podaj pierwszy bok trójkąta: '))
b = int(input('Podaj drugi bok: '))
c = int(input('Podaj trzeci: '))

if ((a*a+b*b==c*c) or (a*a+c==b*b) or c*c+b*b==a*a):
    print('Trójkąt jest prostokątny!')
else: print('Trójkąt nie jest prostokątny!')
'''

#Zadanie 2
'''
liczba = int(input('Podaj dowolną liczbę: '))

if liczba == 0:
    print('Liczba ma wartość równą zero.')
elif liczba > 0:
    print('Liczba jest dodatnia.')
else: print('Liczba jest ujemna.')
'''

#Zadanie 3
'''
a = int(input('Podaj dowolne 3 liczby: '))
b = int(input())
c = int(input())

if a > b and a > c:
    print('Największa jest', a)
elif b > a and b > c:
    print('Największa jest', b)
else: print('Największa jest', c)
'''

#Zadanie 4
'''
print('GRA W KAMIEŃ, PAPIER, NOŻYCE')
wybór = (input('Co wybierasz? '))
if wybór != 'kamień' and wybór != 'nożyce' and wybór != 'papier':
    print('Błędne dane')
else: wybór1 = (input('Drugi gracz: '))

if wybór == 'kamień' and wybór1 == 'nożyce':
   print('Wygrał', wybór) 
elif wybór == 'papier' and wybór1 == 'kamień':
    print('Wygrał', wybór)
elif wybór == 'papier' and wybór1 == 'nożyce':
    print('Wygrały', wybór1)
elif wybór == 'kamień' and wybór1 == 'papier':
    print('Wygrał', wybór1)
elif wybór == 'nożyce' and wybór1 == 'papier':
    print('Wygrały', wybór)
elif wybór == 'nożyce' and wybór1 == 'kamień':
    print('Wygrał', wybór1)
elif wybór == wybór1:
    print('Remis!')
else: print('Błędne dane')

'''

#Zadanie 5
'''
liczba = int(input('Podaj liczbę: '))
liczba1 = int(input('Podaj drugą liczbę: '))

if liczba % 2 == 0 or liczba1 % 2 == 0:
    print('Jedna z liczb jest parzysta!')
else: print('Żadna z liczb nie jest parzysta!')
'''

#Zadanie 6
'''
import random
import time

user = 0
computer = 0
licznik = 0 
o = 'orzeł'
r = 'reszka'
wybór = input('Wybierz orła(o), reszkę(r) ')
if wybór != 'o' and wybór != 'r':
    while True:
        print('Zły wybór wybierz orła(o) albo reszkę(r)')
        wybór = input()
        #licznik = licznik + 1
        if wybór == 'o' or wybór == 'r':
            break
        else: continue

i = 3
while i > 0:
    print(i)
    time.sleep(0.5)
    i -= 1

losowo = random.choice([o, r])
print(losowo)

if losowo == o and wybór == 'o' or losowo == r and wybór == 'r':
        print('Wygrałeś!')
        user += 1
else: 
        computer += 1 
        print('Przegrałeś!')

print('Ty', user,'Komputer', computer)
'''

