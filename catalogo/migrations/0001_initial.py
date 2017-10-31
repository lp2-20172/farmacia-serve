# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 15:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('direccion', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'Almacen',
                'verbose_name_plural': 'Almacenes',
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Area',
                'verbose_name_plural': 'Area',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruc', models.CharField(max_length=11)),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Person')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_doc', models.CharField(max_length=16)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('precio_total', models.FloatField(default=0.0)),
                ('almacen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Almacen')),
                ('comprador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
            },
        ),
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_doc', models.CharField(max_length=16)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('cantidad', models.FloatField(default=0)),
                ('precio_unitario', models.FloatField(default=0.0)),
            ],
            options={
                'verbose_name': 'DetalleCompra',
                'verbose_name_plural': 'DetalleCompras',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('codigo', models.CharField(blank=True, max_length=10, null=True)),
                ('detalle', models.TextField(blank=True, null=True)),
                ('fechaVen', models.DateField()),
                ('precio_venta', models.FloatField(default=0.0)),
                ('almacen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Almacen')),
                ('categoria', models.ManyToManyField(blank=True, null=True, to='catalogo.Categoria', verbose_name='list of Categorias')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=10)),
                ('ruc', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
            },
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(max_length=15)),
                ('precio_uni', models.FloatField(default=0)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Producto')),
            ],
            options={
                'verbose_name': 'ShoppingCart',
                'verbose_name_plural': 'ShoppingCarts',
            },
        ),
        migrations.CreateModel(
            name='UnidadMed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('nombre', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'verbose_name': 'UnidadMed',
                'verbose_name_plural': 'UnidadMeds',
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_doc', models.CharField(max_length=15)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('total', models.FloatField(default=0)),
                ('almacen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Almacen')),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.Cliente')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
            },
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Venta'),
        ),
        migrations.AddField(
            model_name='producto',
            name='unidad_med',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.UnidadMed'),
        ),
        migrations.AddField(
            model_name='compra',
            name='proveedor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Proveedor'),
        ),
    ]
