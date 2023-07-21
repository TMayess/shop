from django.contrib.auth import get_user_model, authenticate, login, logout
from django.shortcuts import render, redirect

from accounts.forms import StepOneForm, StepTwoForm, StepThreeForm

User = get_user_model()


def signup_user(request):
    if request.method == 'POST':
        form = StepOneForm(request.POST)
        if form.is_valid():
            request.session['lastname'] = form.cleaned_data['lastname']
            request.session['firstname'] = form.cleaned_data['firstname']
            request.session['birthdate'] = form.cleaned_data['birthdate']

            return redirect('signup_steptwo')

    context = {
        'form': StepOneForm(),
    }
    return render(request, 'accounts/signup.html', context)


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
