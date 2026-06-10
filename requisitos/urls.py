from django.urls import path
from . import views

app_name = 'requisitos'

urlpatterns = [
    path('', views.lista, name='lista'),
    path('novo/', views.criar, name='criar'),
    path('<int:pk>/editar/', views.editar, name='editar'),
    path('<int:pk>/excluir/', views.excluir, name='excluir'),
    path('<int:pk>/historico/', views.historico, name='historico'),
    path('<int:pk>/chat/', views.chat, name='chat'),
    path('<int:pk>/chat/buscar/', views.buscar_mensagens, name='buscar_mensagens'),
    path('mensagem/<int:pk>/like/', views.like_mensagem, name='like_mensagem'),
    path('matriz/', views.matriz_rastreabilidade, name='matriz'),
    path('exportar/json/', views.exportar_json, name='exportar_json'),
    path('exportar/pdf/', views.exportar_pdf, name='exportar_pdf'),
    path('exportar/docx/', views.exportar_docx, name='exportar_docx'),
    path('exportar/markdown/', views.exportar_markdown, name='exportar_markdown'),
]
