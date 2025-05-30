from django.urls import path
from . import views

urlpatterns = [
    path('producto/<int:pk>/', views.producto_detail, name='producto_detail'),
    path('producto/<int:producto_id>/agregar-componente/', views.agregar_componente, name='agregar_componente'),
]
