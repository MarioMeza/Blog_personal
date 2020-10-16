from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.views.static import serve

from django.conf.urls.static import static
# from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(('aplicaciones.base.urls','base'))),
    

    # path('accounts/login/', views.LoginView.as_view(), name='login'),
    # path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    # path('', include('blog.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += [
#         re_path(r'^media/(?P<path>.*)$', serve , {
#             'document_root':settings.MEDIA_ROOT,
#         }),
#     ]
    
    
