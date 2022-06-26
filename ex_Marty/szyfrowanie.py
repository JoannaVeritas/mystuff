message = 'koniczyna'

#print('dlugosc wiadomosci: ', len(message))

def szyfrowanie(wiadomosc):
    print('wiadomosc na poczatku: ', wiadomosc)
    wiadomosc_jako_lista = []
    for i in wiadomosc:
        wiadomosc_jako_lista += i
    print('wiadomosc jako lista: ', wiadomosc_jako_lista)
    duplikat_tej_listy = wiadomosc_jako_lista.copy()

    rev_wiadomosci = duplikat_tej_listy[::-1]
    print('rev wiadomosci: ', rev_wiadomosci)

    n = 0
    zaszyfrowana = []
    #print(len(wiadomosc))
    while n <= len(wiadomosc)/2 :
        zaszyfrowana.append(duplikat_tej_listy[n])
        zaszyfrowana.append(rev_wiadomosci[n])
        n = n + 1

    return zaszyfrowana


def deszyfrowanie(zaszyfrowana):
    zaszyfrowana_lista = []
    for i in zaszyfrowana:
        zaszyfrowana_lista += i
    print('????????????????', zaszyfrowana_lista) # ok, dziala.

    for z in zaszyfrowana_lista[::2] :
         print(z, end ='')



    zupa = 1
    for x in zaszyfrowana_lista:
        deszyf.append(zaszyfrowana_lista[zupa])
        zupa = zupa + 2
    print('a teraz?', deszyf)

    return deszyf


x = szyfrowanie(message)
print('zaszyfrwana jako lista: ', x)
zaszyfrowana = ''.join(x)
print('wiadomosc: ', zaszyfrowana)

y = deszyfrowanie(zaszyfrowana)
print('deszyfrowana: ', y)
