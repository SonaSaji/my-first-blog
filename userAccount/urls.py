from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name ='home'),
    path('index/', views.index, name ='index'),
    path('signup/', views.signup, name ='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout')
]