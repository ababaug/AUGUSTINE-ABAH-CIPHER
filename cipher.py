import unicodedata
# coding: utf-8

def cipher(lineNumber):
    alpha_dict = {}
    with open("files/input.txt", "r") as instr:
        line = instr.readlines()[lineNumber]
        r_line = line.rstrip() # removes space beneath
        instr_list = r_line.split(":")
        count = int(instr_list[0])
        enc_dec = int(instr_list[1])
        lang = int(instr_list[2])
        text = instr_list[3]
        with open("files/languages.txt", 'r') as language:
            lang_line = language.readlines()[lang]
            r_lang_line = lang_line.rstrip() # removes space beneath
            alphabets = r_lang_line[r_lang_line.find("[") + 1 : r_lang_line.find("]")].split()
            for alpha in alphabets:
                _alpha = {alpha : alphabets[(alphabets.index(alpha) + count) % 26]}
                alpha_dict.update(_alpha)
            
            if(enc_dec == 0 ):  #encrypt
                encrypt(alpha_dict, text)
            elif(enc_dec == 1): #decrypt
                decrypt(alpha_dict, text)
            else:
                return "Invalid choice of encryption or decryption"
                


def encrypt(alpha_dict, text):
    cypherText = ""
    for letter in text:
        if letter == " ":
            cypherText += " "
        else:
            cypherText += "%s" %alpha_dict.get(letter)
    print("Screen Output -> "+ cypherText)
        

def decrypt(alpha_dict, text):
    decyphered = ""
    key_list = list(alpha_dict.keys())
    value_list = list(alpha_dict.values())
    for letter in text:
        if letter == " ":
            decyphered += " "
        else:
            decyphered += key_list[value_list.index(letter)]
    print("Screen Output -> "+ decyphered)