from .models import Auth

def isuser(email):
    for dt in Auth.objects.all():
        if email== dt.email:
            return dt.password
        
    return False
