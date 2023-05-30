
from functions import *

from string import *


print("\n\n|||     |||   ||||    ||||          ||||           |||||||||||           ")
print("|||     |||   ||||    ||||          ||||           ||||                  ")
print("|||||||||||   ||||    ||||          ||||           |||||||||||           ")
print("|||     |||   ||||    ||||||||||    |||||||||||           ||||           ")
print("|||     |||   ||||    ||||||||||    |||||||||||    |||||||||||           ")


print("\n\nWelcome to the HILL's cryptographic algorithm!\n What do you want to do?\n")

choice = 0

try: 
    choice = int(input(("1 - Encrypt\n2 - Decrypt \nAnswer : ")))

except ValueError:

    print("\n\nWe have not this option. You'll be invited to try again until you choose a right options or close the program\n")

    while((choice != 1) and (choice != 2)):
            try : choice = int(input(("Choose a right options \n1 - Encrypt\n2 - Decrypt")))
            except ValueError:
                print("")



if(choice == 1):

    print("\nGood, we will encrypt a message!")

else:
    print("\nGood, we will decrypt a message!")



#Encryption matrix taking

matrice = []

fill_matrix(matrice, 4)


determinant = is_inversible(matrice)

if(determinant != False):
    print("\nThe given matrix is inversible and its determinant is : ", determinant )


#Verifying if the matrix is usable 
if(pgcd(determinant, 26) == 1):
    print("We can use this matrix to encrypt/decrypt with the algorithm of HILL\n")


#COEFFICIENT DE BEZOUT
bezout_coef = BEZOUT(determinant)


comatrix = comatrice(matrice.copy())

#Multiplication of the comatrix by the Bezout's coefficient

for i in range(len(matrice)):
    comatrix[i] = return_in_base(( comatrix[i] * bezout_coef))


#OPTIONS TO ENCRYPT A TEXT

if(choice == 1):


    #Take the text that the user want to cipher
    print("What is the text you want to cipher? ")

    text = controling_text()

    #Take correspondance in numbers of all the letters in a list of list 
    text_breaked = break_strings(match_letter_to_number(text))


    #Making the calculations to get the cipher correspondance with the numbers (correspondance to the simple letters of the text ) in a list of list format
    cipher_numbers = []

    for i in range(len(text_breaked)):

        cipher_numbers.append(matrix_mult((matrice), text_breaked[i]))



    #After getting the right numbers that will be used to find the new letters that will make the ciphered text, I return them in the base to be sure 
    # to get a correspondance 
    for  i in range(len(cipher_numbers)):
        for j in range(len(cipher_numbers[i])):

            cipher_numbers[i][j] = return_in_base(cipher_numbers[i][j]) 
        



    text_ciphered_numbers = []

    #Making a simple list of the different numbers matching with the letters of the text we want to cipher
    for  i in range(len(cipher_numbers)):
        for j in range(len(cipher_numbers[i])):

            text_ciphered_numbers.append(cipher_numbers[i][j])



    #Here the cipher text are created, cause we just use the match_number_to_letter() function to find the letters and form the set of word that
    #will make he cipher text in a list
    cipher = match_number_to_letter(text_ciphered_numbers)


    #Converting this list to a text and showing the text ciphered
    ciphered_text = ""

    for i in cipher:
        ciphered_text += str(i)

    print('\nThe ciphered text is : ', ciphered_text, 'or ', ciphered_text.upper())


#OPTIONS TO DECRYPT A TEXT    

else:

    #Take the text that the user want to cipher
    print("What is the text you want to decipher? ")

    text = controling_text()

    #Take correspondance in numbers of all the letters in a list of list 
    text_breaked = break_strings(match_letter_to_number(text))

    #Making the calculations to get the decipher correspondance with the numbers (correspondance to the simple letters of the text ) in a list of list format
    decipher_numbers = []

    for i in range(len(text_breaked)):

        decipher_numbers.append(matrix_mult((comatrix), text_breaked[i]))



    #After getting the right numbers that will be used to find the new letters that will make the deciphered text, I return them in the base to be sure 
    # to get a correspondance 
    for  i in range(len(decipher_numbers)):
        for j in range(len(decipher_numbers[i])):

            decipher_numbers[i][j] = return_in_base(decipher_numbers[i][j]) 
        



    text_deciphered_numbers = []

    #Making a simple list of the different numbers matching with the letters of the text we want to cipher
    for  i in range(len(decipher_numbers)):
        for j in range(len(decipher_numbers[i])):

            text_deciphered_numbers.append(decipher_numbers[i][j])



    #Here the cipher text are created, cause we just use the match_number_to_letter() function to find the letters and form the set of word that
    #will make he cipher text in a list
    decipher = match_number_to_letter(text_deciphered_numbers)


    #Converting this list to a text and showing the text ciphered
    deciphered_text = ""

    for i in decipher:
        deciphered_text += str(i)

    print('\nThe ciphered text is : ', deciphered_text, 'or ', deciphered_text.upper())

