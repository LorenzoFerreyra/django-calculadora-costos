from django.shortcuts import render
import requests
import json


from django.shortcuts import render

def calcular(request):
    if request.method == "POST":
        try:
            costo_unitario = float(request.POST["costo_unitario"])
            precio_venta = float(request.POST["precio_venta"])
            cantidad = int(request.POST["cantidad"])

            ingreso_total = precio_venta * cantidad
            costo_total = costo_unitario * cantidad
            ganancia = ingreso_total - costo_total
            margen = round((ganancia / ingreso_total) * 100, 2) if ingreso_total else 0

            resultado = {
                "ingreso_total": f"{ingreso_total:,.2f}",
                "costo_total": f"{costo_total:,.2f}",
                "ganancia": f"{ganancia:,.2f}",
                "margen": margen
            }

            return render(request, "calculadora.html", {"resultado": resultado})
        except Exception as e:
            return render(request, "calculadora.html", {"error": str(e)})

    return render(request, "calculadora.html")
