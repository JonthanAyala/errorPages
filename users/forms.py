import re
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'surname', 'control_number', 'age', 'tel', 'password1', 'password2']
        widgets = widgets = {
            'email': forms.EmailInput(
                attrs={
                    'type': 'email',
                    'name': 'email',
                    'class': 'form-control',
                    'placeholder': 'Correo electrónico',
                    'required': True,
                    'maxlength': '254',
                    'autofocus': '',
                    'required': '',
                    'id': 'id_email',
                    'pattern': '^[a-zA-Z0-9._%+-]+@utez\.edu\.mx$',
                    'title': 'El correo electrónico debe ser de UTEZ (@utez.edu.mx).',
                }
            ),
            'name': forms.TextInput(
                attrs={


                    
                    'required': True,
                    'type': 'text',
                    'name': 'name',
                    'class': 'form-control',
                    'placeholder': 'Nombre',
                    'maxlength': '100',
                    'required': '',
                    'id': 'id_name',
                }
            ),
            'surname': forms.TextInput(
                attrs={
                    'required': True,
                    'type': 'text',
                    'name': 'surname',
                    'class': 'form-control',
                    'placeholder': 'Apellido',
                    'maxlength': '100',
                    'required': '',
                    'id': 'id_surname',
                }
            ),
            'control_number': forms.TextInput(
                attrs={
                    'required': True,
                    'type': 'text',
                    'name': 'control_number',
                    'class': 'form-control',
                    'placeholder': 'Matrícula',
                    'maxlength': '20',
                    'required': '',
                    'id': 'id_control_number',
                    'pattern': '^\d{5}TN\d{3}$',
                    'title': 'El numero de control debe tener exactamente 10 dígitos.',
                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'required': True,
                    'type': 'number',
                    'name': 'age',
                    'class': 'form-control',
                    'placeholder': 'Edad',
                    'min': '0',
                    'required': '',
                    'id': 'id_age',
                }
            ),
            'tel': forms.NumberInput(
                attrs={
                    'required': True,
                    'type': 'text',
                    'name': 'tel',
                    'class': 'form-control',
                    'placeholder': 'Teléfono',
                    'maxlength': '15',
                    'required': '',
                    'id': 'id_tel',
                    'pattern': '^\d{10}$',
                    'title': 'El teléfono debe tener exactamente 10 dígitos.',
                }
            ),
            'password1': forms.PasswordInput(
                attrs={
                    'required': True,
                    'type': 'password',
                    'name': 'password1',
                    'class': 'form-control',
                    'placeholder': 'Contraseña',
                    'autocomplete': 'new-password',
                    'pattern': '^(?=.*\d)(?=.*[A-Z])(?=.*[!#$%&?])[A-Za-z\d!#$%&?]{8,}$',
                    'aria-describedby': 'id_password1_helptext',
                    'id': 'id_password1',
                }
            ),
            'password2': forms.PasswordInput(
                attrs={
                    'required': True,
                    'type': 'password',
                    'name': 'password2',
                    'class': 'form-control',
                    'placeholder': 'Confirmar contraseña',
                    'autocomplete': 'new-password',
                    'pattern': '^(?=.*\d)(?=.*[A-Z])(?=.*[!#$%&?])[A-Za-z\d!#$%&?]{8,}$',
                    'aria-describedby': 'id_password2_helptext',
                    'id': 'id_password2',
                }
            ),
        }


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
    name = forms.CharField(
        label="Nombre",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre',
            'required': True
        }),
        max_length=100,
        min_length=2
    )
    surname = forms.CharField(
        label="Apellido",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Apellido',
            'required': True
        }),
        max_length=100,
        min_length=2
    )
    control_number = forms.CharField(
        label="Número de control",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '20223TN073',
            'required': True
        }),
        max_length=20,
        min_length=10
    )

