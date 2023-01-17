from django.urls import path
from .views import home, search, detail, RecipeCreate, comentar

urlpatterns = [
    path("", home, name="home"),
    path('cadastrar/', RecipeCreate.as_view(), name='cadastros'),
    path("search", search, name="search"),
    path("<slug>", detail, name="detail"),
    path('comentar/', comentar.as_view(), name='comentar'),
]