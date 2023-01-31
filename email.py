email =input("Enter an email message: ")
index = email.index('@')
if len(email) >= 10 and len(email) <= 20:
    print("The email is valid.")
else:
    print("The email is not valid.")



