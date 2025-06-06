
from django.contrib import admin
from django.urls import path
from django.urls import include
from avaliacoes import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('avaliacoes.urls')),
    path('registro/', views.registrar_usuario, name='registro'),
    path('accounts/', include('django.contrib.auth.urls')),  # Para autenticação
]


