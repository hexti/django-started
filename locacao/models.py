from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)


