from django import forms
from django.contrib.auth.models import User
from .models import Post

'''
class UserSignUpForm(UserCreationForm):
    stegtype = forms.CharField()
    plaintext = forms.CharField(max_length=100)
    hiddentext = forms.CharField(max_length=35)


    class Meta:
        model = User
        fields = ['username','email','password1','password2']
'''

class TextForm(forms.Form):
    #stegtype = forms.CharField(max_length=10, widget=forms.HiddenInput(), initial='Text')
    plaintext = forms.CharField(label='Plain Text', max_length=100)
    hiddentext = forms.CharField(label='Hidden Text', max_length=35)    

    class Meta:
        model = Post

#ImageField
#FileField