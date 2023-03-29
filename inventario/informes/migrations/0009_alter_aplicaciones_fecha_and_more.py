# Generated by Django 4.1.7 on 2023-03-22 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informes', '0008_alter_aplicaciones_fecha_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aplicaciones',
            name='fecha',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='FechaDevolucion',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha Entrega'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='FechaInicio',
            field=models.DateTimeField(verbose_name='Fecha Inicio'),
        ),
    ]
