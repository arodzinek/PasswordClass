from crypt import crypt

"""
Rule #1: Keep it fun

Our goal is to learn how to open files.  Once we can open files we have all of 
the power required to *BREAK PASSWORDS*

Use your new found power for good!
"""


"""
Serious business ...
We're going to write a plaintext password, and an encrypted password
"""

passwords_of_good = ["burrito", "Burrito", "pickle", "cashew", "laser", "Python"]

file_plaintext = open("./my_new_passwords_plaintext.txt", "w")
file_encrypted = open("./my_new_passwords_encrypted.txt", "w")
# Something we're used to
print "word:\t\tencrypted\n"

for word in passwords_of_good:
    encrypted_result = word + "\t\t" + crypt(word, "salt")
    print encrypted_result
    file_plaintext.writelines(word + "\n")
    file_encrypted.writelines(crypt(word, "salt") + "\n")

# Close the file
file_plaintext.close()
file_encrypted.close()