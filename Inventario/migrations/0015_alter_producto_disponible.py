# Generated by Django 5.1.2 on 2024-11-02 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0014_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='disponible',
            field=models.PositiveBigIntegerField(),
        ),
    ]