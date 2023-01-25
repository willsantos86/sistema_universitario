from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from .models import Campu, Atividade
from django.urls import reverse_lazy

################# Create ################

class CampuCreate(CreateView):
    model = Campu
    fields = ['nome', 'descricao']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('listar-campo')


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
    success_url = reverse_lazy('listar-campo')

class AtividadeUpdate(UpdateView):
    model = Atividade
    fields = ['numero','descricao','pontos', 'detalhes', 'campo']
    template_name ='cadastro/form.html'
    success_url = reverse_lazy ('index')   


################# Delete ################

class CampuDelete(DeleteView):
    model = Campu
    template_name = 'cadastro/form-excluir.html'
    success_url = reverse_lazy('listar-campo')

class AtividadeDelete(DeleteView):
    model = Atividade
    template_name = 'cadastro/form-excluir.html'
    success_url = reverse_lazy('listar-campo')

################# List ################

class CampuList(ListView):
    model = Campu
    template_name = 'cadastro/lista/campo.html'

class AtividadeList(ListView):
    model = Atividade
    template_name = 'cadastro/lista/atividade.html'