# Generated by Django 5.1.2 on 2024-10-21 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0011_alter_usuario_contrasena'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='contrasena',
        ),
    ]
