from django.urls import path
from .views import CampuCreate, AtividadeCreate
from .views import CampuUpdate, AtividadeUpdate
from .views import CampuDelete, AtividadeDelete
from .views import CampuList, AtividadeList


urlpatterns = [
    path('cadastrar/campo/', CampuCreate.as_view(), name='cadastrar-campo'),
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name='cadastrar-atividade'),

    path('editar/campo/<int:pk>/', CampuUpdate.as_view(), name='editar-campo'),
    path('editar/atividade/<int:pk>/', AtividadeUpdate.as_view(), name='editar-atividade'),

    path('excluir/campo/<int:pk>/', CampuDelete.as_view(), name='excluir-campo'),
    path('excluir/atividade/<int:pk>/', AtividadeDelete.as_view(), name='excluir-atividade'),

    path('listar/campo/', CampuList.as_view(), name='listar-campo'),
    path('listar/atividade/', AtividadeList.as_view(), name='listar-atividade'),
    
]