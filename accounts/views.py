from django.contrib.auth import get_user_model, authenticate, login, logout
from django.shortcuts import render, redirect

User = get_user_model()


def signup_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        return redirect('index')

    return render(request, 'accounts/signup.html')


def login_user(request):
    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect('index')

    return render(request, 'accounts/login.html')


def logout_user(request):
    logout(request)
    return redirect('index')