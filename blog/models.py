from django.db import models

class Insumo(models.Model):
    CATEGORIAS = [
        ("insumo", "Insumo"),
        ("packaging", "Packaging"),
        ("topping", "Topping"),
        ("energia", "Energía"),
        ("mano_obra", "Mano de obra"),
    ]

    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    unidad = models.CharField(max_length=20, choices=[("kilo", "Kilo/Litro"), ("unidad", "Unidad")])
    fecha = models.DateField()
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)

    def __str__(self):
        return f"{self.nombre} ({self.categoria})"

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad_producida = models.PositiveIntegerField(help_text="Cantidad de unidades producidas por receta base")
    unidades_por_combo = models.PositiveIntegerField(default=1)
    margen_ganancia = models.DecimalField(max_digits=5, decimal_places=2, help_text="En porcentaje, por ejemplo 200 para 200%")

    def __str__(self):
        return self.nombre

    def calcular_precio_unitario(self):
        componentes = self.componentes.all()
        costo_total = sum([comp.costo_total() for comp in componentes])
        return costo_total / self.cantidad_producida if self.cantidad_producida else 0

    def calcular_precio_combo(self):
        return self.calcular_precio_unitario() * self.unidades_por_combo

    def calcular_precio_venta_combo(self):
        return self.calcular_precio_combo() * (1 + self.margen_ganancia / 100)

class ComponenteProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="componentes")
    insumo = models.ForeignKey(Insumo, on_delete=models.PROTECT)
    cantidad_utilizada = models.DecimalField(max_digits=8, decimal_places=3, help_text="Cantidad utilizada (kg o unidades según insumo)")

    def costo_total(self):
        return self.insumo.precio * self.cantidad_utilizada
    def __str__(self):
        return f"{self.cantidad_utilizada} {self.insumo.unidad} de {self.insumo.nombre} en {self.producto.nombre}"