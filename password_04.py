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

f = open("./my_new_passwords_combined.txt", "w")

# Something we're used to
print "word:\t\tencrypted\n"

for word in passwords_of_good:
    encrypted_result = word + "\t\t" + crypt(word, "salt")
    print encrypted_result
    f.writelines(word + ";" + crypt(word, "salt") + "\n")

# Close the file
f.close()


"""
Take that and rewind it back!

Now that we've grabbed a file, let's open it read only and display the results.
Not just display the results, let's display it like an adult!
"""

read_this_file = open("./my_new_passwords_combined.txt")  # tricky!

for line in read_this_file:
    (plaintext, encrypted) = line.split(";")
    print "plaintext: " + plaintext + "\t encrypted: " + encrypted

read_this_file.close()