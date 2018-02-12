import sys

# TASK 1A: Caesar Cipher
# decrypt or encrypt. This parameter is used distinguish between the two modes of operation.

plainText = "DEFGHIJKLMNOPQRSTUVWXYZABC";
encrypt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
plainChar = list(plainText);
encryptChar = list(encrypt);

if len(sys.argv) == 3:
    operation = sys.argv[1];
    text = sys.argv[2];
    result=""

    if operation == "encrypt":
        for letter in text:
            result += encryptChar[plainChar.index(letter.upper())]
    elif operation == "decrypt":
        for letter in text:
            result += plainChar[encryptChar.index(letter.upper())]
    else:
        print ("Invalid Operation");

    print (result)
else:
    print ("Please provide valid arguments");
    print ("E.g : python caesar.py encrypt Hello");