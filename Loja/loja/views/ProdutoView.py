from django.shortcuts import render
from loja.models import Produto
from datetime import timedelta, datetime
from django.utils import timezone
def edit_produto_view(request, id=None):
    produtos = Produto.objects.all()
    if id is not None:
        produtos = produtos.filter(id=id)
    produto = produtos.first()
    print(produto)
    context = { 'produto': produto }
    return render(request, template_name='produto/produto-edit.html', context=context, status=200)

def list_produto_view(request, id=None):
    dias = request.GET.get("dias")
    produto = request.GET.get("produto")
    destaque = request.GET.get("destaque")
    promocao = request.GET.get("promocao")
    categoria = request.GET.get("categoria")
    fabricante = request.GET.get("fabricante")
    produtos = Produto.objects.all()
    if produto is not None:
        produtos = produtos.filter(Produto__contains=produto)
    if promocao is not None:
        produtos = produtos.filter(promocao=promocao)
    if destaque is not None:
        produtos = produtos.filter(destaque=destaque)  
    # print(produtos)
    if destaque is not None:
        print(destaque)
    if produto is not None:
        print(produto)
    if promocao is not None:
        print(promocao)
    if categoria is not None:
        produtos = produtos.filter(categoria__Categoria=categoria)
    if fabricante is not None:
        produtos = produtos.filter(fabricante__Fabricante=fabricante)
    if id is not None:
        produtos = produtos.filter(id=id)
    if dias is not None:
        now = timezone.now()
        print(dias)
        now = now - timedelta(days = int(dias))
        produtos = produtos.filter(criado_em__gte=now)
    # print(produtos)
    
    context = {'produtos': produtos}
    return render(request, template_name='produto/produto.html', context=context, status=200)
    

    # if id is None:
    #     return HttpResponse('<h1>Nenhum id foi informado</h1>') #opcional!
    # return HttpResponse('<h1>Produto de id %s!</h1>' % id)