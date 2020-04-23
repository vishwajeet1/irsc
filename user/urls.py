from django.urls import path
from .views import sign, login

urlpatterns = [
    path('', sign, name="sign"),
    path('login', login, name="login"),
]
