from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.contrib.auth import authenticate
import re
from .models import CustomUser
class CustomUserCreationForm(UserCreationForm):
    
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Contraseña',
                'required': True,
                'pattern': r'^(?=.*\d)(?=.*[A-Z])(?=.*[!@#$%^&*()_+{}|:"<>?[\];\',./`~\\-])[A-Za-z\d!@#$%^&*()_+{}|:"<>?[\];\',./`~\\-]{8,}$',
                'title': 'La contraseña debe contener al menos 8 caracteres, 1 número, 1 letra mayúscula y 1 carácter especial.',
                'autocomplete': 'new-password',
            }
        )
    )
    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirmar contraseña',
                'required': True,
                'pattern': r'^(?=.*\d)(?=.*[A-Z])(?=.*[!@#$%^&*()_+{}|:"<>?[\];\',./`~\\-])[A-Za-z\d!@#$%^&*()_+{}|:"<>?[\];\',./`~\\-]{8,}$',
                'title': 'La contraseña debe contener al menos 8 caracteres, 1 número, 1 letra mayúscula y 1 carácter especial.',
                'autocomplete': 'new-password',
            }
        )
    )
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'surname', 'control_number', 'age', 'tel', 'password1', 'password2']
        widgets = {
            'email': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Correo electrónico',
            'required': True,
            'pattern': r'^[a-zA-Z0-9._%+-]+@utez\.edu\.mx$',
            'title': 'Debes ingresar un correo de la UTEZ',
            }),
            'name': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre',
            'required': True,
            'title': 'Ingresa tu nombre',
            }),
            'surname': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Apellido',
            'required': True,
            'title': 'Ingresa tu apellido',
            }),
            'control_number': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Número de control',
            'pattern': r'^\d{5}TN\d{3}$',
            'required': True,
            'title': 'Ingresa tu número de control',
            }),
            'age': forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Edad',
            'required': True,
            'title': 'Ingresa tu edad',
            }),
            'tel': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Teléfono',
            'required': True,
            'pattern': r'^\d{10}$',
            'title': 'El número de teléfono debe de ser de 10 números',
            }),
        }
        validators = {
            'email': [MaxLengthValidator(254), MinLengthValidator(5)],
            'name': [MaxLengthValidator(100), MinLengthValidator(2)],
            'surname': [MaxLengthValidator(100), MinLengthValidator(2)],
            'control_number': [MaxLengthValidator(20), MinLengthValidator(10)],
            'tel': [MaxLengthValidator(15), MinLengthValidator(10)],
        }

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not re.match(r"^[a-zA-Z0-9._%+-]+@utez\.edu\.mx$", email):
            raise forms.ValidationError("Debes usar un correo de la UTEZ.")
        return email
    
    def clean_control_number(self):
        control_number = self.cleaned_data.get("control_number")
        if not re.match(r"^\d{5}TN\d{3}$", control_number):
            raise forms.ValidationError("Formato incorrecto (ejemplo 20223TN085).")
        return control_number

    def clean_tel(self):
        tel = self.cleaned_data.get("tel")
        if not tel.isdigit() or len(tel) != 10:
            raise forms.ValidationError("El teléfono debe contener exactamente 10 dígitos.")
        return tel

    def clean_age(self):
        age = self.cleaned_data.get("age")
        if age < 0 or age > 120:
            raise forms.ValidationError("La edad debe estar entre 0 y 120 años.")
        return age
    
    def clean_password(self):
        password = self.cleaned_data.get("password")
        if not re.match(r'^(?=.*\d)(?=.*[A-Z])(?=.*[!@#$%^&*()_+{}|:"<>?[\];\',./`~\\-])[A-Za-z\d!@#$%^&*()_+{}|:"<>?[\];\',./`~\\-]{8,}$', password):
            raise forms.ValidationError("La contraseña debe contener al menos 8 caracteres, 1 número, 1 letra mayúscula y 1 carácter especial.")
        return password
    
    def clean(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Las contraseñas no coinciden.")

        return password1, password2

class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Correo electrónico",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'ejemplo@utez.edu.mx',
            'required': True
        }),
        max_length=254,
        min_length=5
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña',
            'required': True
        }),
        min_length=8,
        max_length=128
    )
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Usuario o contraseña incorrectos.")
        return cleaned_data