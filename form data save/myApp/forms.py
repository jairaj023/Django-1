from django import forms

class Register(forms.Form):
    Fullname = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder" : "Enter your fullname..."}
        )
    )
    Email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"placeholder" : "Enter your email..."}
        )
    )
    Password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder" : "Enter your password..."}
        )
    )
