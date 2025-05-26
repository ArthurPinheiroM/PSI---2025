from django.contrib import admin

from django.contrib import admin #isso já vai estar existindo noarquivo
#Register your models here.
from .models import * #imporata nossos models
class FabricanteAdmin(admin.ModelAdmin):
    # Cria um filtro de hierarquia com datas
    date_hierarchy = 'criado_em'
class ProdutoAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'
    list_display = ('Produto', 'destaque', 'promocao', 'msgPromocao',
    'preco', 'categoria',)
    empty_value_display = 'Vazio'
    # fields = ('Produto', 'destaque', 'promocao', 'msgPromocao', 'preco', 'categoria',) #exclui o fabricante e imagem
    search_fields = ('Produto',) #esse pesquisa os produtos na aba de produtos
    # exclude =('msgPromocao',) #esse exclui a mensagem de promoção
admin.site.register(Fabricante, FabricanteAdmin) #adiciona a interface do adm
admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)
