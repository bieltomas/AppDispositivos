# Generated by Django 4.1.7 on 2023-03-22 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('informes', '0004_alter_prestamo_observaciones'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prestamo',
            old_name='NombrePC',
            new_name='Identificador',
        ),
    ]
