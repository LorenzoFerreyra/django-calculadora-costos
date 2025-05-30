from django import forms
from .models import Insumo, Producto, ComponenteProducto

class InsumoForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class ComponenteProductoForm(forms.ModelForm):
    class Meta:
        model = ComponenteProducto
        fields = ['insumo', 'cantidad_utilizada']
