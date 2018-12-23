from django.db import models



class Aerosol(models.Model):
	color=models.CharField(max_length=30)
	cantidad=models.IntegerField(default=0)
	marca=models.CharField(max_length=30)

	def __str__(self):
		return self.color


class Venta(models.Model):

	aerosol = models.ForeignKey(Aerosol, on_delete=models.CASCADE)
	cantidad=models.IntegerField(default=0)

class Cliente(models.Model):


	nombre=models.CharField(max_length=30)
	apellido=models.CharField(max_length=30)
	telefono=models.CharField(max_length=30)
	correo=models.CharField(max_length=30)
	direccion=models.CharField(max_length=30)
	compras = models.ForeignKey(Venta, on_delete=models.CASCADE)









