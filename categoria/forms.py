from django import forms
from categoria.models import Categoria

class CategoriaCreateForm(forms.ModelForm):
    class Meta: 
        model = Categoria
        fields = ['categoria']