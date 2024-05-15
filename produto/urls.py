from django.urls import path
from . import views # Esse ponto indica ao Python que o arquivo importado está no mesmo diretório desse mesmo aquivo

urlpatterns = [
    path("", views.home, name='home'),
    path("categoria/<int:id>", views.categorias, name='categoria'),
    path("produto/<int:id>", views.produto, name='produto'),
    path("add_carrinho/", views.add_carrinho, name='add_carrinho'),
    path("ver_carrinho/", views.ver_carrinho, name='ver_carrinho'),
    path("remover_carrinho/<int:id>", views.remover_carrinho, name='remover_carrinho'),
]