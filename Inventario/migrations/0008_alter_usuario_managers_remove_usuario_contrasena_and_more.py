# Generated by Django 5.1.2 on 2024-10-20 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0007_alter_usuario_contrasena'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='usuario',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='contrasena',
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
