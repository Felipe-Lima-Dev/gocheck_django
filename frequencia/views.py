from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Excursao, Passageiro
from .forms import PassageiroForm, ExcursaoForm

def index(request):
    """Página inicial do GoCheck (redireciona para a lista de viagens ou login)"""
    if request.user.is_authenticated:
        return redirect('relacao_viagens')
    return render(request, 'frequencia/login.html')

def login_view(request):
    """Ecrã e validação de autenticação/login"""
    if request.method == 'POST':
        usuario_input = request.POST.get('username')
        senha_input = request.POST.get('password')
        
        user = authenticate(request, username=usuario_input, password=senha_input)
        if user is not None:
            login(request, user)
            return redirect('relacao_viagens')
        else:
            context = {'erro': 'Utilizador ou palavra-passe incorretos.'}
            return render(request, 'frequencia/login.html', context)
            
    return render(request, 'frequencia/login.html')

def logout_view(request):
    """Termina a sessão do utilizador"""
    logout(request)
    return redirect('login')

def relacao_viagens(request):
    """Lista todas as excursões cadastradas"""
    lista_viagens = Excursao.objects.all()
    context = {'viagens': lista_viagens}
    return render(request, 'frequencia/relacao_viagens.html', context)

def detalhe_viagem(request, pk):
    """Mostra os detalhes de uma excursão específica"""
    viagem = get_object_or_404(Excursao, pk=pk)
    context = {'viagem': viagem}
    return render(request, 'frequencia/detalhe_viagem.html', context)

def nova_viagem(request):
    """Cadastra/regista uma nova viagem"""
    if request.method == 'POST':
        form = ExcursaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('relacao_viagens')
    else:
        form = ExcursaoForm()
    context = {'form': form}
    return render(request, 'frequencia/novaviagem.html', context)

def novo_passageiro(request):
    """Cadastra um novo passageiro"""
    if request.method == 'POST':
        form = PassageiroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('relacao_viagens')
    else:
        form = PassageiroForm()
    context = {'form': form}
    return render(request, 'frequencia/novo_passageiro.html', context)

def detalhe_passageiro(request, pk):
    """Mostra os detalhes de um passageiro específico"""
    passageiro = get_object_or_404(Passageiro, pk=pk)
    context = {'passageiro': passageiro}
    return render(request, 'frequencia/detalhe_passageiro.html', context)

def editar_viagem(request, pk):
    """Atualiza os dados de uma excursão existente"""
    viagem = get_object_or_404(Excursao, pk=pk)
    if request.method == 'POST':
        form = ExcursaoForm(request.POST, instance=viagem)
        if form.is_valid():
            form.save()
            return redirect('detalhe_viagem', pk=viagem.pk)
    else:
        form = ExcursaoForm(instance=viagem)
    context = {'form': form, 'viagem': viagem}
    return render(request, 'frequencia/editar_viagem.html', context)

def deletar_viagem(request, pk):
    """Elimina uma excursão da base de dados"""
    viagem = get_object_or_404(Excursao, pk=pk)
    if request.method == 'POST':
        viagem.delete()
        return redirect('relacao_viagens')
    context = {'viagem': viagem}
    return render(request, 'frequencia/confirmar_exclusao.html', context)