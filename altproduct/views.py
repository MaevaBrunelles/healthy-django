from django.shortcuts import render
from .forms import AccountCreationForm


# Create your views here.
def index(request):
    return render(request, 'altproduct/index.html')


def legal(request):
    h1_tag = "Mentions légales"
    context = {'h1_tag': h1_tag}
    return render(request, 'altproduct/legal.html', context)


def account(request):

    if request.method == "POST":
        pass
    else:
        h1_tag = "Créer un compte"
        account_form = AccountCreationForm()

    context = {
        'h1_tag': h1_tag,
        'form': account_form,
    }

    return render(request, 'altproduct/account.html', context)
