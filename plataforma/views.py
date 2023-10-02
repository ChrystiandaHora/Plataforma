from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger
from .models import Transacao
from .forms import TransacaoForm


@login_required(login_url="/auth/login")
def plataforma(request):
    transacoes = Transacao.objects.filter(usuario=request.user)

    entradas = 0
    saidas = 0

    for transacao in transacoes:
        if transacao.tipo == 'E':
            entradas += transacao.valor
        else:
            saidas += transacao.valor

    saldo = entradas - saidas

    return render(request, 'plataforma.html', {
        'transacoes': transacoes,
        'saldo': saldo,
        'entradas': entradas,
        'saidas': saidas,
    })


@login_required(login_url="/auth/login")
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


@login_required(login_url="/auth/login")
def listar_transacoes(request):
    transacoes = Transacao.objects.filter(usuario=request.user)

    registros_por_pagina = 10
    paginator = Paginator(transacoes, registros_por_pagina)

    page = request.GET.get('page', 1)

    try:
        transacoes_pagina = paginator.page(page)
    except PageNotAnInteger:
        transacoes_pagina = paginator.page(1)
    except EmptyPage:
        transacoes_pagina = paginator.page(paginator.num_pages)

    entradas = 0
    saidas = 0

    for transacao in transacoes_pagina:
        if transacao.tipo == 'E':
            entradas += transacao.valor
        else:
            saidas += transacao.valor

    saldo = entradas - saidas

    return render(request, 'plataforma/listar_transacoes.html', {
        'transacoes': transacoes_pagina,
        'saldo': saldo,
        'entradas': entradas,
        'saidas': saidas,
    })
