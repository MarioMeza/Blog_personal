import random
from django.shortcuts import render,redirect
from django.views.generic import ListView,View,DetailView
from django.core.mail import send_mail
from mysite.settings import EMAIL_HOST_USER
from .models import Post,Categoria,RedesSociales,Web,Suscriptor, Portada
from .utils import *
from .forms import ContactoForm
from django.db.models import Q
from django.template import RequestContext
class Inicio(ListView):
    def get(self,request,*args,**kwargs):
        queryset = request.GET.get("buscar")
        posts = Post.objects.filter(estado = True)
        if queryset:
            posts = Post.objects.filter(
                Q(titulo__icontains = queryset) |
                Q(descripcion__icontains = queryset)
            ).distinct()
            
        posts = list(Post.objects.filter(
                estado = True,
                publicado = True
                ).values_list('id',flat = True))

        principal = random.choice(posts)
        posts.remove(principal)
        principal = consulta(principal)

        post1 = random.choice(posts)
        posts.remove(post1)
        post2 = random.choice(posts)
        posts.remove(post2)
        post3 = random.choice(posts)
        posts.remove(post3)
        post4 = random.choice(posts)
        posts.remove(post4)


        try:
            post_videojuegos = Post.objects.filter(
                                estado = True,
                                publicado = True,
                                categoria = Categoria.objects.get(nombre = 'Videojuegos')
                                ).latest('fecha_publicacion')
        except:
            post_videojuegos = None

        try:
            post_general = Post.objects.filter(
                            estado = True,
                            publicado = True,
                            categoria = Categoria.objects.get(nombre = 'General')
                            ).latest('fecha_publicacion')
        except:
            post_general = None

        contexto = {
            'principal':principal,
            'post1': consulta(post1),
            'post2': consulta(post2),
            'post3': consulta(post3),
            'post4': consulta(post4),

            'post_general':post_general,
            'post_videojuegos':post_videojuegos,
            'sociales':obtenerRedes(),
            'web':obtenerWeb(),
            'portadas':obtenerPortada(),
        }

    
                

        return render(request,'index.html',contexto)


class Listado(ListView):

    def get(self,request,nombre_categoria,*args,**kwargs):
        contexto = generarCategoria(request,nombre_categoria)
        return render(request,'category.html',contexto)
    
class FormularioContacto(View):
    def get(self,request,*args,**kwargs):
        form = ContactoForm()
        contexto = {
            'sociales':obtenerRedes(),
            'web':obtenerWeb(),
            'form':form,
        }
        return render(request,'contact.html',contexto)

    def post(self,request,*args,**kwargs):
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base:index')
        else:
            contexto = {
                'form':form,
            }
            return render(request,'contact.html',contexto)
        

class DetallePost(DetailView):
    def get(self,request,slug,*args,**kwargs):
        # queryset = request.GET.get("buscar")
        # posts = Post.objects.filter(
        #     estado = True,
        #     categoria = Categoria.objects.get(nombre_iexact = 'General')
        #     )

        # if queryset:
        #     posts = Post.objects.filter(
        #         Q(titulo__icontains = queryset) |
        #         Q(descripcion__icontains = queryset),
        #         estado = True,
        #         categoria = Categoria.objects.get(nombre_iexact = 'General'),

        #     ).distinct()
        try:
            post = Post.objects.get(slug = slug)
        except:
            post = None
        posts = list(Post.objects.filter(
                estado = True,
                publicado = True
                ).values_list('id',flat = True))
        posts.remove(post.id)
        post1 = random.choice(posts)
        posts.remove(post1)
        post2 = random.choice(posts)
        posts.remove(post2)
        post3 = random.choice(posts)
        posts.remove(post3)

        contexto = {
            'post':post,
            'sociales':obtenerRedes(),
            'portadas':obtenerPortada(),
            'web':obtenerWeb(),
            'post1':consulta(post1),
            'post2':consulta(post2),
            'post3':consulta(post3),
        }

        return render(request,'post.html',contexto)
    
    
class Suscribir(View):
    def post(self,request,*args,**kwargs):
        correo = request.POST.get('correo')
        Suscriptor.objects.create(correo = correo)
        asunto = 'GRACIAS POR SUSCRIBIRTE A BLOG.DEV!'
        mensaje = 'Te haz suscrito exitosamente a Blog.Dev, Gracias por tu preferencia!!!'
        try:
            send_mail(asunto,mensaje,EMAIL_HOST_USER,[correo])
        except:
            pass

        return redirect('base:index')
    
    
# def handler404(request, exception):
#     return render(request, "errors/404.html", {})
    
# def handler404(request, exception):
#     context = {}
#     response = render(request, "/errors/404.html", context=context)
#     response.status_code = 404
#     return response
# def handler404(request, exception, template_name="404.html"):
#     response = render(template_name)
#     response.status_code = 404
#     return response

def handler404(request, exception=None):
    return render(request, '404.html', {})

def handler500(request, exception=None):
    return render(request, "500.html", {})

def handler403(request, exception=None):
    return render(request, "403.html", {})

def handler400(request, exception=None):
    return render(request, "400.html", {})


# def response_error_handler(request, exception=None):
#     return HttpResponse('Error handler content', status=403)
        
    
    

    