from django.contrib import admin


from .models import Aerosol, Venta, Cliente



admin.site.register(Aerosol)
admin.site.register(Venta)
# Register your models here.

admin.site.register(Cliente)