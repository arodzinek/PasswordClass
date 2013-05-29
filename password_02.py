from crypt import crypt

"""
Rule #1: Keep it fun

Our goal is to learn how to open files.  Once we can open files we have all of 
the power required to *BREAK PASSWORDS*

Use your new found power for good!
"""


"""
Make it rain file descriptors!

Open the file, "a" means "append".  This will also create a file if one does 
not already exist.
"""
f = open("./my_new_passwords.txt", "a")

#  Write it out
f.write("Hello World\n")

# Close the file
f.close()