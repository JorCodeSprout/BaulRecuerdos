from django.shortcuts import render, get_object_or_404
from .models import Carta, Razon, Cupon, Recuerdo

def inicio(request):
    return render(request, 'baul/index.html')

# LISTAS
def cartas(request):
    cartas_list = Carta.objects.all()
    return render(request, 'baul/cartas.html', {'cartas': cartas_list})

def recuerdos(request):
    recuerdos_list = Recuerdo.objects.all().order_by('-fecha')
    return render(request, 'baul/recuerdos.html', {'recuerdos': recuerdos_list})

def razones(request):
    razones_list = Razon.objects.all().order_by('orden')
    return render(request, 'baul/razones.html', {'razones': razones_list})

def cupones(request):
    cupones_list = Cupon.objects.all()
    return render(request, 'baul/cupones.html', {'cupones': cupones_list})

# DETALLES (Página individual que se abre en pestaña nueva)
def detalle_carta(request, pk):
    carta = get_object_or_404(Carta, pk=pk)
    return render(request, 'baul/detalle_carta.html', {'carta': carta})

def detalle_recuerdo(request, pk):
    recuerdo = get_object_or_404(Recuerdo, pk=pk)
    return render(request, 'baul/detalle_recuerdo.html', {'recuerdo': recuerdo})

def detalle_cupon(request, pk):
    cupon = get_object_or_404(Cupon, pk=pk)
    return render(request, 'baul/detalle_cupon.html', {'cupon': cupon})