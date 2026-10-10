import random

#Firstly, we will write the encryption algorithm which is based on permutation

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lettersA = [letterA for letterA in alphabet] #Seperating all letters in the alphabet

def main():

    random.shuffle(lettersA) #permutating the alphabet to change the order of the plain text's letters.

    cT = encryptor()
    dT = decryptor(cT)

    print(f'Crypted text: {cT}')

    print(f'Decrypted text: {dT}')    

    return lettersA, alphabet


def encryptor():
    pT = str(input("Enter a plain text that you want to encrypt: ")) #Our plain text

    letters = [letter for letter in pT if letter.isalpha()] #Seperating the letters of the plain text

    cT = "" #Our crypted text
    
    for letter in letters:
        order = alphabet.index(letter.upper()) #Finding the order of the letters in unshuffled alphabet

        cT += lettersA[order] #Applying the same order on shuffled alphabet


    return cT

#Now its time to decrypt the crypted text

def decryptor(cT): #Basically similar operations that we have done during encryption
    dT = "" #Decrypted text

    letters = [letter for letter in cT if letter.isalpha()] 

    for letter in letters:
        order = lettersA.index(letter)

        dT += alphabet[order]

    return dT

if __name__ == "__main__": main()
