
'''To jest palidrom droga chalupnicza, raczej nie przyszlosciowy'''

word = input('Podaj slowo, sprawdzimy czy jest palidromem: ')

list = [] # lista zeby dalo sie porownac
for letter in word:
    list += letter

backwards = [] # lista odwroconej kolejnosci word
list.reverse() # rev listy zawierajacej word
for let in list:
    backwards += let

list.reverse() # powrot listy do kolejnosci normalnej

wo = "".join(list) # wypisze word
ow = ''.join(backwards) # wypisze word od tylu


if list == backwards:
    print('tak, to jest palidrom')
else:
    print('to nie jest palidrom')

#def list(word_given):
    #list = []
    #for letter in word_given:
    #    list += letter
    #    return list
