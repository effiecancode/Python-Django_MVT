from django.shortcuts import render, redirect
from .forms import RegistrationForm

def register_user(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("Accounts:login")

    form = RegistrationForm()
    return render(request, "Accounts/register_user.html", {"form": form, "title":"register"})


# Create your views here.
