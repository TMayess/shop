from datetime import datetime
from email.message import EmailMessage
from pyexpat.errors import messages

from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from accounts.forms import StepOneForm, StepTwoForm, StepThreeForm
from accounts.models import Adresse, CustomUser
from accounts.token import account_activation_token

User = get_user_model()


def signup_step_one(request):
    if request.method == 'POST':
        form = StepOneForm(request.POST)

        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['birthdate'] = cleaned_data['birthdate'].strftime('%d/%m/%Y')

            request.session['signup_data'] = cleaned_data
            return redirect('signup_step_two')

    context = {
        'form' : StepOneForm(),
        'title' : "Informations personnelles",
        'subtitle' : "Prière de fournir les détails suivants pour compléter votre inscription :",
    }

    return render(request, 'accounts/signup.html', context=context)


def signup_step_two(request):
    signup_data = request.session.get('signup_data', {})

    if request.method == 'POST':
        form = StepTwoForm(request.POST)
        if form.is_valid():
            signup_data.update(form.cleaned_data)
            request.session['signup_data'] = signup_data
            return redirect('signup_step_three')


    context = {
        'form': StepTwoForm(),
        'title': "Adresse",
        'subtitle': "",
    }

    return render(request, 'accounts/signup.html', context=context)


def signup_step_three(request):
    signup_data = request.session.get('signup_data', {})
    print(signup_data)

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
                password=password,
                email=email,
                phone=phone,
                birthdate=birthdate,
                adresse=adresse
            )

            user.firstname = firstname
            user.lastname = lastname
            user.save()




            del request.session['signup_data']

            messages.success(request, f"vous avez creer une nouveau utilisateur")
            return HttpResponse('Please confirm your email address to complete the registration')






    context = {
        'form': StepThreeForm(),
        'title': "Sécurité",
        'subtitle': "Veuillez remplir le formulaire d'inscription :",
    }

    return render(request, 'accounts/signup.html', context=context)





def login_user(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:

            return render(request, 'accounts/login.html', {'error': 'Email ou mot de passe incorrect.'})
    else:
        return render(request, 'accounts/login.html')


def logout_user(request):
    logout(request)
    return redirect('index')
