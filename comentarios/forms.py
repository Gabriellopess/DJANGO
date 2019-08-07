from django import forms
from comentarios.models import Comentarios

class ComentariosCreateForm(forms.ModelForm):
    class Meta: 
        model = Comentarios
        fields = ['comentario','post']
