from datetime import datetime

from django.contrib.auth import get_user_model, authenticate, login, logout
from django.shortcuts import render, redirect

from accounts.forms import StepOneForm, StepTwoForm, StepThreeForm
from accounts.models import Adresse, CustomUser

User = get_user_model()


def signup_step_one(request):
    if request.method == 'POST':
        form = StepOneForm(request.POST)

        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['birthdate'] = cleaned_data['birthdate'].strftime('%d/%m/%Y')

            request.session['signup_data'] = cleaned_data
            return redirect('signup_step_two')
    else:
        form = StepOneForm()

    return render(request, 'accounts/signup.html', {'form': form})


def signup_step_two(request):
    signup_data = request.session.get('signup_data', {})

    if request.method == 'POST':
        form = StepTwoForm(request.POST)
        if form.is_valid():
            signup_data.update(form.cleaned_data)
            request.session['signup_data'] = signup_data
            return redirect('signup_step_three')
    else:
        form = StepTwoForm()

    return render(request, 'accounts/signup.html', {'form': form})

def signup_step_three(request):
    signup_data = request.session.get('signup_data', {})

    if request.method == 'POST':
        form = StepThreeForm(request.POST)
        if form.is_valid():
            signup_data.update(form.cleaned_data)

            firstname = signup_data['firstname']
            lastname = signup_data['lastname']
            username = lastname.upper() + " " + firstname.capitalize()
            password = signup_data['password']
            email = signup_data['email']
            phone = signup_data['phone']
            birthdate_str = signup_data['birthdate']
            birthdate = datetime.strptime(birthdate_str, '%d/%m/%Y').strftime('%Y-%m-%d')
            pays = signup_data['pays']
            ville = signup_data['ville']
            adresse_str = signup_data['adresse']
            codepostal = signup_data['codepostal']


            adresse, _ = Adresse.objects.get_or_create(
                pays=pays,
                ville=ville,
                adresse=adresse_str,
                codepostal=codepostal
            )


            user = CustomUser.objects.create_user(
                username=username,
                firstname=firstname,
                lastname=lastname,
                password=password,
                email=email,
                phone=phone,
                birthdate=birthdate,
                adresse=adresse
            )
            user.set_password(password)
            user.save()

            del request.session['signup_data']

            return redirect('login')
    else:
        form = StepThreeForm()

    return render(request, 'accounts/signup.html', {'form': form})


def success_view(request):
    return render(request, 'success.html')


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
