from unicodedata import name
from django.contrib import admin
from django.urls import path
from produtos import views
from produtos.views import cadastrar_produto
from produtos.views import produto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('produto/<int:produto_id>', views.produto, name="produto"),
    path('cadastrar/', views.cadastrar_produto)
]
