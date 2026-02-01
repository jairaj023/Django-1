from django import forms

from myAPp.models import Register

class registerForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = "__all__"
        widgets = {
            'fullname' : forms.TextInput(
                attrs={"placeholder" : "Enter fullname", "class" : "mycss"}
            ),
            'email' : forms.EmailInput(
                attrs={} 
            ),
            'password' : forms.PasswordInput(
                
            )
        }