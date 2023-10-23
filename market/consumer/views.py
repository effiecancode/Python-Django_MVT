from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib.auth import logout, authenticate, login
import json

# from .forms import ConsumerUserForm, ConsumerLoginForm
from .CreateConsumerAccount import CreateConsumerAccount


def create_consumer_user(request):
    """
        Client sign up functional view:
        takes a number of details from client_signup form and posts them, creating a user account.
    """
    print('create user')
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            if password1 == password2:
                account_creator = CreateConsumerAccount()  # Create an instance
                res = account_creator.save_client_account(username, email, password1)
            # if password1 == password2:
            #     res = CreateConsumerAccount.save_client_account(
            #         '',username, email, password1)
            #     auth_user = authenticate(
            #         request, email=email, password=password1)
            #     login(request, auth_user)

                return redirect('home')
            else:
                return HttpResponse(json.dumps({'status': 'failed', 'data': {'message': 'Password didn\'t match. Check and try again!'}}))

            # return redirect('client_login')
        else:
            return render(request, 'consumer/create_consumer_user.html')
    except Exception as e:
        return render(request, 'consumer/create_consumer_user.html')

def consumer_login(request):
    if request.method == 'POST':
        # form = ConsumerLoginForm(request.POST)
        # if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get("password")
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse(json.dumps({'status': 'failed', 'data': {'message': 'failed to login'}}))
    else:
        # form = ConsumerLoginForm()
        return render(request, 'consumer/consumer_login.html')

def consumer_logout(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request, 'home.html')
