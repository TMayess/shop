from django import forms


class StepOneForm(forms.Form):
    lastname = forms.CharField(
        max_length=100,
        label="Nom",
        widget=forms.TextInput(attrs={'placeholder': 'Entrez votre nom'})
    )
    firstname = forms.CharField(
        max_length=100,
        label="Prenom",
        widget=forms.TextInput(attrs={'placeholder': 'Entrez votre prenom'})
    )
    birthdate = forms.DateField(
        label="Date de naissance",
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'JJ/MM/AAAA'})
    )
    phone = forms.CharField(
        max_length=100,
        label="Numéro de téléphone",
        widget=forms.TextInput(attrs={'placeholder': 'Entrez votre numéro de téléphone'})
    )


class StepTwoForm(forms.Form):
    pays = forms.CharField(
        max_length=100,
        label="Pays",
        widget=forms.TextInput(attrs={'placeholder': 'Entrez votre pays'})
    )
    ville = forms.CharField(
        max_length=100,
        label="Ville",
        widget=forms.TextInput(attrs={'placeholder': 'Entrez votre ville'})
    )
    adresse = forms.CharField(
        max_length=200,
        label="Adresse",
        widget=forms.TextInput(attrs={'placeholder': 'Entrez votre adresse'})
    )
    codepostal = forms.CharField(
        max_length=10,
        label="Code postal",
        widget=forms.TextInput(attrs={'placeholder': 'Entrez votre code postal'})
    )

class StepThreeForm(forms.Form):
    email = forms.EmailField(
        label="Adresse e-mail",
        widget=forms.EmailInput(attrs={'placeholder': 'Entrez votre adresse e-mail'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Entrez votre mot de passe'}),
        label="Mot de passe"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirmez votre mot de passe'}),
        label="Confirmer le mot de passe"
    )