def encode(plaintext):
    alphabet= "abcdefghijklmnopqrstuvwxyz"
    reversedalphabet= alphabet[::-1]
    cipher=""
    for char in plain_text:
        if char.lower() in alphabet:
            newtext= reversedalphabet[alphabet.index(char)]
            cipher=cipher+newtext
        else:
            cipher=cipher+char
    return cipher

plain_text= input("Enter text to encode: ")
encoded_text= encode(plain_text)
print("Encoded text:", encoded_text)