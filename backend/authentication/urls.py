from django.urls import path, include
from .views import authView, Home
urlpatterns = [
    path("", Home, name="home"),
    path("signup/", authView, name="authView"),
    path("accounts/", include("django.contrib.auth.urls"))
]