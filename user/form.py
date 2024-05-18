from django import forms
from .models import CreateUser

class CreateUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CreateUser
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'image']


    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user





class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CreateUser
        fields = ['username', 'email', 'first_name', 'last_name', 'image']
