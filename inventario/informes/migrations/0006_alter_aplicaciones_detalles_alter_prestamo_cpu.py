# Generated by Django 4.1.7 on 2023-03-22 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informes', '0005_rename_nombrepc_prestamo_identificador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aplicaciones',
            name='detalles',
            field=models.CharField(blank=True, max_length=70),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='CPU',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]