from django.shortcuts import render, redirect
from loja.models import Produto
from datetime import timedelta, datetime
from django.utils import timezone

def edit_produto_postback(request, id=None):
    if request.method == 'POST':
    # Salva dados editados
        id = request.POST.get("id")
        produto = request.POST.get("Produto")
        destaque = request.POST.get("destaque")
        promocao = request.POST.get("promocao")
        msgPromocao = request.POST.get("msgPromocao")
        print("postback")
        print(id)
        print(produto)
        print(destaque)
        print(promocao)
        print(msgPromocao)
        try:
            obj_produto = Produto.objects.filter(id=id).first()
            obj_produto.Produto = produto
            obj_produto.destaque = (destaque is not None)
            obj_produto.promocao = (promocao is not None)
            if msgPromocao is not None:
                obj_produto.msgPromocao = msgPromocao
                obj_produto.save()
                print("Produto %s salvo com sucesso" % produto)
        except Exception as e:
                print("Erro salvando edição de produto: %s" % e)
    return redirect("/produto")



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
    

def details_produto_view(request, id=None):
# Processa o evento GET gerado pela action
    produtos = Produto.objects.all()
    if id is not None:
        produtos = produtos.filter(id=id)
    produto = produtos.first()
    print(produto)
    context = {'produto': produto}
    return render(request, template_name='produto/produto-details.html', context=context,
    status=200)


def delete_produto_view(request, id=None):
# Processa o evento GET gerado pela action
    produtos = Produto.objects.all()
    if id is not None:
        produtos = produtos.filter(id=id)
    produto = produtos.first()
    print(produto)
    context = {'produto': produto}
    return render(request, template_name='produto/produto-delete.html', context=context, status=200)
    # if id is None:
    #     return HttpResponse('<h1>Nenhum id foi informado</h1>') #opcional!
    # return HttpResponse('<h1>Produto de id %s!</h1>' % id)