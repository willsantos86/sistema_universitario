from django.views.generic import CreateView, UpdateView
from .models import Campu, Atividade
from django.urls import reverse_lazy

################# Create ################

class CampuCreate(CreateView):
    model = Campu
    fields = ['nome', 'descricao']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('index')


class AtividadeCreate(CreateView):
    model = Atividade
    fields = ['numero','descricao','pontos', 'detalhes', 'campo']
    template_name ='cadastro/form.html'
    success_url = reverse_lazy ('index')



################# Update ################

class CampuUpdate(UpdateView):
    model = Campu
    fields = ['nome', 'descricao']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('index')

class AtividadeUpdate(UpdateView):
    model = Atividade
    fields = ['numero','descricao','pontos', 'detalhes', 'campo']
    template_name ='cadastro/form.html'
    success_url = reverse_lazy ('index')   