from django import forms

class userForm(forms.Form):
    name=forms.CharField(label="Name",widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    email=forms.EmailField(label="Email",widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    phone=forms.CharField(label="Contact",widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))