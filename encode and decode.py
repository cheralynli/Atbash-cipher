def encode(plain_text):
    alphabet= "abcdefghijklmnopqrstuvwxyz"
    reversedalphabet= alphabet[::-1]
    numbers= "123456789"
    cipher=""
    count=0
    for char in plain_text:
        if char.lower() in alphabet:
            if char.isupper():
                newtext= reversedalphabet[alphabet.index(char.lower())]
                cipher=cipher+newtext
                count+=1
            else:
                newtext= reversedalphabet[alphabet.index(char)]
                cipher=cipher+newtext
                count+=1
        elif char in numbers:
            cipher=cipher+char
            count+=1
        else:
            cipher=cipher
        if count%5==0 and cipher[-1]!=" ":
            cipher=cipher+" "
    if cipher[-1]==" ":
        cipher= cipher[:-1]
    return cipher

def decode(ciphered_text):
    cipherednospace=ciphered_text.strip(" ")
    alphabet= "abcdefghijklmnopqrstuvwxyz"
    reversedalphabet= alphabet[::-1]
    numbers= "123456789"
    plaintext=""
    for char in cipherednospace:
        if char.lower() in alphabet:
            if char.isupper():
                newtext= alphabet[reversedalphabet.index(char.lower())]
                plaintext=plaintext+newtext
            else:
                newtext= reversedalphabet[alphabet.index(char)]
                plaintext=plaintext+newtext    
        elif char in numbers:
            plaintext=plaintext+char
        else:
            plaintext=plaintext
    return plaintext

choice= input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text= input("Type your message:\n")
if choice=="encode":
    print(encode(text))
elif choice=="decode":
    print(decode(text))