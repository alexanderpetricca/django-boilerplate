from django.contrib.auth import forms as auth_forms
from django import forms

from .models import CustomUser


# Admin Forms

class CustomUserAdminCreateForm(auth_forms.UserCreationForm):
    """Form used to create a user in the admin backend"""

    class Meta:
        model = CustomUser
        fields = ('__all__')


class CustomUserAdminChangeForm(auth_forms.UserChangeForm):
    """Form used to update a user in the admin backend"""

    class Meta:
        model = CustomUser
        fields = ('__all__')



# Custom Auth Forms
        
class CustomLoginForm(auth_forms.AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Email'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'


class CustomSignupForm(auth_forms.UserCreationForm):

    class Meta:
        model = CustomUser
        fields = (
            'email',
        )


class CustomPasswordResetForm(auth_forms.PasswordResetForm):

    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))


class CustomSetPasswordForm(auth_forms.SetPasswordForm):

    def __init__(self, *args, **kwargs):
        super(CustomSetPasswordForm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].widget = forms.PasswordInput(attrs={'placeholder': 'New Password'})
        self.fields['new_password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Confirm New Password'})


class CustomPasswordChangeForm(auth_forms.PasswordChangeForm):
    
    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs['placeholder'] = 'Old Password'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'New Password'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'New Password (again)'