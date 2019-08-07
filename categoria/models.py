from django.db import models

# Create your models here.
class Categoria(models.Model):
    categoria = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f'Categoria: {self.categoria}'
    