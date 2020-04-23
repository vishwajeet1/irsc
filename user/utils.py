import re
import hashlib


def passValid(password):
    flag = 0
    while True:
        if (len(password) < 8):
            flag = -1
            msg = "Password length must be greater than 7 char"
            break
        elif not re.search("[a-z]", password):
            flag = -1
            msg = "Password must contain atleast one lowercase char"
            break
        elif not re.search("[A-Z]", password):
            flag = -1
            msg = "Password must contain atleast one uppercase char"
            break
        elif not re.search("[0-9]", password):
            flag = -1
            msg = "Password must contain atleast one digit"
            break
        elif not re.search("[_@$]", password):
            flag = -1
            msg = "Password must contain atleast one special char"
            break
        elif re.search("\s", password):
            flag = -1
            msg = "unkown error"
            break
        else:
            flag = 0
            return False

    if flag == -1:
        return msg


def emailValid(email):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if(re.search(regex, email)):
        return True
    else:
        return False


def hashfun(password):
    return hashlib.sha256(password.encode()).hexdigest()
