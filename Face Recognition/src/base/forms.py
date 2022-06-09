from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Student

class CreateUser(UserCreationForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'required':'',
            'name':'username',
            'id':'username',
            'type':'text',
            'class':'form-control',
            'placeholder':'Username',
            'max-length':'150',
            'max-length':'50'
        })
        self.fields["email"].widget.attrs.update({
            'class':'form-control',
            'required':'',
            'name':'email',
            'id':'email',
            'type':'email',
            'placeholder':'Email'    
            
        })

        self.fields["password1"].widget.attrs.update({
            'class':'form-control',
            'required':'',
            'name':'password',
            'id':'password',
            'type':'password',
            'placeholder':'Password',
            'max-length':'150',
            'max-length':'50'    
        })
        self.fields["password2"].widget.attrs.update({
            'class':'form-control',
            'required':'',
            'name':'password2',
            'id':'password2',
            'type':'password2',
            'placeholder':'Password2',
            'max-length':'150',
            'max-length':'50'    
        })
    class Meta:
        model=User
        fields=['username', 'email', 'password2', 'password2']  

# class editstudent(forms.ModelForm):

#         class Meta:
#             model=Student
#             fields='__all__'