from django.urls import path
from .views import CampuCreate, AtividadeCreate
from .views import CampuUpdate, AtividadeUpdate


urlpatterns = [
    path('cadastrar/campo/', CampuCreate.as_view(), name='cadastrar-campo'),
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name='cadastrar-atividade'),

    path('editar/campo/<int:pk>/', CampuUpdate.as_view(), name='editar-campo'),
    path('editar/atividade/<int:pk>/', CampuUpdate.as_view(), name='editar-atividade'),
    
]