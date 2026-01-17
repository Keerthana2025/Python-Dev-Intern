//EMAIL VALIDATION

def validate_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False

email = input("Enter email address: ")

if validate_email(email):
    print("Valid email address")
else:
    print("Invalid email address")
