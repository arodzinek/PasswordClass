from crypt import crypt

"""
Rule #1: Keep it fun

Our goal is to learn how to open files.  Once we can open files we have all of 
the power required to *BREAK PASSWORDS*

Use your new found power for good!
"""


"""
Crypt takes 2 arguments, the password and the salt.
The statement below will print the result of encrypting the password "things" 
the salt "salt"
"""
print crypt("things", "salt")
