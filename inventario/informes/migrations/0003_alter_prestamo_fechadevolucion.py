# Generated by Django 4.1.7 on 2023-03-22 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informes', '0002_alter_prestamo_fechadevolucion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='FechaDevolucion',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha Entrega'),
        ),
    ]
