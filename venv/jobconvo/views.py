from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Vaga, Candidato
from jobconvo.forms import VagaForm, CandidatoForm

def pginicial(request):
    return render(request, 'pginicial.html')


@login_required(login_url='/accounts/login')
def index(request):
    data = {}
    data['db'] = Vaga.objects.all()
    return render(request, 'index.html', data)

def candidatos(request):
    data = {}
    data['bd'] = Candidato.objects.all()
    return render(request, 'candidatos.html', data)


def lista(request):
    data = {}
    data['db'] = Vaga.objects.all()
    return render(request, 'lista.html', data)


def vaga(request, vaga_id):
    vaga = get_object_or_404(Vaga, pk=vaga_id)

    vaga_a_exibir={
        'vaga' : vaga
    }

    return render(request,'vaga.html', vaga_a_exibir)


def login(request):
    return render(request, 'login.html')


def form(request):
    data = {}
    data['form'] = VagaForm()
    return render(request, 'form.html', data)

def cand(request):
    data = {}
    data['cand'] = CandidatoForm()
    return render(request, 'cand.html', data)


def create(request):
    form = VagaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')


def createcand(request):
    cand = CandidatoForm(request.POST or None)
    if cand.is_valid():
        cand.save()
        return redirect('lista')


def viewcd(request, pk):
    data = {}
    data['db'] = Vaga.objects.get(pk=pk)
    return render(request, 'viewcd.html', data)


def edit(request, pk):
    data = {}
    # o get vai pegar o pk que é o parâmetro que está sendo passado através da url que é o <int:pk>
    data['db'] = Vaga.objects.get(pk=pk)
    # VagaForm vai chamar uma instância que vai vir lá do "database",
    # essa instancia vai ser o objeto de acordo com a "pk"
    # com base nisso será gerado o formulário
    data['form'] = VagaForm(instance=data['db'])
    return render(request, 'form.html', data)
#estamos utilizando o mesmo formulário do cadastro para edição


def update(request, pk):
    data = {}
    data['db'] = Vaga.objects.get(pk=pk)
    # "request.POST" quer dizer que está recebendo os dados via POST, passando a instância o Django vai interpretar
    # que é para fazer o "update" pegando os dados que estão vindo via POST e fazer o "update" nesse objeto que
    # está vindo lá do banco de dados
    form = VagaForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('index')


def delete(request, pk):
    db = Vaga.objects.get(pk=pk)
    db.delete()
    return redirect('index')

