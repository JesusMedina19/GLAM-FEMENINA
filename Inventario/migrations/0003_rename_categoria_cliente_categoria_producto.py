# Generated by Django 5.1.2 on 2024-10-18 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0002_rename_sale_ventas'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categoria_Cliente',
            new_name='Categoria_Producto',
        ),
    ]
