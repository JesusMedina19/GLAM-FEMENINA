# Generated by Django 5.1.2 on 2024-11-04 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0024_alter_producto_id_categoria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='id_categoria',
            new_name='categoria',
        ),
    ]
