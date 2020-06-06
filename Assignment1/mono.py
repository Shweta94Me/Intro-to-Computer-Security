import sys
import os
import re
import random

position = [*range(97, 123, 1)]

def printPlainCipherMapping(pos):
    print("Plaintext-Ciphertext")
    for i in range(len(pos)):
        print(chr(i+97)+'-'+chr(pos[i]),end=",")
    print('\n')

def generateCipherText(s):
    encryptedText = ""
    for val in s:
        encryptedText += chr(position[ord(val) - 97])
    return encryptedText

def generatePlainText(s):
    decryptedText = ""
    for val in s:
        idx = position.index(int(ord(val)))
        decryptedText += chr(idx + 97)
    return decryptedText

def monoalphabeticCipher():
    inputFile = sys.argv[1]
    if not os.path.isfile(inputFile):
        print("Input file does not exist.")
        sys.exit()

    outputFile = sys.argv[2]
    if not os.path.isfile(outputFile):
        print("Output file does not exist.")
        sys.exit()

    fp1 = open(inputFile)
    content = (fp1.read()).rstrip('\n')
    #content = fp1.read()
    fp1.close()

    fp2 = open(outputFile, 'w')
   
    if(content):
        res = re.sub('[a-z]','',content)
        if(len(res) != 0):
             print("File contains characters other than a-z (lowercase).")
             sys.exit()
        elif(sys.argv[3] == '1'):
             printPlainCipherMapping(position)
             encryptedText = generateCipherText(content)
             fp2.write(encryptedText)    
        elif(sys.argv[3] == '0'):
             printPlainCipherMapping(position)
             decryptedText = generatePlainText(content)
             fp2.write(decryptedText)
    else:
        print("File does not contain any characters")
    fp2.close()

if __name__ == '__main__':
    random.seed(5)
    random.shuffle(position)
    monoalphabeticCipher()
