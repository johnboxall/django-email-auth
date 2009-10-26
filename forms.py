from django.contrib.auth import authenticate
from django import forms


class EmailAuthenticationForm(forms.Form):
    """
    Copy of AuthenticationForm with a few fields changed.
    http://code.djangoproject.com/browser/django/trunk/django/contrib/auth/forms.py
    
    """
    email = forms.CharField(label="Email", max_length=60)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    
    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super(EmailAuthenticationForm, self).__init__(*args, **kwargs)
        
    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            self.user_cache = authenticate(email=email, password=password)
            if self.user_cache is None:
                raise forms.ValidationError("Please enter a correct email and password. Note that both fields are case-sensitive.")
            elif not self.user_cache.is_active:
                raise forms.ValidationError("This account is inactive.")

        if self.request:
            if not self.request.session.test_cookie_worked():
                raise forms.ValidationError("Your Web browser doesn't appear to have cookies enabled. Cookies are required for logging in.")
            
            # For post processing, it is helpful to update the availible user on the request obj..
            if self.get_user() is not None:
                self.request.user = self.get_user()

        return self.cleaned_data

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache