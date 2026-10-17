from django.shortcuts import render, redirect, get_object_or_404
from .models import Excursao, Passageiro
from .forms import ExcursaoForm, PassageiroForm

# --- VIEWS DE EXCURSÃO ---
def lista_excursoes(request):
    excursoes = Excursao.objects.all()
    return render(request, 'frequencia/lista_excursoes.html', {'excursoes': excursoes})

def detalhe_excursao(request, pk):
    excursao = get_object_or_404(Excursao, pk=pk)
    passageiros = excursao.passageiros.all()
    return render(request, 'frequencia/detalhe_excursao.html', {'excursao': excursao, 'passageiros': passageiros})

def criar_excursao(request):
    if request.method == 'POST':
        form = ExcursaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_excursoes')
    else:
        form = ExcursaoForm()
    return render(request, 'frequencia/form_excursao.html', {'form': form})

def editar_excursao(request, pk):
    excursao = get_object_or_404(Excursao, pk=pk)
    if request.method == 'POST':
        form = ExcursaoForm(request.POST, instance=excursao)
        if form.is_valid():
            form.save()
            return redirect('lista_excursoes')
    else:
        form = ExcursaoForm(instance=excursao)
    return render(request, 'frequencia/form_excursao.html', {'form': form})

def excluir_excursao(request, pk):
    excursao = get_object_or_404(Excursao, pk=pk)
    if request.method == 'POST':
        excursao.delete()
        return redirect('lista_excursoes')
    return render(request, 'frequencia/confirma_exclusao.html', {'objeto': excursao, 'tipo': 'Excursão'})

# --- VIEWS DE PASSAGEIRO ---
def criar_passageiro(request):
    if request.method == 'POST':
        form = PassageiroForm(request.POST)
        if form.is_valid():
            passageiro = form.save()
            return redirect('detalhe_excursao', pk=passageiro.excursao.pk)
    else:
        form = PassageiroForm()
    return render(request, 'frequencia/form_passageiro.html', {'form': form})

def editar_passageiro(request, pk):
    passageiro = get_object_or_404(Passageiro, pk=pk)
    if request.method == 'POST':
        form = PassageiroForm(request.POST, instance=passageiro)
        if form.is_valid():
            form.save()
            return redirect('detalhe_excursao', pk=passageiro.excursao.pk)
    else:
        form = PassageiroForm(instance=passageiro)
    return render(request, 'frequencia/form_passageiro.html', {'form': form})

def excluir_passageiro(request, pk):
    passageiro = get_object_or_404(Passageiro, pk=pk)
    excursao_pk = passageiro.excursao.pk
    if request.method == 'POST':
        passageiro.delete()
        return redirect('detalhe_excursao', pk=excursao_pk)
    return render(request, 'frequencia/confirma_exclusao.html', {'objeto': passageiro, 'tipo': 'Passageiro'})

    from django.shortcuts import render

def login_view(request):
    return render(request, 'frequencia/login.html')