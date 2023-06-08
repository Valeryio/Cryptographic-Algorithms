from functions import *


print("\n\n||||||||||||||      ||||||||||||      |||||||||||||      ||||||||||||||      ||||||||||          ")
print("||||||||||||||      ||||||||||||      |||||||||||||      ||||||||||||||      ||||||||||          ")
print("|||||               ||||              |||||              |||||    |||||      ||||   |||          ")
print("|||||               ||||||||||||      |||||||||||||      ||||||||||||||      ||||||||||          ")
print("|||||               ||||                      |||||      |||||    |||||      ||||||||||||        ")
print("||||||||||||||      ||||||||||||      |||||||||||||      |||||    |||||      ||||    |||||       ")
print("||||||||||||||      ||||||||||||      |||||||||||||      |||||    |||||      ||||      ||||      ")



options = 0

#Verifying the option the user want to use, decrypt or encrypt

try : 
    options = int(input("\n2Welcome to the César's algorithm\nChoose an option of what you want to do : \n1- Encrypt\n2-Decrypt\n Answer : "))

except ValueError:
    
    print("You have entered an option that we don't have. Now you'll try until you gave a right value, or end the program\n")
    
    while( (options != 1) or (options != 2) ):
            try : choice = int(input(("\nChoose a right options \n1 - Encrypt\n2 - Decrypt \n Answer : ")))
            except ValueError:
                print("")


shifts = 0


#Verify the value of the shift we get to make sure that it's a valid number and not a text or 0

try : 

    print("\nRemember that you cannot give 0 as shift\n")

    shifts = int(input("Give a shift to make the encryption : "))

except : 
     
    print("\nYou have entered a text, we request a number, so try again")

    while(shifts == 0):
        try: 
            shifts = int(input("\nGive a shift to encrypt/decrypt : "))

            print("The shift could not be 0") if shifts == 0 else print()

        except ValueError:
            print()


#Getting the text from the user 

if(options == 1):
    print("Give the text you want to cipher ")
else: 
    print("Give the text you want to decipher ")
    

text = input("\nAnswer : ")

#text = controling_text()

print("This is the text that you have entered : ", text)

#text = text.lower()



#Macthing the different letters given with their letters in the alphabet
text_numbers = match_letter_to_number(list(text.lower()))


print("Here we can see the text numbers : ", text_numbers)

#Adding the shift to find the right letter
if(options == 1):
    for i in range(len(text_numbers)):
        text_numbers[i] = return_in_base( text_numbers[i] + shifts ) 
else: 
    for i in range(len(text_numbers)):
        text_numbers[i] = return_in_base( text_numbers[i] - shifts ) 



#Finding the letters that match with the numbers of the ciphered or deciphered message

ciphered = match_number_to_letter(text_numbers)



if(len(ciphered) == len(text)):
    
    #Converting the list in a string that the user can take and use

    result = ""

    for i in ciphered:
        result += i


    print("The result is : ", result, " or : ", result.upper())

else: 

    text_array = list(text)

    answer = []

    tmp = 0

    
    print("The result is : ", ciphered)



    for i in range(len(text)):

        if(tmp < len(ciphered)):

            #Controling if it's a letter that we are face in
            if(  controling_alphabet(  text[i].lower()  )   ):

                print("La lettre ", text[i], " Est dans l'aphabet, poursuivons !")

                #Controling if the letter is upper or lower case

                if(   text[i].lower() == text[i]  ):
                #That means that the letter is in lower characters

                    print('VOici le text : ', text[i])

                    answer.append(  ciphered[tmp]   )

                    tmp += 1

                else: 
                #That means that the letter is in upper characters

                    answer.append(  ciphered[tmp].upper()   )

                    tmp += 1


            else : 

                answer.append(text_array[i])
                

    print("THe result : ", answer)

    result = ""

    for i in answer:
        result += i


    print("The result is : ", result, " or : ", result.upper())


#ZEPIVC NI RI 45678 WYMW TEW YR SVHMREXIYV JEGMP +98][#';PUE\2345


