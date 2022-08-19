from django.contrib import admin
from .models import Vaga, Candidato, Salario, Escolaridade

admin.site.register(Vaga)
admin.site.register(Candidato)
admin.site.register(Salario)
admin.site.register(Escolaridade)
