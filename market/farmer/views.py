from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import FarmerRegistrationForm, FarmerLoginForm
from .models import Product, FarmerUser


def signup(request):
    if request.method == 'POST':
        form = FarmerRegistrationForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                form.save()
            return redirect("farmer:signin")
    else:
        form = FarmerRegistrationForm()

    return render(request, 'farmer/signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = FarmerLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            # print(user)
            if user is not None:
                login(request, user)
                return redirect('farmer:index')
            else:
                return render(request, 'farmer/signin.html', {'form': form, 'error_message': 'Invalid email or password'})
    else:
        form = FarmerLoginForm()

    return render(request, 'farmer/signin.html', {'form': form})


@login_required
def index(request, id):
    
    products = Product.objects.filter_by(farmer_user_id=id)

    return render(request, "farmer/index.hrml", {"products":products})


