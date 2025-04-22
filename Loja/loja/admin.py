from django.contrib import admin

from django.contrib import admin #isso já vai estar existindo noarquivo
#Register your models here.
from .models import * #imporata nossos models
admin.site.register(Fabricante) #adiciona a interface do adm
admin.site.register(Categoria)
admin.site.register(Produto)