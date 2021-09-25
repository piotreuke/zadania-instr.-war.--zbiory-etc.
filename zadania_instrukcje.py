#Instrukcje warunkowe

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

#Krotki i zbiory

#Zadanie 1
'''
kolory = ['zielony', 'czerwony', 'niebieski', 'czarny',
 'fioletowy', 'granatowy', 'niebieski', 'czarny', 'czarny',
 'zielony', 'cytrynowy', 'granatowy', 'niebieski', 'indygo',
 'zielony', 'czerwony']

zbiór = set(kolory)
ile = len(kolory)
ile1 = len(zbiór) #ile kolorów zostało użytych
print(ile) 
print(ile1)
print(*zbiór, sep='\n') #każdy w osobnej linii

kolory.append('szary')
print(kolory)

kolory.remove('zielony')
print(kolory)
'''

#Zadanie 2
'''
zdanie = input('Wpisz zdanie: ')
znaki = ['.', ',', ':', ';', '!', '?']

for i in zdanie:
    if i in znaki:
        zdanie = zdanie.replace(i, '')

print(zdanie)
txt = zdanie.split()
długość = len(txt)
print(długość)
print(txt[0], txt[3])

zbiór = set(txt)
print(zbiór)
zbiór1 = tuple(zbiór)
print(zbiór1[0], zbiór1[3])

if zbiór1[0] == zbiór1[3]:
    print('Takie same!')
else: print('różne')
'''

#Zadanie 3
'''
moje_kolory = {'zielony', 'czerwony', 'granatowy'}
twoje_kolory = {input('Podaj swoje kolory: ')}
print(moje_kolory)
print(twoje_kolory)

print(moje_kolory.intersection(twoje_kolory))

if twoje_kolory == moje_kolory:
    print('takie same')
else: print('inne')

NIE ZROBIONE WRÓCIĆ!!!
'''

#Zadanie 4
'''
A = set([])
B = set([])
numer = int(input('Podaj liczbę n: '))
i = 0
liczba = 0

while i < numer and liczba <= numer:
    if liczba % 2 == 0:
        A.add(liczba)
        liczba += 2
        i += 1
    else: break
print(A)   

j = 0
liczba1 = 5
while j < numer and liczba1 <= numer:
    if liczba1 % 3 == 2:
        B.add(liczba1)
        liczba1 += 3
        j += 1
    else: break
print(B) 
'''

#Słowniki

#Zadanie 1
'''
zespoły = {'The Sensual World' : 'Kate Bush', 'Shaday' : 'Ofra Haza',
'Achtung Baby' : 'U2', 'Aion' : 'Dead Can Dance', 'Invisible Touch' : 'Genesis'}
print(zespoły.keys())

wartość = input('Podaj nazwę albumu: ')
dane = zespoły.get(wartość)
if dane:
    print('Wykonawcą albumu', wartość, 'jest', dane)
else: print('Brak danych')
'''

#Zadanie 2
'''
zespoły = {'The Sensual World' : 'Kate Bush', 'Shaday' : 'Ofra Haza',
'Achtung Baby' : 'U2', 'Aion' : 'Dead Can Dance', 'Invisible Touch' : 'Genesis'}
print(zespoły.keys())

user = input('Czy chcesz dodać album i zespół? (y/n)')
if user == 'y':
    zespół = input('Zespół: ')
    album = input ('Album: ')
    dodanie = zespoły.update({zespół : album})
    print(zespoły)
else: print('')
print('Może chcesz jakiś usunąć?(y/n)')
user2 = input()

if user2 == 'y':
    print('Wpisz nazwę zespołu, bądź albumu, by usunąć parę')
    usuwanie = input()
    zespoły.pop(usuwanie)
else: print('Do widzenia!')
print(zespoły)
'''

#Zadanie 3
'''
tekst = {'Once' : 1, 'upon' : 1 , 'a' : 3, 'midnight' : 1, 'dreary' : 1, 'while' : 2, 'I' : 3, 'pondered' : 1, 'weak' : 1, 'and' : 3, 'weary' : 1,
'Over' : 1, 'many' : 1, 'quaint' : 1, 'curious' : 1, 'volume' : 1, 'of' : 2, 'forgotten' : 1, 'love' : 1, 'nodded' : 1, 'nearly' : 1, 'napping' : 1,
'suddenly' : 1, 'there' : 1, 'came' : 1, 'tapping' : 2, 'As' : 1, 'someone' : 1, 'gently' : 1, 'rapping' : 2, 'at' : 2, 'my' : 2, 'chamber' : 1, 'door' : 1,
'Only' : 1, 'nothing' : 1, 'more' : 1}
'''

