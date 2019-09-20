from django import forms
from django.forms import Form

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import DB,Author



class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password1', 'password2')

 
    def save(self, commit=True):
        user = super(SignupForm,self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user


class TextArea(forms.Form):
    text = forms.CharField(max_length=100)
    #msgField=forms.CharField(max_length=1000)
    class Meta:
        model = DB
        fields = ('text')

    def save(self, commit=True):
        ss = super(TextArea,self).save(commit=False)
        ss.text(self.cleaned_data['text'])
        #s_text.msgField(self.cleaned_data['msgField'])
class AuthorTextArea(forms.Form):
    text = forms.CharField(max_length=100)
    #msgField=forms.CharField(max_length=1000)
    class Meta:
        model = Author
        fields = ('text')

    def save(self, commit=True):
        ss = super(TextArea,self).save(commit=False)
        ss.text(self.cleaned_data['text'])