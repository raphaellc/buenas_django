from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=45)
    dt_nasc = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.nome