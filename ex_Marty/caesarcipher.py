'''Caesar Cipher'''

#message = input('Provide the message: ').lower()

def cipher(message):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'q', 'x', 'y', 'z']
    alph = ''.join(alphabet)
    alpha = alph + alph
    print(alpha)
    encrypted = ''
    shift = int(input('provide shift value: '))
    if shift < 2*len(alphabet):
        for letter in message:
            pos = alpha.find(letter)
            nlet = alpha[pos+shift]
            encrypted += nlet
    else:
        print('Przesuniecie to big')
        quit()

    return encrypted


message = input('Message that you want to encrypt: ')
print(cipher(message))
