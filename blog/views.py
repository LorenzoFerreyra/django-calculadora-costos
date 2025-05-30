from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
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

def calculadora(request):
    # Initialize session costs if not present
    if 'costos' not in request.session:
        request.session['costos'] = []
    costos = request.session['costos']
    mensaje = ''

    # Handle adding a new cost
    if request.method == 'POST' and 'agregar_costo' in request.POST:
        nombre = request.POST.get('nombre', '').strip()
        valor = request.POST.get('valor', '').strip()
        try:
            valor = float(valor)
            if nombre and valor >= 0:
                costos.append({'nombre': nombre, 'valor': valor})
                request.session['costos'] = costos
            else:
                mensaje = 'Por favor, ingrese un nombre y un valor válido.'
        except ValueError:
            mensaje = 'El valor debe ser un número.'

    # Handle clearing all costs
    if request.method == 'POST' and 'limpiar_costos' in request.POST:
        request.session['costos'] = []
        costos = []

    resultado = None
    # Handle calculation
    if request.method == 'POST' and 'calcular' in request.POST:
        precio_venta = request.POST.get('precio_venta', '').strip()
        cantidad = request.POST.get('cantidad', '').strip()
        try:
            precio_venta = float(precio_venta)
            cantidad = int(cantidad)
            costo_total = sum([c['valor'] for c in costos]) * cantidad
            ingreso_total = precio_venta * cantidad
            ganancia = ingreso_total - costo_total
            margen = (ganancia / costo_total * 100) if costo_total else 0
            resultado = {
                'ingreso_total': round(ingreso_total, 2),
                'costo_total': round(costo_total, 2),
                'ganancia': round(ganancia, 2),
                'margen': round(margen, 1),
            }
        except (ValueError, ZeroDivisionError):
            mensaje = 'Por favor, complete todos los campos correctamente.'

    return render(request, 'calculadora.html', {
        'costos': costos,
        'resultado': resultado,
        'mensaje': mensaje,
    })
