<<<<<<< HEAD
from App.models import Users
=======

>>>>>>> 1f59a014b846477a57cac5fbe8a2566ec5b79be9

def isAsciiNumber(mystr):
    mylist = ['0','1','2','3','4','5','6','7','8','9']
    for c in mystr:
        if c not in mylist:
            return False
<<<<<<< HEAD
    return True


list_mail = [ c.email_address
          
               for c in Users.query]
=======
    return True
>>>>>>> 1f59a014b846477a57cac5fbe8a2566ec5b79be9
