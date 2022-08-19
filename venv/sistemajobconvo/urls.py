from django.contrib import admin
from django.urls import path, include
from jobconvo.views import index, form, create, edit, update, delete, pginicial, login, lista, viewcd, cand, createcand, candidatos

urlpatterns = [
    path('pginicial/', include('jobconvo.urls')),
    path('admin/', admin.site.urls),
    path('', pginicial, name='pginicial'),
    path('form/', form, name='formulario'),
    path('create/', create, name='create'),
    path('lista/viewcd/<int:pk>/', viewcd, name='viewcd'),
    path('index/edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('index/', index, name='index'),
    path('lista/', lista, name='lista'),
    path('cand/', cand, name='candidatura'),
    path('createcand/', createcand, name='createcand'),
    path('candidatos/', candidatos, name='candidatos')
]

