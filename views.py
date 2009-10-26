from django.contrib.auth import REDIRECT_FIELD_NAME
from email_auth.forms import EmailAuthenticationForm


def login(request, template_name='registration/login.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=EmailAuthenticationForm):
    from django.contrib.auth.views import login
    return login(request, template_name, redirect_field_name, authentication_form)