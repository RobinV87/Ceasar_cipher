# Caesar cipher

import pyperclip, os

os.system('clear')
print("=======================================")
print("|                                     |")
print("|           Ceasar Cipher             |")
print("|               V1.0                  |")
print("|                                     |")
print("=======================================")
message = input("What do you want to encrypt:> ")

key = 1

mode = 'encrypt'

# Include space in the SYMBOLS string
SYMBOLS = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()_+}{":>?<:">?< '

translated = ''

for symbol in message:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key

        # Correct the boundary conditions for wrapping around
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]

    else:
        translated = translated + symbol


print(translated)
pyperclip.copy(translated)
