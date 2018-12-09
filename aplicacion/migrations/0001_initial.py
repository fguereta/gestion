# Generated by Django 2.1.4 on 2018-12-09 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aerosol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=30)),
                ('cantidad', models.IntegerField(default=0)),
                ('marca', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=0)),
                ('aerosol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.Aerosol')),
            ],
        ),
    ]