from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Transacao
from .forms import TransacaoForm


@login_required(login_url="/auth/login")
def plataforma(request):
    return render(request, 'plataforma.html')


@login_required
def listar_transacoes(request):
    transacoes = Transacao.objects.filter(usuario=request.user)
    return render(request, 'plataforma/listar_transacoes.html', {'transacoes': transacoes})


@login_required
def adicionar_transacao(request):
    if request.method == 'POST':
        form = TransacaoForm(request.POST)
        if form.is_valid():
            # Associa transação ao usuário atualmente logado
            nova_transacao = form.save(commit=False)
            nova_transacao.usuario = request.user
            nova_transacao.save()
            return redirect('listar_transacoes')
    else:
        form = TransacaoForm()
    return render(request, 'plataforma/adicionar_transacao.html', {'form': form})


@login_required
def listar_transacoes(request):
    # Calcular o saldo com base nas transações do usuário
    transacoes = Transacao.objects.filter(usuario=request.user)

    saldo = 0
    for transacao in transacoes:
        if transacao.tipo == 'E':
            saldo += transacao.valor
        else:
            saldo -= transacao.valor

    return render(request, 'plataforma/listar_transacoes.html', {'transacoes': transacoes, 'saldo': saldo})
