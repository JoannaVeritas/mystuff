message = 'wiadomosc do zaszyfrowania'

print(len(message))

message_list = []
for i in message:
    message_list += i

message_duplicat = message_list.copy()

#print(message_list, message_duplicat_list)
reversed_list = message_duplicat[::-1]
print(reversed_list)

zaszyfrowana = []

n = 0
while n <= len(message)/2 :
    zaszyfrowana.append(message_duplicat[n] + reversed_list[n])
    n =+1

wiadomosc = ''.join(zaszyfrowana)
print('lista: ', zaszyfrowana)
print('wiadomosc: ', wiadomosc)
