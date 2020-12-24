# Hopefully you won't need this, but Paiza is in beta, so it might accidentally delete all of the code. If it does, just copy everything below this and paste it there.
# coding: utf-8
# Disclaimer and credit:
# The code herein is for demonstration purposes only and is not intended for use as a profit vehicle, or to secure any other compensation.
# This code was modified from https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_quick_guide.htm
# No credit is taken for its authorship, nor claim to its copyright.
# If you haven't been able to find a suitable translation service for the login, may I suggest the following: https://web.expasy.org/translate/

def encrypt(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        # Encrypt lowercase characters in plain text. This means that you did it wrong.
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

###########################################################################################################################################################################
##### I realize that this is kind of a weird Christmas card, having to jump through all of these hoops and all. Here's an ASCII santa. I hope it helps:    *<[:{)     #####
###########################################################################################################################################################################

text = "ENTER YOUR CODE HERE"
s = 4

print ("Congratulations on finding the token! Assuming you translated it correctly, your password is as follows. Please take it to https://www.quandarystudio.com/easteregg.")
print (encrypt(text,s))
