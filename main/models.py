from django.db import models
from autoslug import AutoSlugField
from django.shortcuts import reverse
from django.conf import settings

class Cidade(models.Model):
    title = models.CharField(max_length=200)

    slug = AutoSlugField(populate_from="title")
    def __str__(self):
        return self.title

class Topic(models.Model):
    title = models.CharField(max_length=200)

    slug = AutoSlugField(populate_from="title")
    def __str__(self):
        return self.title

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from="title")
    image = models.CharField(max_length=400)
    descricao = models.TextField()
    endereco = models.TextField()
    servicos = models.TextField()
    detalhes = models.CharField(max_length=5)
    desde = models.CharField(max_length=5)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse("detail", kwargs={
            "slug":self.slug,
        })
class Comentario(models.Model):
    session_client = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    conteudo = models.TextField(max_length=420, default='')
    Local = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    def __str__(self):
        return self.conteudo