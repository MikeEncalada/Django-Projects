from django.contrib import admin

#Se importan los modelos que se quiere gestionar desde el panel de administracion
from gestionPedidos.models import Clientes, Articulos, Pedidos

# Register your models here.

class ClientesAdmin(admin.ModelAdmin):  
    list_display = ("nombre", "direccion", "telefono") #Con esto se lográ añadir los campos que se ven en la lista del panel admin
    search_fields = ("nombre", "telefono") #Para agregar busquedas por campos (se agrega un campo de busquedas)

class ArticulosAdmin(admin.ModelAdmin):
    list_filter = ("seccion", )   #Esto es así "con coma" porque estamos utilizando una tupla

class PedidosAdmin(admin.ModelAdmin):
    list_display = ("numero", "fecha")
    list_filter= ("fecha",)
    date_hierarchy = "fecha"  #Filtro especializado para fechas

#Agrega en el panel de admin los modelos que se desea gestionar
admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
#admin.site.register(Pedidos) #Se puede dejar así pero se agrega sin filtros ni formato
admin.site.register(Pedidos, PedidosAdmin)

