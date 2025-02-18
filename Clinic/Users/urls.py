from django.urls import path
from . import views

app_name = "Users"

urlpatterns = [
    path("register/", views.registerUser, name="register_user"),
    path("login/", views.loginUser, name="login_user"),
    path("logout/", views.logoutUser, name="logout_user")
]