from django.db import models


class Vaga(models.Model):
    nome_vaga = models.CharField(max_length=200)
    requisitos = models.TextField()
    faixa_salarial = models.ForeignKey('Salario', related_name='ganhos', on_delete=models.CASCADE, null=True)
    escolaridade_minima = models.ForeignKey('Escolaridade', related_name='ganhos', on_delete=models.CASCADE, null=True)
    candidatos = models.ManyToManyField("Candidato", null=True)


class Candidato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(null=False, blank=False)
    pretensao_salarial = models.ForeignKey('Salario', related_name='itens', on_delete=models.CASCADE, null=True)
    experiencia = models.TextField()
    ultima_escolaridade = models.ForeignKey('Escolaridade', related_name='itens', on_delete=models.CASCADE, null=True)
    vaga_desejada = models.ManyToManyField("Vaga")


class Salario(models.Model):
    faixa_salarial = models.CharField(max_length=100)

    def __str__(self):
        return self.faixa_salarial


class Escolaridade(models.Model):
    escolaridade = models.CharField(max_length=100)

    def __str__(self):
        return self.escolaridade





