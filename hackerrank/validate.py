import re
def fun(s):
    # return True if s is a valid email, else return False
    if re.search(r'^[\w\d-]+@[A-Za-z0-9]+\.\w?\w?\w$',s):
        return True
    else:
        return False
