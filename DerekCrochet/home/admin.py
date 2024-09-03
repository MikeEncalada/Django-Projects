from django.contrib import admin

# Register your models here.

from .models import CategoriaProducto, Producto

class CategoriaProdAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(CategoriaProducto, CategoriaProdAdmin)
admin.site.register(Producto, ProductoAdmin)