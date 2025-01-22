
from django.urls import path
from .views import *
urlpatterns = [
    path("register/", UserRegister.as_view(),name = 'user registrations'),
    path("login/", UserLogin.as_view(),name = 'user login'),
]
