# Generated by Django 4.0.1 on 2022-02-12 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0006_remove_producto_categoria_producto_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, default='producto/default.jpg', upload_to='producto/%Y/%m/%d/'),
        ),
    ]
