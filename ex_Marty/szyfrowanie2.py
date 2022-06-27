message = 'wiadomosc'


def cyphering(message):
    mess_as_list = []
    for i in message:
        mess_as_list.append(i)
    mess_as_list.insert(0, '') # to have real message start at index 1.
    new_list = []
    n = 1
    while n <= len(message):
        new_list.append(mess_as_list[n])
        new_list.append(mess_as_list[-n])
        n = n + 1
    return(new_list)

cyphered = cyphering(message)
#print(cyphered)

cyphered_str = ''.join(cyphered)
print('cyphered message:', cyphered_str)



decyph = cyphered_str[::2]
print('and decyphered message:', decyph)
