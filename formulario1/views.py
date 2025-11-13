from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ReporteFalla
from datetime import timedelta

def index(request):
    if request.method == 'POST':
        # === 1. Leer campos del formulario ===
        fecha = request.POST.get('fecha')
        tecnico = request.POST.get('tecnico')          # <select name="tecnico">
        linea = request.POST.get('linea')              # <select name="linea">
        operacion = request.POST.get('operacion')      # <select name="operacion">
        tipo_falla = request.POST.get('tipo_falla')
        falla = request.POST.get('falla')
        actividad = request.POST.get('actividad')
        refacciones = request.POST.get('refacciones')
        tiempo_muerto = request.POST.get('tiempo_muerto')

        # === 2. Convertir minutos a intervalo (PostgreSQL usa 'interval') ===
        duracion_falla = timedelta(minutes=int(tiempo_muerto)) if tiempo_muerto else None

        # === 3. Guardar en la tabla 'reporte_falla' ===
        ReporteFalla.objects.create(
            fecha=fecha,
            nombre_reporta=tecnico,           # técnico que reporta
            id_maquina=linea,                 # usamos la línea como id_maquina
            nombre_maquina=operacion,         # operación / máquina seleccionada
            ubicacion="Planta Principal",     # fijo por ahora
            hora_falla="08:00",               # fijo por ahora
            descripcion_falla=falla,
            tipo_falla=tipo_falla,
            duracion_falla=duracion_falla,
            tipo_mantenimiento="correctivo",  # 👈 aquí el cambio clave (minúsculas)
            tarea_solucion=actividad,
            refacciones_usadas=refacciones,
        )

        messages.success(request, 'Formulario guardado exitosamente')
        return redirect('index')

    return render(request, "formulario/index.html")
