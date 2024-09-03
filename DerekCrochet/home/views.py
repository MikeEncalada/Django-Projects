from django.shortcuts import render

from home.models import CategoriaProducto, Producto

from django.core.paginator import Paginator

# Create your views here.

def home(request):

    categorias_activadas = CategoriaProducto.objects.filter(activado=True)

    return render(request, "home/home.html", {"categoriasActivadas": categorias_activadas})

def catalogo(request):

    productos = Producto.objects.all()

    # Obtener la categoría seleccionada (si hay alguna)
    categoria_id = request.GET.get('categoria')

    # Filtrar productos por categoría seleccionada (si hay alguna)
    if categoria_id:
        productos = productos.filter(categorias__id=categoria_id)

    # Configurar la paginación
    paginator = Paginator(productos, 12)  # Muestra 10 productos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Obtener todas las categorías para el filtro
    categorias = CategoriaProducto.objects.all().values('id', 'nombre')

    return render(request, 'home/catalogo.html', {'page_obj': page_obj, 'categorias': categorias})
