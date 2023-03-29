from base64 import urlsafe_b64decode
from django import urls
from django.urls import URLPattern, include, path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('prestamos/',views.prestamos,name='prestamos'),
    path('prestamos/<int:prestamo_id>/',views.prestamo,name='prestamo'),
    path('prestamos/crear/', views.crear, name='crear'),
    path('prestamos/crear/apps/<int:prestamo_id>/', views.crearB, name='crearB'),
    path('prestamos/editar/<int:prestamo_id>/',views.editar,name='editar'),
    path('prestamos/delete/<int:prestamo_id>/', views.delete, name='delete'),
    path('prestamos/delete/apps/<int:apps_id>/', views.deleteB, name='deleteB'),
    path('login/',views.loginU, name='login'),
    path('invitado/',views.logoutU, name='logout'),
]