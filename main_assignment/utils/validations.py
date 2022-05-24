import re

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
password_regex = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$")



def emailvalidation(input_email):
    if re.fullmatch(email_regex, input_email):
        return True
    else:
        print("Invalid email id")
        return False


def phonenumbervalidation(input_phone_number):
    if len(input_phone_number) == 10:
        return True
    else:
        print("Invalid phone number")
        return False

def passwordvalidation(input_password):
    if re.search(password_regex, input_password):
        return True
    else:
        print("Password Should contain One Capital Letter, One Number, Special Character, Length Should be 8-16")
        return False

class Validation:
    pass
