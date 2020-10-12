
def break_cipher(text):
    Alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z' ]
    print(Alphabet)
    text_index = []

    for i in range(len(text)):
        text_index.append(Alphabet.index(text[i]))

    for j in range(len(Alphabet)):
        decrypted = ""
        for k in range(len(text)):
            decrypted += Alphabet[(text_index[k]+j)%26]
        print(decrypted)
            
cipher_text = input('Type cipher text in capital letters:')
break_cipher(cipher_text)