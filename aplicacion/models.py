from django.db import models



class Aerosol(models.Model):
	color=models.CharField(max_length=30)
	cantidad=models.IntegerField(default=0)
	marca=models.CharField(max_length=30)


class Venta(models.Model):

	aerosol = models.ForeignKey(Aerosol, on_delete=models.CASCADE)
	cantidad=models.IntegerField(default=0)

