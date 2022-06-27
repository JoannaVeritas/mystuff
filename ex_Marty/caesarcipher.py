'''Caesar Cipher'''

#message = input('Provide the message: ').lower()

def cipher(message):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'q', 'x', 'y', 'z']
    alpha = ''.join(alphabet)
    encrypted = ''
    shift = int(input('provide shift value: '))
    if shift < 2*len(alphabet):
        alphabet = alphabet + alphabet + alphabet
    else:
        print('Przesuniecie to big')
        quit()
    for letter in message:
        pos = alpha.find(letter)
        nlet = alpha[pos+shift]
        encrypted += nlet
    return encrypted


message = input('Message that you want to encrypt: ')
print(cipher(message))
