import sys

#CONTROLS FUNCTIONS

###################################################################################################################################
###################################################################################################################################
###################################################################################################################################

def controling_alphabet(text):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        a = 0

        for i in text:
            for j in letters:

                if(i == j):
                    a += 1

                    break

        if(a == len(text)):
            return True
        else:
            return False



def controling_text():

    tmp = ""

    control = "y"

    clear_text = ""

    while(control == 'y'):
        clear_text = input(("Answer : ")).lower()

        tmp = controling_alphabet(clear_text) 
        
        if(tmp == True):
            print("The entry is right!")

            return clear_text
        
        else:
            control1 = input("Letters of your text are not in the alphabet! \nDo you want to try again? (Y/N) : ").lower()
            control = control1.replace(" ", "")
        
    if(control == "n"):
        print("\n\nEnd of program, you entry is not valid!")
        sys.exit()



###################################################################################################################################
###################################################################################################################################
###################################################################################################################################
                                                                                                                                                                    



def match_letter_to_number(text):

    chain = list(text)

    chain.append("a") if ((len(chain) % 2) != 0) else print()

    cardinal = [i for i in range(26)]
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    alphabet = {i:k for i,k in zip(letters, cardinal)}


    dict = []

    for i in chain:
        for j in alphabet:

            if( i == j):
                dict.append(alphabet[j])

    return dict




def match_number_to_letter(text):

    cardinal = [i for i in range(26)]
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    alphabet = {i:k for i,k in zip(letters, cardinal)}

    dict = []

    for i in text:
        for j in alphabet:
                
                if( i == alphabet[j]):
                    dict.append(j)
                

    return dict




def fill_matrix(matrix, lenght):
    
    while(len(matrix)<lenght):
        try:
            a = int(input("\nGive an element of the encryption matrix : "))
            matrix.append(a)

        except ValueError:
            print("\nThe entered value is not an enter!Try again!")


    return matrix



def is_inversible(matrix):

    det = matrix[0]*matrix[2] - matrix[1]*matrix[3]

    det = return_in_base(det)

    if(det == 0):
        return False
    
    return det



def return_in_base(var):
    while(var < 0):
        var += 26
    
    while(var > 25):
        var -=26
    
    return var




def pgcd(a, b):
    if(a<b):
        a, b = b, a

    while((a%b) != 0):
        c = a
        b = a%b
        a = c

    return b




def BEZOUT(det):
    i = 0

    while(((det * i) -1) % 26 !=0):
        i +=1

    return i




def binary_1(decimal):

    binaire = []

    c = decimal % 2

    while( decimal != 0):
        binaire.append(decimal % 2)

        decimal = decimal // 2    

    binaire.reverse()

    return binaire
    



def comatrice(matrice):

    matrice[0], matrice[2] = matrice[2], matrice[0]
    matrice[1], matrice[3] = -matrice[1], -matrice[3]

    return matrice




def break_strings(var):

    chain = list(var)

    a = []
    breaked_string = []

    for i in range(len(chain)):
        
        a.append(chain[i])

        if( (i % 2) != 0):
            breaked_string.append(a)
            a = []

    return breaked_string




def matrix_mult(matrice, matrice1):
    mult = []

    mult.append((matrice[0]*matrice1[0]) + (matrice[1] * matrice1[1]))
    mult.append((matrice[2]*matrice1[1]) + (matrice[3] * matrice1[0]))

    return mult
