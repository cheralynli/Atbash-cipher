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

plain_text= input("Enter text to encode: ")
encoded_text= encode(plain_text)
print("Encoded text:", encoded_text)