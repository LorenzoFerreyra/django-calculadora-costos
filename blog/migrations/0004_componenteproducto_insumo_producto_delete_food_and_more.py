# Generated by Django 5.2.1 on 2025-05-30 23:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200404_0411'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComponenteProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_utilizada', models.DecimalField(decimal_places=3, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=12)),
                ('unidad', models.CharField(choices=[('kilo', 'Kilo/Litro'), ('unidad', 'Unidad')], max_length=20)),
                ('fecha', models.DateField()),
                ('categoria', models.CharField(choices=[('insumo', 'Insumo'), ('packaging', 'Packaging'), ('topping', 'Topping'), ('energia', 'Energía'), ('mano_obra', 'Mano de obra')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('cantidad_producida', models.PositiveIntegerField(help_text='Cantidad de unidades producidas por receta base')),
                ('unidades_por_combo', models.PositiveIntegerField(default=1)),
                ('margen_ganancia', models.DecimalField(decimal_places=2, help_text='Ej: 200 para 200%', max_digits=5)),
            ],
        ),
        migrations.DeleteModel(
            name='Food',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.DeleteModel(
            name='Transport',
        ),
        migrations.AddField(
            model_name='componenteproducto',
            name='insumo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.insumo'),
        ),
        migrations.AddField(
            model_name='componenteproducto',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='componentes', to='blog.producto'),
        ),
    ]
