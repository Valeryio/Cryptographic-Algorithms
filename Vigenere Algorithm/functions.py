import sys



def match_letter_to_number(text):

    #alphabet = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

    cardinal = [i for i in range(26)]
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    alphabet = {i:k for i,k in zip(letters, cardinal)}


    dict = []

    for i in text:
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
        clear_text = input((" : ")).lower()

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



def verify_number_of_letters(text, key):

    if(len(text) == len(key)):
        print("The matching is perfect !")
    else:
        print("The matching is imperfect!")



def formating(var):
    var = var.replace(" ", "").lower()

    return list(var)



def right_key(text_splitted, key_splitted):
    custom_key = []
    customised_key = []

    while len(custom_key) < len(text_splitted):
        for i in key_splitted:
            custom_key.append(i)

    for i in range(len(text_splitted)):
        customised_key.append(custom_key[i])
    
    return customised_key



def return_in_base(var):
    while(var <= 1):
        var = var + 26

    while(var >= 26):
        var = var - 26

    return var
    
