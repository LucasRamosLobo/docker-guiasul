from django.contrib import admin
from .models import Topic, Recipe, Cidade, Comentario


admin.site.register(Recipe)
admin.site.register(Topic)
admin.site.register(Cidade)
admin.site.register(Comentario)