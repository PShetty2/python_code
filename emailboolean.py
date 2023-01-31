def checklength(s):

    if len(s) >=10 and len(s) <=20:
        return True
    else:
        return False

def check_char(s):
    if s.index('@'):
        return True
    else:
        return False


email = input("enter email: ")
print(checklength(email) and check_char(email))