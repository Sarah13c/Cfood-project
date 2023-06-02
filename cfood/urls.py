
from django.urls import path
from .views import inicio, search, detail, index
from . import views

urlpatterns = [

    path('login/',views.login2, name = 'login '),
    path('register/', views.register, name='register'),
    path('home/', views.inicio, name = "home"),
    path("search", search, name="search"),
    path("<slug>", detail, name="detail"),
    path("", index, name="index"),
    path('fav/<int:id>/', views.favourite_add, name='favourite_add'),
    path('favourite/', views.favourite_list, name='favourite_list'),
    path ('index/', views.user_logout, name= "user_logout"),

]