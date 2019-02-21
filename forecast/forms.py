import re
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UniqueEmailField(forms.EmailField):
    """
        * An EmailField which is valid if no User has that email.
    """

    def validate(self, value):
        super(forms.EmailField, self).validate(value)
        try:
            User.objects.get(email=value)
            raise forms.ValidationError("Email already exists")
        except User.MultipleObjectsReturned:
            raise forms.ValidationError("Email already exists")
        except User.DoesNotExist:
            pass


class ExtendedUserCreationForm(UserCreationForm):
    """
        * extends the UserCreationForm

        * Adds an email field, which uses the custom UniqueEmailField,
          Nothing will be committed if the user exists.

        * the username is the email
    """
    username = forms.CharField(required=False, max_length=30)
    email = UniqueEmailField(required=True, label='Email address')

    def __init__(self, *args, **kwargs):
        """
            * Changes the order of fields, and removes the username field.
        """
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = ['email', 'password1', 'password2']

    def clean(self, *args, **kwargs):
        """
            * user cleanup
            * setting username = email
        """
        cleaned_data = super(UserCreationForm, self).clean(*args, **kwargs)
        if cleaned_data.get('email', ''):
            cleaned_data['username'] = cleaned_data['email']
        return cleaned_data

    def save(self, commit=True):
        """
            * Saves the email after the normal save is complete.
        """
        user = super(UserCreationForm, self).save(commit)
        if user:
            user.email = self.cleaned_data['email']
            user.set_password(self.cleaned_data['password1'])
            if commit:
                user.save()
        return user
