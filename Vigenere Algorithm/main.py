from functions import *
from time import sleep
import sys
import string

print('\n\n||||||         ||||||   ||||   ||||||||||||      ||||||||||||   |||||      ||||   ||||||||||||   |||||||||||||     |||||||||||||||   |||||||||||||    |||||||||||||||  ')
print(' ||||||       ||||||    ||||   ||||||||||||      ||||||||||||   |||||||    ||||   ||||||||||||   |||      ||||     |||||||||||||||   |||      ||||    |||||||||||||||   ')
print('  ||||||     ||||||     ||||   |||               |||            |||| |||   ||||   |||            |||      ||||     |||               |||      ||||    |||               ')
print('   ||||||   ||||||      ||||   |||      ||||||   ||||||||||||   ||||  |||  ||||   ||||||||||||   |||||||||||||     |||||||||||||||   |||||||||||||    |||||||||||||||   ')
print('    |||||| ||||||       ||||   |||      ||||||   ||||||||||||   ||||   ||| ||||   ||||||||||||   |||||||||||       |||||||||||||||   |||||||||||      |||||||||||||||   ')
print('     |||||||||||        ||||   |||         |||   |||            ||||    |||||||   |||            ||||||  ||||      |||               ||||||   ||||    |||               ')
print('       |||||||          ||||   |||||||||||||||   ||||||||||||   ||||     ||||||   ||||||||||||   ||||||    ||||    |||||||||||||||   ||||||    ||||   |||||||||||||||   ')
print('        |||||           ||||   |||||||||||||||   ||||||||||||   ||||      |||||   ||||||||||||   ||||||     ||||   |||||||||||||||   ||||||     ||||  |||||||||||||||   ') 


#Getting the value of the user, and verifiing if there are right!

option = 0

try : 
    options = int(input('\nHere is the implementation of Vigenere\'s cryptographic algorithm. \n What do you want to do : \n1- Encrypt \n2- Decrypt \n    Answer : ')) 

    print("\nRight, keep going...")

except ValueError:
    print("We have not this options. Try again!")

    print("\nWe will give you the chance to try three time more. After that, you should restart the program!")

    i=0

    #When the person enter bad values
    while(i<3):
        try : 
            options = int(input('Here is the implementation of Vigenere\'s cryptographic algorithm. \n What do you want to do : \n1- Encrypt \n2- Decrypt \n    Answer : ')) 
            
            print("\nRight, keep going...")
            
            sleep(1)
            
            break

        except ValueError:
            print("We have not this options. Try again!\n")

        i +=1

    if((options != 1) and (options != 2)):
        print("\n\nEnd of program, you entry is not valid!")
        sys.exit()




#Controling the text input

if( options == 1):
    print("Give the text you want to cipher")
else:   
    print("Give the text you want to decrypt")


clear_text = controling_text()
text_splitted = formating(clear_text)

print("Enter the key you want to use")
key = controling_text()
key_splitted = formating(key)


#Creating a key that have the same numbers of characters than the text
customised_key = right_key(text_splitted, key_splitted)


text_matched_letters = match_letter_to_number(text_splitted)
key_matched_letters = match_letter_to_number(customised_key)

#Verifying if the matching of the size of the key and the text
#verify_number_of_letters(text_matched_letters, key_matched_letters)

dict_1 = []

####     CYPHERING

if(options == 1):

    for i in range(len(text_matched_letters)):
        a = return_in_base(text_matched_letters[i]+key_matched_letters[i])

        dict_1.append(a)


    result1 = match_number_to_letter(dict_1)

    result = ''.join(result1)

    print("The decrypted text is : ", result)


####     DECYPHER

else: 

    decrypted_text_numbers = []

    for i in range(len(text_matched_letters)):

        d = return_in_base(text_matched_letters[i] - key_matched_letters[i])

        decrypted_text_numbers.append(d)


    decrypted_text_letters = match_number_to_letter(decrypted_text_numbers)


    decrypted_text = ''.join(decrypted_text_letters)

    print("The decrypted text is : ", decrypted_text)