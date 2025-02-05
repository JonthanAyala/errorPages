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
                    'type': 'text',
                    'name': 'control_number',
                    'class': 'form-control',
                    'placeholder': 'Matrícula',
                    'maxlength': '20',
                    'required': '',
                    'id': 'id_control_number',
                    'pattern': '^\d{10}$',
                    'title': 'El numero de control debe tener exactamente 10 dígitos.',
                }
            ),
            'age': forms.NumberInput(
                attrs={
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
                    'type': 'password',
                    'name': 'password1',
                    'class': 'form-control',
                    'placeholder': 'Contraseña',
                    'autocomplete': 'new-password',
                    'aria-describedby': 'id_password1_helptext',
                    'id': 'id_password1',
                }
            ),
            'password2': forms.PasswordInput(
                attrs={
                    'type': 'password',
                    'name': 'password2',
                    'class': 'form-control',
                    'placeholder': 'Confirmar contraseña',
                    'autocomplete': 'new-password',
                    'aria-describedby': 'id_password2_helptext',
                    'id': 'id_password2',
                }
            ),
        }


class CustomUserLoginForm(AuthenticationForm):
    pass

