from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:vaga_id>', views.vaga, name='vaga'),
    path('form/', views.form, name='formulario'),
    path('create/', views.create, name='create'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('pginicial/', views.pginicial, name='pginicial'),
]


