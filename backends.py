from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend

class EmailBackend(ModelBackend):
    """
    Authenticate user by email. 
    http://code.djangoproject.com/browser/django/trunk/django/contrib/auth/backends.py
    
    """
    def authenticate(self, email=None, password=None):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None
        if user.check_password(password):
            return user