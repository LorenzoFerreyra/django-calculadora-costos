from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculadora, name='calculadora'),
    path('backoffice/', views.backoffice, name='backoffice'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logout, name='logout'),
    path('producto/create/', views.producto_create, name='producto_create'),
    path('producto/<int:pk>/', views.producto_detail, name='producto_detail'),
    path('producto/<int:producto_id>/agregar-componente/', views.agregar_componente, name='agregar_componente'),
    path('producto/<int:pk>/edit/', views.producto_edit, name='producto_edit'),
    path('producto/<int:pk>/delete/', views.producto_delete, name='producto_delete'),
    path('export/excel/', views.export_productos_excel, name='export_productos_excel'),
]
