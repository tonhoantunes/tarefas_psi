from django.shortcuts import render
from datetime import date
from .models import Tarefa

# Create your views here.

def index(request):
    hoje = date.today()

    tarefas = Tarefa.objects.all()

    context = {
        "tarefas": tarefas,
        "hoje": hoje, 
    }

    return render(request, 'index.html', context)