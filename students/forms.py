from django import forms
from django.contrib.auth.models import User
from .models import Student, Group, Club, Profile


class StudentForm(forms.ModelForm):
    clubs = forms.ModelMultipleChoiceField(
        queryset=Club.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Кружки"
    )
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "age", "group", "clubs"]
        labels = {"first_name": "Имя", "last_name": "Фамилия", "age": "Возраст", "group": "Группа"}


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Подтвердите пароль")
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        labels = {"username": "Имя пользователя", "email": "Email"}
    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password") != cleaned_data.get("confirm_password"):
            raise forms.ValidationError("Пароли не совпадают!")
        return cleaned_data


class ProfileForm(forms.Form):
    display_name = forms.CharField(
        max_length=100, required=False, label="Отображаемое имя",
        widget=forms.TextInput(attrs={'placeholder': 'Ваше имя для отображения'})
    )
    username = forms.CharField(
        max_length=150, label="Имя пользователя (логин)",
        widget=forms.TextInput(attrs={'placeholder': 'Логин'})
    )
    email = forms.EmailField(
        required=False, label="Email",
        widget=forms.EmailInput(attrs={'placeholder': 'email@example.com'})
    )
    avatar = forms.ImageField(required=False, label="Фото профиля")
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Оставьте пустым, чтобы не менять'}),
        required=False, label="Новый пароль"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Повторите новый пароль'}),
        required=False, label="Подтвердите пароль"
    )
    captcha_answer = forms.IntegerField(label="Ответ на вопрос", widget=forms.NumberInput(attrs={'placeholder': '?'}))

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get("new_password")
        p2 = cleaned_data.get("confirm_password")
        if p1 and p1 != p2:
            raise forms.ValidationError("Пароли не совпадают!")
        return cleaned_data
