from django.urls import path
from django.contrib.auth import views
from django.contrib.auth.views import LoginView

from . import views


# app_name = "consumer"

urlpatterns = [
    path("create_consumer_user/",views.create_consumer_user, name="create_consumer_user"),
    path("consumer_login/", views.consumer_login, name="consumer_login"),
    path("consumer_logout/", views.consumer_logout, name='consumer_logout'),
    path('home/', views.home, name='home'),
]