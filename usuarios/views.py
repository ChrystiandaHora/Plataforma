from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django, logout


def cadastro(request):
    if request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirme_senha = request.POST.get('confirme_senha')

        if len(username) < 3:
            error_message = 'O nome de usuário deve conter pelo menos 3 caracteres.'
        elif User.objects.filter(username=username).exists():
            error_message = 'Já existe um usuário com esse nome.'
        elif not (8 <= len(senha) <= 20):
            error_message = 'A senha deve conter entre 8 e 20 caracteres.'
        elif senha != confirme_senha:
            error_message = 'As senhas não coincidem.'
        else:
            user = User.objects.create_user(
                username=username, password=senha)
            user.save()
            return redirect('login')

        return render(request, 'cadastro.html', {'error_message': error_message})
    else:
        return render(request, 'cadastro.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)
            return redirect('plataforma')
        else:
            error_message = 'Usuário ou senha inválidos.'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')


def sair(request):
    logout(request)
    return redirect('login')
