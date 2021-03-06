# Generated by Django 2.1.4 on 2018-12-23 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
                ('compras', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.Venta')),
            ],
        ),
    ]
