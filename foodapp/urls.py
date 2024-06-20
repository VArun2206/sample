from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('menu/',views.menu),
    path('about/',views.about),
    path('book/',views.book),
    path('login/',views.login),
]
