# Generated by Django 4.1.7 on 2023-03-22 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='FechaDevolucion',
            field=models.DateTimeField(blank=True, verbose_name='Fecha Entrega'),
        ),
    ]