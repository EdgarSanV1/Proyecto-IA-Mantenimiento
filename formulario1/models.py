from django.db import models

class ReporteFalla(models.Model):
    id = models.BigAutoField(primary_key=True)  # usa la secuencia reporte_falla_id_seq

    fecha = models.DateField()
    nombre_reporta = models.CharField(max_length=120)
    id_maquina = models.CharField(max_length=60)
    nombre_maquina = models.CharField(max_length=120)
    ubicacion = models.CharField(max_length=120)
    hora_falla = models.TimeField()
    descripcion_falla = models.TextField()
    tipo_falla = models.CharField(max_length=120)

    # interval -> DurationField en Django
    duracion_falla = models.DurationField(null=True, blank=True)

    tipo_mantenimiento = models.CharField(max_length=50, null=True, blank=True)
    tarea_solucion = models.TextField(null=True, blank=True)
    refacciones_usadas = models.TextField(null=True, blank=True)

    # lo llena la BD con DEFAULT now(), así que lo marcamos como opcional
    fecha_registro = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "reporte_falla"  
        managed = False             

    def __str__(self):
        return f"{self.fecha} - {self.nombre_maquina} - {self.tipo_falla}"
