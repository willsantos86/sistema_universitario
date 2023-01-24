from django.db import models

# Create your models here.
class Campu(models.Model):
    nome = models.CharField(max_length=50,)
    descricao = models.CharField(max_length=150, verbose_name="Descrição")

    def __str__(self):
        return f'{self.nome} ({self.descricao})'

class Atividade(models.Model):
    numero = models.IntegerField(verbose_name='Número')
    descricao = models.CharField(max_length=150, verbose_name='Descrição')
    pontos = models.DecimalField(decimal_places=1, max_digits=4)
    detalhes = models.CharField(max_length=100)
    campo = models.ForeignKey(Campu, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.numero} - {self.descricao} ({self.campo.nome})'
