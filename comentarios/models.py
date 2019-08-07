from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comentarios(models.Model):
    post = models.ForeignKey("posts.post", verbose_name= 'post', on_delete = models.CASCADE)
    comentario = models.TextField(verbose_name = "comentario")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentarios {self.pk} | Author {self.autor} | Created at {self.created_at}'

