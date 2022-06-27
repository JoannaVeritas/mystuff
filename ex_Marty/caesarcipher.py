'''Caesar Cipher'''

#message = input('Provide the message: ').lower()

def cipher(message):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'q', 'x', 'y', 'z']
    alpha = ''.join(alphabet)
    alph = alpha + alpha
    encrypted = ''
    shift = int(input('provide shift value: '))
    x = shift % 23
    for letter in message:
        pos = alph.find(letter)
        nlet = alph[pos+x]
        encrypted += nlet
    #else:
    #    print('Przesuniecie to big')
    #    quit()

    return encrypted


message = input('Message that you want to encrypt: ')
print(cipher(message))
