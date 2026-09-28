from django.db import models
from django.core.validators import MinValueValidator


class Categoria(models.Model):
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField()
    precio = models.IntegerField()
    stock = models.IntegerField(validators=[MinValueValidator(0)])
    activo = models.BooleanField(default=False)
    creado = models.DateTimeField()
    codigo = models.CharField(max_length=20)

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=models.Q(stock__gte=0),
                name='producto_stock_non_negative',
            ),
        ]

    def __str__(self):
        return self.nombre
