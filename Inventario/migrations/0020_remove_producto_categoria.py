# Generated by Django 5.1.2 on 2024-11-04 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0019_alter_producto_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='categoria',
        ),
    ]