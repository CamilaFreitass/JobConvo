from django.forms import ModelForm
from jobconvo.models import Vaga, Candidato

class VagaForm(ModelForm):
    class Meta:
        model = Vaga
        fields = ['nome_vaga', 'requisitos', 'faixa_salarial', 'escolaridade_minima', 'candidatos']


class CandidatoForm(ModelForm):
    class Meta:
        model = Candidato
        fields = ['nome', 'email', 'pretensao_salarial', 'experiencia', 'ultima_escolaridade', 'vaga_desejada']



