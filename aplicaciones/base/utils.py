from django.core.paginator import Paginator
from .models import Post,Categoria,RedesSociales,Web, Portada
from django.db.models import Q
def consulta(id):
    try:
        return Post.objects.get(id = id)
    except:
        return None

def obtenerRedes():
    return RedesSociales.objects.filter(estado = True).latest('fecha_creacion')

def obtenerPortada():
    return Portada.objects.filter(estado = True).latest('fecha_creacion')


def obtenerWeb():
    return Web.objects.filter(estado = True).latest('fecha_creacion')

def generarCategoria(request,nombre_categoria):
    queryset = request.GET.get("buscar")
    
    posts = Post.objects.filter(
                        estado = True,
                        publicado = True,
                        categoria = Categoria.objects.get(nombre = nombre_categoria)
                        )

    try:
        categoria = Categoria.objects.get(nombre = nombre_categoria)
    except:
        categoria = None

    paginator = Paginator(posts,6)
    pagina = request.GET.get('page')
    posts = paginator.get_page(pagina)
    contexto = {
        'posts':posts,
        'sociales':obtenerRedes(),
        'web':obtenerWeb(),
        'categoria':categoria,
    }
    return contexto

