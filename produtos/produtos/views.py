from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from produtos.entity import Produto

produto1 = Produto(
    id= 1, 
    name="Smartphone Moto G30", 
    description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus sodales iaculis felis, ut viverra ex.", 
    price=2000.00, 
    image="https://www.casasbahia-imagens.com.br/Control/ArquivoExibir.aspx?IdArquivo=1685155745"
)
produto2 = Produto(
    id= 2,
    name="Headset Gamer RGB Blackfire", 
    description="Aenean sit amet arcu dui. Nullam congue tortor vel ante suscipit, sodales dignissim erat dignissim.", 
    price=129.99, 
    image="https://m.media-amazon.com/images/I/61UzXyG5S2L._AC_SL1000_.jpg"
)
produto3 = Produto(
    id=3,
    name="Relógio Smartwatch Amazfit GTS 2 mini - Black", 
    description="Vivamus vel posuere eros. Aliquam posuere vitae lectus euismod cursus",
    price=550.99, 
    image="https://m.media-amazon.com/images/I/61hmDN6921L._AC_SX569_.jpg")

produtos = [produto1, produto2, produto3]

dados = {'produtos': produtos}

def index(request):
    return render(request=request, template_name="index.html", context=dados)

def produto(request, produto_id):
    for produto in produtos:
        if produto_id == produto.id:
            produto_selecionado = produto

    produto_a_exibir = {
        'produto': produto_selecionado
    }
    
    return render(request=request, context=produto_a_exibir, template_name="produto.html")

def cadastrar_produto(request):
    if request.method == "POST":
        id = len(produtos) + 1
        name = request.POST.get("name", None)
        image = request.POST.get("image", None)
        description = request.POST.get("description", None)
        price = request.POST.get("price", None)
        produto = Produto(id=id, name=name, image=image, description=description, price=price)
        produtos.append(produto)
        return render(request=request, template_name="cadastro.html", context={"produtos": produtos})
    
    return render(request=request, template_name="cadastro.html", context={"produtos": produtos})
