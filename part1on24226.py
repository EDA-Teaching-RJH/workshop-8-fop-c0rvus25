'''
email = input("What's your email? ").strip()
username, domain = email.split("@")
if username and domain.endswith(".ac.uk"):
 print("Valid")
else:
 print("Invalid")

email = input("What's your email? ").strip()
import re
if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.ac.uk$", email):
    print("Valid") 
else:
 print("Invalid")

import re
phone = input("Please enter your phone number: ")
if re.search(r"^07\d{9}$", phone):
    print("Valid")
else:
    print("Invalid")
'''

import re
Student_ID = input("Please enter your Student ID number: ")
if re.search(r"^[a-zA-Z]{4}\d{4}$", Student_ID):
    print("Valid")
else:
    print("Invalid")

#i get it now 