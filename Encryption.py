step = 10
alph = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
            'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!',
            '#', '$', '+', '-', '/', ':', '@', '[', '.', '*',]

def encrypt(input):
    ciphertext = ""
    for x in input:
        chri = alph.index(x) + step
        if chri > len(alph):
            chri = chri % len(alph)
        ciphertext += alph[chri]
    return ciphertext

def decrypt(ciphertext):
    input = ""
    for x in ciphertext:
        chri = alph.index(x) - step
        if chri < len(alph):
            chri = chri % len(alph)
        input += alph[chri]
    return input