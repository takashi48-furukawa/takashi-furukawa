from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, UserProfile

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=150, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    birthday = forms.DateField(required=True)
    password1 = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    password2 = forms.CharField(label='パスワード再入力', widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'birthday', 'password1', 'password2')

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('パスワードが一致しません')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
            UserProfile.objects.create(
                user=user,
                first_name=user.first_name,
                last_name=user.last_name,
                birthday=user.birthday,
            )
        return user

class CustomUserChangeForm(UserChangeForm):
    username = forms.CharField(max_length=150, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'birthday', 'is_active', 'is_staff')

    def save(self, commit=True):
        user = super().save(commit=False)
       
        if commit:
            user.save()
        return user
