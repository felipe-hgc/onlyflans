import re

from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField

from web.models import ContactForm


class ContactFormForm(forms.Form):
    customer_email = forms.CharField(label='Correo')
    customer_name = forms.CharField(max_length=64, label='Nombre')
    message = forms.CharField(label="Mensaje")

    def clean_customer_email(self):
        data = self.cleaned_data['customer_email']
        regex = re.compile('^[a-zA-Z0-9_\.]+@[a-zA-Z]+\.(com|cl)$')
        if regex.match(data):
            return data
        else:
            raise ValidationError("Debes ingresar un correo válido")



class ContactFormModelForm(ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_name', 'customer_email', 'message']

    def clean_customer_email(self):
        data = self.cleaned_data['customer_email']
        regex = re.compile('^[a-zA-Z0-9_\.]+@[a-zA-Z]+\.(com|cl)$')
        if regex.match(data):
            return data
        else:
            raise ValidationError("Debes ingresar un correo válido")
