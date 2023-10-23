from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views


app_name = "farmer"

urlpatterns = [
    path("signup",views.signup, name="signup"),
    path("signin",views.signin, name="signin"),
    path("logout", LogoutView.as_view(next_page="farmer:signin"), name="logout"),
    path("<int:id>",views.index, name="index"),
]