from django.shortcuts import render, get_object_or_404
from .models import Producto
from .forms import ComponenteProductoForm

def producto_detail(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    form = ComponenteProductoForm()
    return render(request, 'blog/producto_detail.html', {
        'producto': producto,
        'form': form
    })

def agregar_componente(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    if request.method == "POST":
        form = ComponenteProductoForm(request.POST)
        if form.is_valid():
            componente = form.save(commit=False)
            componente.producto = producto
            componente.save()
    return render(request, 'blog/partials/componentes_table.html', {
        'producto': producto
    })
