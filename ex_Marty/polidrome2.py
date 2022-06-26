
word = input('Podaj slowo, sprawdzimy czy jest palidromem: ')

list = []
for letter in word:
    list += letter

backwards = []
list.reverse() # rev listy zawierajacej word
for let in list:
    backwards += let


drow = ''.join(backwards)
num = len(word)

n = 0
zaszyfrowana = []
while n <= len(word)/2 :
    zaszyfrowana.append(list[n] + backwards[n]) #przeokrotnie sie wiesza. wpada w infinita
    n =+1

print(zaszyfrowana)
