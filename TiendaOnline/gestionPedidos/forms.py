#Este archivo se crea manualmente
#Por cada formulario se crea una clase

from django import forms

class FormularioContacto(forms.Form):
    asunto = forms.CharField()
    email = forms.EmailField()
    mensaje = forms.CharField()



