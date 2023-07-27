from django import forms
from django.contrib.auth.forms import UserCreationForm,UsernameField,AuthenticationForm,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from .models import Customer

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': 'True', 'class':'form-control'}))
    password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'True', 'class':'form-control'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','locality','city','mobile','state','zipcode']
        widgets={
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'locality':forms.TextInput(attrs={'class': 'form-control'}),
            'city':forms.TextInput(attrs={'class': 'form-control'}),
            'mobile':forms.NumberInput(attrs={'class': 'form-control'}),
            'state':forms.Select(attrs={'class': 'form-control'}),
            'zipcode':forms.NumberInput(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super(CustomerProfileForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "姓名"
        self.fields['locality'].label = "地點"
        self.fields['city'].label = "城市"
        self.fields['mobile'].label = "手機"
        self.fields['state'].label = "國家"
        self.fields['zipcode'].label = "郵遞區號"

class MyPasswordChangeForm(PasswordChangeForm):
    old_password=forms.CharField(label='Old Password',widget=forms.PasswordInput(attrs={'autofocus':'True','autocomplete':'current password','class':'form-control'}))
    new_password1=forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'autocomplete':'current password','class':'form-control'}))
    new_password2=forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'autocomplete':'current password','class':'form-control'}))

class MyPasswordResetForm(PasswordResetForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1=forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'autocomplete':'current password','class':'form-control'}))
    new_password2=forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'autocomplete':'current password','class':'form-control'}))