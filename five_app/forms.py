from django import forms
from django.contrib.auth.models import User
from five_app.models import Userprofileinfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')
    
class Userprofileinfoform(forms.ModelForm):
    class Meta():
        model = Userprofileinfo
        fields = ('porfilefile_site', 'profile_image') #field = "__all__"


