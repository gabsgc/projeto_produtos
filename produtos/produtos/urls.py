from unicodedata import name
from django.contrib import admin
from django.urls import path
from produtos import views
from produtos.views import remover_produto
from produtos.views import cadastrar_produto
from produtos.views import editar_produto
from produtos.views import produto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('produto/<int:produto_id>', views.produto, name="produto"),
    path('cadastrar/', views.cadastrar_produto),
    path('remover/<int:produto_id>', views.remover_produto, name="produto"),
    path('editar/<int:produto_id>', views.editar_produto, name="produto")
]
