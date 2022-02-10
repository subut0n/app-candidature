

def isAsciiNumber(mystr):
    mylist = ['0','1','2','3','4','5','6','7','8','9']
    for c in mystr:
        if c not in mylist:
            return False
    return True