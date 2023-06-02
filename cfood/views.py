from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Recipe
from django.db.models import Q
import os



# Create your views here.




def inicio(request):
    #"C:/Users/sarah/PycharmProjects/proyecto/proyecto/cfood/template/templateSusana/index.html"
    total_recipes = Recipe.objects.all().count()
    context = {
        "title": "Homepage",
        "total_recipes": total_recipes,
    }
    # Obtener la ruta absoluta del directorio del archivo views.py
    current_path = os.path.dirname(os.path.abspath(__file__))

    # Construir la ruta relativa al archivo de plantilla
    template_path = os.path.join(current_path, 'template', 'templateSusana', 'index.html')

    return render(request, template_path, context)


def index(request):
    context = {
        "title": "Bienvenido"
    }
    # Obtener la ruta absoluta del directorio del archivo views.py
    current_path = os.path.dirname(os.path.abspath(__file__))

    # Construir la ruta relativa al archivo de plantilla
    template_path = os.path.join(current_path, 'template', 'templateSusana', 'index.html')

    return render(request, template_path, context)


def registerpr(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, None)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.UserApp.username = form.cleaned_data.get('username')
            user.UserApp.email = form.cleaned_data.get('email')
            user.UserApp.password = form.cleaned_data.get('password')
            user.is_active = True
            user.save()
            print(user)
        else:
            print(form.errors)
    else:
        form = RegisterForm()
    context = { 'form' : form}
    return render(request,'./register/register.html', context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, None)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.username = form.cleaned_data.get('username')
            user.email = form.cleaned_data.get('email')
            user.set_password(form.cleaned_data.get('password'))
            user.is_active = True
            user.save()
            print("USUARIOOOOOOOOOOOOOOOO: ",user)
            return redirect('login ')
        else:
            print(form.errors)
    else:
        form = RegisterForm()
    context = { 'form' : form}
    return render(request,'./register/register.html', context)



def login2(request):
    if request.POST:
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        print(username, password, user)
        login(request,user)
        print("usuario", user)
        return redirect('home')
    else:
        form = LoginForm(request.POST)
        context = {'form': form}
        # Obtener la ruta absoluta del directorio del archivo views.py
        current_path = os.path.dirname(os.path.abspath(__file__))

        # Construir la ruta relativa al archivo de plantilla
        template_path = os.path.join(current_path, 'template', 'loguear.html')

        return render(request, template_path, context)

def search(request):
    recipes = Recipe.objects.all()

    if "search" in request.GET:
        query = request.GET.get("search")
        queryset = recipes.filter(Q(title__icontains=query))

    if request.GET.get("breakfast"):
        results = queryset.filter(Q(topic__title__icontains="breakfast"))
        topic = "breakfast"
    elif request.GET.get("lunch"):
        results = queryset.filter(Q(topic__title__icontains="lunch"))
        topic="lunch"
    elif request.GET.get("salads"):
        results = queryset.filter(Q(topic__title__icontains="salads"))
        topic="salads"
    elif request.GET.get("dinner"):
        results = queryset.filter(Q(topic__title__icontains="dinner"))
        topic="dinner"
    elif request.GET.get("dessert"):
        results = queryset.filter(Q(topic__title__icontains="dessert"))
        topic="dessert"
    elif request.GET.get("easy"):
        results = queryset.filter(Q(topic__title__icontains="easy"))
        topic="easy"
    elif request.GET.get("hard"):
        results = queryset.filter(Q(topic__title__icontains="hard"))
        topic="hard"

    total = results.count()

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
        "topic":topic,
        "page":page,
        "total":total,
        "query":query,
        "results":results,
    }
    return render(request, "search.html", context)

def detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    context = {
        "recipe":recipe,
    }
    return render(request, "detail.html", context)




def favourite_add3(request, id):
    receta = get_object_or_404(Recipe, id=id)
    if receta.favourites.filter(id=request.user.id).exists():
        receta.favourites.remove(request.user)
    else:
        receta.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

"""def favourite_add(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if request.method == 'POST':
        recipe.favourite.add(request.user)
    return render(request, 'favourite.html' % id)"""

def favourite_add(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if recipe.favourites.filter(id=request.user.id).exists():
        recipe.favourites.add(request.user)
    else:
        recipe.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

"""def favourite_list(request):
    receta = get_object_or_404(Recipe, id=id)
    new = receta.filter(favourites=request.user)
    return render(request,
                  'cfood/favourites.html',
                  {'new': new})"""

def favourite_list(request):
    new = Recipe.objects.filter(favourites=request.user)
    return render(request,
                  'favourite.html',
                  {'new': new})
def user_logout(request):
    logout(request)
    return redirect('index')


"""def favourite_list(request):
    new = Post.newmanager.filter(favourites=request.user)
    return render(request,
                    'accounts/favourites.html',
                    {'new': new})"""
