from django.shortcuts import render, get_object_or_404
from .models import Recipe
from .models import Comentario
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required



class RecipeCreate(CreateView):
    
    model = Recipe
    fields = ['title','image','descricao','endereco','servicos','detalhes','desde','topic','cidade']
    template_name = 'Base2.html'
    success_url = reverse_lazy('home')

def home(request):
    total_recipes = Recipe.objects.all().count()
    recipes = Recipe.objects.all()
    inter2=[]
    for recipe in recipes:
        inter2.append(recipe)
    context = {
        "title":"Homepage",
        "total_recipes":total_recipes,
        "recipes":recipes,
        "inter2":inter2,
    }  
        
    return render(request, "home.html", context)

class comentar(CreateView):
    
    model = Comentario
    fields = ['conteudo','Local','session_client']
    template_name = 'base2.html'
    success_url = reverse_lazy('home')

def search(request):
    recipes = Recipe.objects.all()
    inter = []
    results1=[]
    results2=[]
    results3=[]
    results4=[]
    results5=[]
    results6=[]
    results7=[]
    results8=[]
    results9=[]
    results10=[]
    results=[]
    b = False

    if "search" in request.GET:
        query = request.GET.get("search")
        queryset = recipes.filter(Q(title__icontains=query))
        results = recipes.filter(Q(title__icontains=query))
        topic = ''
        cidade =''
    
    if request.GET.get("Itacaré"):
        results1 = queryset.filter(Q(cidade__title__icontains="Itacaré"))
        cidade = "Itacaré"
        b = True
    if request.GET.get("Ilhéus"):
        results2 = queryset.filter(Q(cidade__title__icontains="Ilhéus"))
        cidade="Ilhéus"
        b = True    
    if request.GET.get("Bares"):
        results3 = queryset.filter(Q(topic__title__icontains="Bares"))
        topic = "Bares"
        b = True  
    if request.GET.get("Restaurantes"):
        results4 = queryset.filter(Q(topic__title__icontains="Restaurantes"))
        topic="Restaurantes"
        b = True 
    if request.GET.get("Eventos"):
        results5 = queryset.filter(Q(topic__title__icontains="Eventos"))
        topic="Eventos"
        b = True 
    if request.GET.get("Hospedagens"):
        results6 = queryset.filter(Q(topic__title__icontains="Hospedagens"))
        topic="Hospedagens"
        b = True 
    if request.GET.get("Passeios Turísticos"):
        results7 = queryset.filter(Q(topic__title__icontains="Passeios Turísticos"))
        topic="Passeios Turísticos"
        b = True 
    if request.GET.get("Praças"):
        results8 = queryset.filter(Q(topic__title__icontains="Praças"))
        topic="Praças"
        b = True 
    if request.GET.get("Feiras"):
        results9 = queryset.filter(Q(topic__title__icontains="Feiras"))
        topic="Feiras"
        b = True 
    if request.GET.get("Comércios"):
        results10 = queryset.filter(Q(topic__title__icontains="Comércios"))
        topic="Comércios"
        b = True 

    
    
    a = False
    for x in recipes:
        for y in results1:
            if x == y:
                if x not in inter:
                    inter.append(x)
                    a = True
        for y in results2:
            if x == y:
               if x not in inter:
                    inter.append(x)
                    a = True
        for y in results3:
            if x == y:
                if x not in inter:
                    inter.append(x)
                    a = True
        for y in results4:
            if x == y:
               if x not in inter:
                    inter.append(x)
                    a = True
        for y in results5:
            if x == y:
               if x not in inter:
                    inter.append(x)
                    a = True
        for y in results6:
            if x == y:
                if x not in inter:
                    inter.append(x)
                    a = True
        for y in results7:
            if x == y:
               if x not in inter:
                    inter.append(x)
                    a = True
        for y in results8:
            if x == y:
               if x not in inter:
                    inter.append(x)
                    a = True
        for y in results9:
            if x == y:
                if x not in inter:
                    inter.append(x)
                    a = True
        for y in results10:
            if x == y:
               if x not in inter:
                    inter.append(x)
                    a = True
          
    if a == False and b == False:
        inter = results
                
    
    #paginate results
    paginator = Paginator(results, 3)
    page = request.GET.get("page")
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)

    context = {
        "cidade":cidade,
        "topic":topic,
        "page":page,
        "results2":results2,
        "results3":results3,
        "results4":results4,
        "results5":results5,
        "results6":results6,
        "results7":results7,
        "results8":results8,
        "results9":results9,
        "results10":results10,
        "query":query,
        "results":results,
        "results1":results1,
        "inter":inter,
   
       
    }
    return render(request, "search.html", context)

def detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    context = {
        "recipe":recipe,
    }
    return render(request, "detail.html", context)



