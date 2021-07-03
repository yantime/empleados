from django import forms
from django.forms import fields
from .models import Empleado

class EmpleadoForm(forms.ModelForm):

    class Meta:
        model=Empleado
        fields='__all__'