from django.db import models

# Create your models here.
class Carta(models.Model):
    titulo = models.CharField(
        max_length=200,
        help_text="Ej: Ábrelo cuando estés triste"
        )
    icono = models.CharField(
        max_length=10, 
        default="✉️", 
        help_text="Emoji o icono para el sobre"
        )
    contenido = models.TextField(
        help_text="Mensaje o carta especial"
        )
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Razon(models.Model):
    texto = models.CharField(
        max_length=300,
        help_text="Ej: Tu sonrisa ilumina el día"
    )
    orden = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name_plural = "Razones"

    def __str__(self):
        return f"{self.orden}.- {self.texto}"

class Cupon(models.Model):
    titulo = models.CharField(
        max_length=200,
        help_text="Ej: Vale por una cena"
    )
    descripcion = models.TextField(
        blank=True,
        help_text="Detalles del cupón"
    )
    canjeado = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Cupones"

    def __str__(self):
        return f"{self.titulo} - {'Canjeado' if self.canjeado else 'Disponible'}"

class Recuerdo(models.Model):
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='recuerdos/')
    descripcion = models.TextField(blank=True)
    fecha = models.DateField()

    def __str__(self):
        return self.titulo