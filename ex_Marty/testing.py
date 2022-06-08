import urllib.request
import random

# 1 generujemy losowe slowo V
def generujSlowo():
    '''w tym przypadku wyciagamy slowa z konkretnej strony internetowej, po czym
    dodajac random.choice wybieramy losowe slowo '''
    fhand = urllib.request.urlopen('https://www.randomlists.com/data/words.json')
    for data in fhand:
        x = data.decode()
    slowa = x.replace('"', '').split(',')

    losoweSlowo = random.choice(slowa)
    return losoweSlowo

slowo = generujSlowo()
print(slowo)

print(generujSlowo.__doc__) #The first string after the function header is
# called the docstring and is short for documentation string. It is briefly used
# to explain what a function does.

# 2 ustawiamy ilosc zyc w zaleznosci od slowa V
def iloscZyc():
    iloscZyc = len(slowo)
    return iloscZyc

iloscZyc = iloscZyc()
print(iloscZyc)

#3 wysietlamy slowo w podlogach  V
def wypodlogujSlowo():
    wypodloguj = '_ ' * iloscZyc
    return wypodloguj

podgladSlowa = wypodlogujSlowo()
print(podgladSlowa)

def wyswietlPowitanie():
    print('\n\n~~~~~~~~~~~~~~~~ Welcome to wisielec ~~~~~~~~~~~~~~~~\n\n')
    print("Sposrod wielu slow wybralem losowo jedno slowo, ktore teraz ty musisz odgadnac\n")
    print('Wylosowane slowo ma', len(slowo), 'liter, w zwiazku z czym masz', len(slowo), 'zyc\n\nPowodzenia!!' )

wyswietlPowitanie()

def literkaWSlowie(letter, word):
    '''sprawdzenie czy podana przez uzytkownika literka znajduje sie w slowie,
    ktore ma odgadnac'''
    index = 0
    podglad = list("_" *len(word))
    while index < len(word):
        current = word[index]
        if current == letter:
            podglad[index] = current
        index += 1
    return "".join(podglad)


#podgladSlowa = zaktualizujPodglad(podgladSlowa, slowo, literka)


while iloscZyc > 0 or czyZgadl == False:
    literka = input("daj literke")
    if literkaWSlowie(slowo, literka):
        podgladSlowa = zaktualizujPodglad(podgladSlowa, slowo, literka)
        print(podgladSlowa)

    else:
        iloscZyc = iloscZyc - 1
        print('ups')
        print(iloscZyc)

    proba = input('zdadnij slowo!: ')
    if proba == slowo:
        print('brawo!')
        czyZgadl = True
    else:
        print('ups')
        iloscZyc = iloscZyc - 1
        print(iloscZyc)

if czyZgadl == True:
    print('Brawo!')
else:
    print('koniec gry')


#def zaktualizujPodglad(x, y, z): #wywolujemy pozniej 3 wartosci wiec musza byc 3 tu tez.
    '''zastapienie podlogi literka'''
