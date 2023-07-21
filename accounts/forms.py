from django import forms


class StepOneForm(forms.Form):
    lastname = forms.CharField(max_length=100, label="Nom")
    firstname = forms.CharField(max_length=100, label="Prénom")
    birthdate = forms.DateField(label="Date de naissance")


class StepTwoForm(forms.Form):
    phone = forms.CharField(max_length=100, label="Numéro de téléphone")
    pays = forms.CharField(max_length=100, label="Pays")
    ville = forms.CharField(max_length=100, label="Ville")
    adresse = forms.CharField(max_length=200, label="Adresse")
    codepostal = forms.CharField(max_length=10, label="Code postal")


class StepThreeForm(forms.Form):
    email = forms.EmailField(label="Adresse e-mail")
    password = forms.CharField(widget=forms.PasswordInput(), label="Mot de passe")
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label="Confirmer le mot de passe")
