from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='index'),
    path('login',views.Login,name='login'),
    path('register',views.register,name='register'),
    path('terms',views.terms,name='terms'),
]
