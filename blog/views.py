from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Producto
from .forms import ComponenteProductoForm, ProductoForm
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group

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
    if 'costos' not in request.session:
        request.session['costos'] = []
    costos = request.session['costos']
    mensaje = ''
    resultado = None
    htmx = request.headers.get('HX-Request') == 'true'

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
        if htmx:
            html = render_to_string('blog/partials/costos_list.html', {'costos': costos, 'mensaje': mensaje}, request=request)
            return render(request, 'blog/partials/costos_list.html', {'costos': costos, 'mensaje': mensaje})

    # Handle clearing all costs
    if request.method == 'POST' and 'limpiar_costos' in request.POST:
        request.session['costos'] = []
        costos = []
        if htmx:
            return render(request, 'blog/partials/costos_list.html', {'costos': costos, 'mensaje': mensaje})

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
        if htmx:
            return render(request, 'blog/partials/result_box.html', {'resultado': resultado})

    # Normal full page render
    return render(request, 'calculadora.html', {
        'costos': costos,
        'resultado': resultado,
        'mensaje': mensaje,
    })

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

@login_required
def backoffice(request):
    productos = Producto.objects.all()
    return render(request, 'backoffice.html', {'productos': productos})

@login_required
def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('backoffice')
    else:
        form = ProductoForm()
    return render(request, 'producto_form.html', {'form': form})

@login_required
def producto_edit(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('backoffice')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'producto_form.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_staff)
def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('backoffice')
    return render(request, 'producto_confirm_delete.html', {'producto': producto})
