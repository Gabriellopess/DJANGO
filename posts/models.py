#This file means the 'data base' of our project. Where we keep the informations taken
#located in for future uses.

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class post(models.Model):
    autor = models.ForeignKey("users.User", verbose_name='autor', on_delete=models.CASCADE)
    categoria = models.ForeignKey("categoria.Categoria", verbose_name='categoria', on_delete=models.CASCADE)
    texto = models.TextField(verbose_name='texto')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Post {self.pk} | Author {self.autor} | Created at {self.created_at}'

    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'



